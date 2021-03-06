# searchtag.py

import re
import sqlalchemy as sa

from libweasyl import staff

from weasyl import define as d
from weasyl import files
from weasyl import ignoreuser
from weasyl import macro as m
from weasyl import orm
from weasyl import welcome
from weasyl.error import PostgresError
from weasyl.error import WeasylError


_TAG_DELIMITER = re.compile(r"[\s,]+")


def select(submitid=None, charid=None, journalid=None):
    return d.execute("SELECT st.title FROM searchtag st"
                     " INNER JOIN searchmap%s sm USING (tagid)"
                     " WHERE sm.targetid = %i"
                     " ORDER BY st.title",
                     [
                         "submit" if submitid else "char" if charid else "journal",
                         submitid if submitid else charid if charid else journalid
                     ], options="within")


def select_with_artist_tags(submitid):
    db = d.connect()
    tags = (
        db.query(orm.Tag.title, orm.SubmissionTag.is_artist_tag)
        .join(orm.SubmissionTag)
        .filter_by(targetid=submitid)
        .order_by(orm.Tag.title)
        .all())
    ret = []
    artist_tags = set()
    for tag, is_artist_tag in tags:
        ret.append(tag)
        if is_artist_tag:
            artist_tags.add(tag)
    return ret, artist_tags


def can_remove_tags(userid, ownerid):
    return userid == ownerid or userid in staff.MODS or 'k' not in d.get_config(ownerid)


def removable_tags(userid, ownerid, tags, artist_tags):
    if not can_remove_tags(userid, ownerid):
        return [tag for tag in tags if tag not in artist_tags]
    else:
        return tags


def select_list(map_table, targetids):
    if not targetids:
        return {}

    mt = map_table
    st = d.meta.tables['searchtag']
    q = (
        d.sa
        .select([mt.c.targetid, d.sa.func.array_agg(st.c.title)])
        .select_from(mt.join(st, mt.c.tagid == st.c.tagid))
        .where(mt.c.targetid.in_(targetids))
        .group_by(mt.c.targetid))

    db = d.connect()
    return dict(list(db.execute(q)))


def get_ids(names):
    result = d.engine.execute(
        "SELECT tagid, title FROM searchtag WHERE title = ANY (%(names)s)",
        names=list(names))

    return {row.title: row.tagid for row in result}


def suggest(userid, target):
    if not target:
        return []

    if userid:
        block = d.execute("SELECT tagid FROM blocktag WHERE userid = %i", [userid], options="within")

    query = list()
    target = d.get_search_tag(target)
    statement = ["SELECT title FROM searchtag WHERE title LIKE '%s%%'"]

    if userid and block:
        statement.append(" AND tagid NOT IN %s" % (d.sql_number_list(block),))

    for i in d.execute("".join(statement + [" ORDER BY title LIMIT 10"]), [target], options="within"):
        query.append(i)

    statement = ["SELECT title FROM searchtag WHERE title LIKE '%%%s%%' AND title NOT LIKE '%s%%'"]

    if userid and block:
        statement.append(" AND tagid NOT IN %s" % (d.sql_number_list(block),))

    for i in d.execute("".join(statement + [" ORDER BY title LIMIT 5"]), [target, target], options="within"):
        query.append(i)

    return query


def create(title):
    return d.engine.execute(
        "INSERT INTO searchtag (title) VALUES (%(tag_name)s) RETURNING tagid",
        tag_name=d.get_search_tag(title)
    ).scalar()


def tag_array(tagids):
    if not tagids:
        return None
    st = d.meta.tables['searchtag']
    return sa.func.array(
        sa.select([st.c.title])
        .where(st.c.tagid.in_(tagids))
        .as_scalar())


def parse_tags(text):
    tags = set()

    for i in _TAG_DELIMITER.split(text):
        tag = d.get_search_tag(i)

        if tag:
            tags.add(tag)

    return tags


def associate(userid, tags, submitid=None, charid=None, journalid=None):
    targetid = d.get_targetid(submitid, charid, journalid)

    # Assign table, feature, ownerid
    if submitid:
        table, feature = "searchmapsubmit", "submit"
        ownerid = d.get_ownerid(submitid=targetid)
    elif charid:
        table, feature = "searchmapchar", "char"
        ownerid = d.get_ownerid(charid=targetid)
    else:
        table, feature = "searchmapjournal", "journal"
        ownerid = d.get_ownerid(journalid=targetid)

    # Check permissions and invalid target
    if not ownerid:
        raise WeasylError("TargetRecordMissing")
    elif userid != ownerid and "g" in d.get_config(userid):
        raise WeasylError("InsufficientPermissions")
    elif ignoreuser.check(ownerid, userid):
        raise WeasylError("contentOwnerIgnoredYou")

    # Determine previous tags
    existing = d.engine.execute(
        "SELECT tagid, settings FROM {} WHERE targetid = %(target)s".format(table),
        target=targetid).fetchall()

    # Determine tag titles and tagids
    query = d.engine.execute(
        "SELECT tagid, title FROM searchtag WHERE title = ANY (%(tags)s)",
        tags=list(tags)).fetchall()

    newtags = list(tags - {x.title for x in query})

    if newtags:
        query.extend(
            d.engine.execute(
                "INSERT INTO searchtag (title) SELECT * FROM UNNEST (%(newtags)s) AS title RETURNING tagid, title",
                newtags=newtags
            ).fetchall())

    existing_tagids = {t.tagid for t in existing}
    entered_tagids = {t.tagid for t in query}

    # Assign added and removed
    added = entered_tagids - existing_tagids
    removed = existing_tagids - entered_tagids

    # Check removed artist tags
    if not can_remove_tags(userid, ownerid):
        existing_artist_tags = {t.tagid for t in existing if 'a' in t.settings}
        removed.difference_update(existing_artist_tags)
        entered_tagids.update(existing_artist_tags)

    # Remove tags
    if removed:
        d.engine.execute(
            "DELETE FROM {} WHERE targetid = %(target)s AND tagid = ANY (%(removed)s)".format(table),
            target=targetid, removed=list(removed))

    if added:
        d.execute("INSERT INTO %s VALUES %s" % (table, d.sql_number_series([[i, targetid] for i in added])))

        if userid == ownerid:
            d.execute(
                "UPDATE %s SET settings = settings || 'a' WHERE targetid = %i AND tagid IN %s",
                [table, targetid, d.sql_number_list(list(added))])

    if submitid:
        try:
            d.engine.execute(
                'INSERT INTO submission_tags (submitid, tags) VALUES (%(submission)s, %(tags)s)',
                submission=submitid, tags=list(entered_tagids))
        except PostgresError:
            result = d.engine.execute(
                'UPDATE submission_tags SET tags = %(tags)s WHERE submitid = %(submission)s',
                submission=submitid, tags=list(entered_tagids))

            assert result.rowcount == 1

        db = d.connect()
        db.execute(
            d.meta.tables['tag_updates'].insert()
            .values(submitid=submitid, userid=userid,
                    added=tag_array(added), removed=tag_array(removed)))
        if userid != ownerid:
            welcome.tag_update_insert(ownerid, submitid)

    files.append(
        "%stag.%s.%s.log" % (m.MACRO_SYS_LOG_PATH, feature, d.get_timestamp()),
        "-%sID %i  -T %i  -UID %i  -X %s\n" % (feature[0].upper(), targetid, d.get_time(), userid,
                                               " ".join(tags)))


def tag_history(submitid):
    db = d.connect()
    tu = d.meta.tables['tag_updates']
    pr = d.meta.tables['profile']
    return db.execute(
        sa.select([pr.c.username, tu.c.updated_at, tu.c.added, tu.c.removed])
        .select_from(tu.join(pr, tu.c.userid == pr.c.userid))
        .where(tu.c.submitid == submitid)
        .order_by(tu.c.updated_at.desc()))
