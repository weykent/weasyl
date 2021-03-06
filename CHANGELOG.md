Weasyl Changelog
================

v1.1.2: 2016-06-14
----------

Publicly visible changes:

 *  Makes collection thumbnails respect generated/custom user preference. (#36, @strain-113)
 *  Hides image and description for Twitter cards on age 18+ submissions. (#35, @Syfaro)
 *  Updates Google reCAPTCHA version used for account creation to version 2. (#37, @kfkitsune)
 *  Introduces array based tag searches to increase search performance. (#50, @charmander)

Internal changes:

 * Updates developer documentation to explain installing Weasyl in a Windows vagrant
   environment. (#32, @kfkitsune)
 * Fixes consistency of capitalization of 'Weasyl' and quotation of code in project
   README. (#41, @kfkitsune)
 * Includes the Weasyl 'libweasyl' library in the main site code, rather than being used as
   an external library dependency. (#40, #45, @weykent)
 * Fixes the upgrade-db make function with new introduced libweasyl changes. (#53, @strain-113)

v1.1.1: 2016-06-05
----------

Publicly visible changes:

 *  Fixes thumbnail alignments for Android stock browser. (#34, @taedixon)

v1.1: 2016-06-03
----------

Publicly visible changes:

 *  Adds API methods for journals and characters. (#22, #28, @Syfaro)
 *  Changes the year in the page footer's copyright line to the current year. (#29, #31, @kfkitsune)
 *  Recenters the positions of thumbnails. (#30, @strain-113)

Internal changes:

 * Updates versions of python library dependencies. (#23, @skylerbunny)
 * Creates a weasyl_test database when creating a test VM environment. (#24, @strain-113)
 * Fixes collection related Python tests. (#25, @charmander) 

2016-05-31
----------

Publicly visible changes:

 * Removes legacy thumbnail restore tool.

Internal changes:

 * Drops support for IE 6–8.
 * Removes unused functions in weasyl.files.
 * Stops consulting the unused loginaddress table so it can be removed.

2016-05-29
----------

Publicly visible changes:

 * Adds current e-mail address to /control/editemailpassword.

2016-05-28
----------

Internal changes:

 * Open source release.
 * Numerous changes to prepare for open source.
   - Adds a license.
   - Improves the README.
 * Fixes a bug in how submission media link urls were handled.
   - This was not visible in production due to nginx rewriting rules.
 * Many library versions have been bumped.

2016-04-16
----------

Publicly visible changes:

 * Allows users to log in after being suspended.
 * Adds title text to thumbnail bylines, allowing them to be read
   even when truncated.
 * Removes unnecessary alt text.
 * Requires comments for certain types of reports.
 * Displays a more useful error when commenting on a deleted submission.

2016-03-04
----------

Publicly visible changes:

 * Allows users to request a submission as a collection item.
 * Adds a setting to allow a user to prevent their submissions from being
   requested as a collection.
 * Adds a setting to allow a user to prevent notifications for items they've
   collected (for themselves).

Internal changes:

 * Allows moderators to clear the 'critique requested' flag on submissions.

2016-03-01
----------

Internal changes:

 * Shows information on a user's reporting history on the user's Staff Notes
   page.
 * Updates Python libweasyl library versions (minor version bumps).

2016-02-15
----------

Publicly visible changes:

 * Limits searches of site users to 100 results, preventing denial of
   service when too many results are returned.

Internal changes:

 * Warns moderators, on the moderator report page, if a reported user's
   galleries contain items with tags they have blacklisted.

2016-02-07
----------

Publicly visible changes:

 * Allows users to see journals from everyone, not just themselves, on the
   /search browse page when in SFW mode.
 * Prevents users from ignoring site moderators, admins, or directors.

2016-02-06
----------

Publicly visible changes:

 * Prevents diacritics in a username from breaking user pages.

Internal changes:

 * Prevents the admin tool from generating a login name with diacritics
   (but usernames with them are still allowed to be created by the tool).
 * Allows tests to run now that SFW mode requires access to cookies.

2016-01-29
----------

Publicly visible changes:

 * Adds SFW mode filtering feature to site.

2016-01-26
----------

Publicly visible changes:

 * Removes “βετα” from the header logo.
 * Adds notifications of comments and favorites on collected submissions.

Internal changes:

 * Removes old, unused password fields and registration table from the database.

2015-12-30
----------

Publicly visible changes:

 * Fixes reported content type list in mod tools' list reports.

2015-12-23
----------

Internal changes:

 * Controls staff membership with weasyl-staff.yaml file rather than
   static libweasyl code.
 * Updates library versions of twisted, raven, requests, oauth2, others.
   (weasyl-old specific)

2015-12-10
----------

Publicly visible changes:

 * Changess Aden and Weykent from technical to developers.
 * Adds Menageriecat and Mohrne to moderators.
 * Removes Kailys, Kauko, Ritty and Rooshoes from developers.
 * Lists staff as tech only if not also a director.
 * Adds two new reporting types for moderation.

Internal changes:

 * Grants technical access to directors.
 * Upgrades libweasyl to version 0.10.14.
 * Cleans up Changelog formatting

2015-11-18
----------

Publicly visible changes:

 * Adds Sketchfab as a multimedia embed option for submissions.
 * Updates web.py to 0.37+weasyl.1
   * Trailing newlines in URLs cause 404s and not 500s.


2015-11-09
----------

Publicly visible changes:

 * Changes width at which notifications appear in the main toolbar.


2015-11-05
----------

Internal changes:

 * Fixes whitespace and flake8 errors in moderation messages.


2015-10-26
----------

Publicly visible changes:

 * Removes Pinardilla from moderators, changes Suburbanfox from developers
   to moderators.

Internal changes:

 * Upgrades libweasyl to version 0.10.13.


2015-10-18
----------

Publicly visible changes:

 * Updates messages displayed for banned and suspended users.

Internal changes:

 * Updates the templates moderators may use to fill ban and suspend reasons.


2015-10-10
----------

Publicly visible changes:

 * Disables access to cookies through document.cookie.

Internal changes:

 * Upgrades libweasyl to version 0.10.12, updates psycopg2 and sqlalchemy.


2015-09-21
----------

Publicly visible changes:

 * Fixes a bug in uploading character submissions, when a cover image needs
   to be generated.

Internal changes:

 * Upgrades libweasyl to version 0.10.11.


2015-09-19
----------

Publicly visible changes:

 * Fixes a bug in identification of .mp3 files, when uploaded via multimedia
   submission.


2015-09-14
----------

Internal changes:

 * Upgrades Vagrant development installations to install with Debian 8.x.
 * Upgrades python libraries.
   * weasyl-old: zope.interface, pyOpenSSL, requests, python-memcached, mock
   * libweasyl: alembic, arrow, lxml, oauthlib, psycopg2, pytz, sqlalchemy
 * Upgrades libweasyl to version 0.10.8.


2015-09-13
----------

Internal changes:

 * Library updates: Twisted to version 15.4.0, crochet to 1.4.0.
 * Dozer memory analysis wrapper added to weasyl.tac, to facilitate analysis
   of Weasyl WSGI workers receiving traffic. 


2015-09-11
----------

Publicly visible changes:

 * Disables Markdown 'code blocks' created by indenting lines. There were
   complaints about this behavior; code blocks can still be created using
   triple quotation mark fencing. Weasyl Markdown FAQ updated to show this.
 * Markdown previews now properly match output displayed on saved markdown
   text, because inconsistency of code blocks created on line indents has
   been resolved. 

Internal changes:

 * Libweasyl updated to 0.10.7, updating Misaka to disable Markdown code
   blocks by line indents.


2015-09-03
----------

Publicly visible changes:

 * Fixes a bug where thumbnails for recently popular submissions would not
   display properly for users who had disabled custom thumbnails.

Internal changes:

 * Removed an CSRF API vunerability in which tokens are not sent in a request
   to favorite a submission. Reporter has been notified of the fix.


2015-08-24
----------

Publicly visible changes:

 * Fixes situations where a Weasyl username may overrun the space in which
   it is meant to be displayed, causing layout issues.
 * Fixes a bug where thumbnails for non-visual submissions in searches
   would not display correctly for users who had disabled custom thumbnails.

Internal changes:

 * 'Do nothing' is restored as the default moderator action. 


2015-08-21
----------

Publicly visible changes:

 * Speeds up viewing and deleting user messages/notifications in certain
   situations. (Libweasyl 0.10.4, 0.10.5, 0.10.6)

Internal changes:

 * Creates database index for welcome by type.
 * Updates libweasyl version to 0.10.6.


2015-08-20
----------

Internal changes:

 * Creates database index for welcome by otherid.
 * Updates libweasyl version to 0.10.5.


2015-08-19
----------

Internal changes:

 * Creates database index for welcome by referid and targetid.
 * Updates libweasyl version to 0.10.4.


2015-07-23
----------

Internal changes:

 * Fixes links and references to pypi installation to point to Weasyl's new
   devpi server.
 * Updates libweasyl version to 0.10.3.


2015-07-22
----------

Internal changes:

 * Makes required Python library version identifiers PEP 0440 compliant.
 * Updates libweasyl version to 0.10.2.


2015-07-14
----------

Publicly visible changes:

 * Allows a user to select system generated thumbnails if they do not wish
   to see those created or uploaded by a content submitter.

Internal changes:

 * Adds a jsonb_settings column to users' profiles for future use.
 * Adds jsonb setting for 'no custom thumbnail' user preference.
 * Updates libweasyl version to 0.10.1.


2015-07-07
----------

Publicly visible changes:

 * New 250 pixel tall thumbnails and varying width display released.


2015-07-03
----------

Publicly visible changes:

 * Adds informative page titles to more pages which did not have them before
   (Formerly simply 'Weasyl').

Internal changes:

 * Performs additional migrations in preparation for new thumbnails.
 * Fixes places where 'thumbnail-legacy' is not used and should be.
 * Fixes new thumbnails creation for multimedia submission type.
 * Changes whitespace in SQL queries to be more SQL idiomatic.
 * Updates libweasyl version to 0.9.15.


2015-07-01
----------

Publicly visible changes:

 * Filters submission notifications by rating preference if the rating of
   a submission has been raised since it was first submitted.

Internal changes:

 * Creates 'thumbnail-legacy' and 'thumbnail-generated' links internally
   for use in the New Thumbnails rollout.
 * Updates Vagrant: PostgreSQL is now installed as version 9.4, RabbitMQ
   packages are installed, default memory for a virtual machine is now 1024M.
 * Changes various internal thumbnail link names for new thumbnail rollout.
 * Updates libweasyl version to 0.9.14.


2015-06-27
----------

Publicly visible changes:

 * Makes minor clarifications to the community guidelines regarding the
   Collections policy.
 * Changes some of Weasyl's user errors for clarity.

Internal changes:

 * Changes how user-facing errors are generated and displayed. Whimsy
   reduced.


2015-06-24
----------

Publicly visible changes:

 * Revises the community and ratings guidelines.
 * Fixes browsing by category (Literature, multimedia, etc.) to persist the
   category properly when browsing 'next' pages.
 * Increases length of gender field from 25 to 100 characters.
 * Removes Armaina from moderator status (on hiatus)

Internal changes:

 * Updates libweasyl version to 0.9.13.


2015-06-19
----------

Publicly visible changes:

 * Fixes several cases where a user can overrun database field limits and
   is not stopped at input time. (Full name, catchphrase, etc.)

Internal changes:

 * Adds maxAspectRatio version of imageselect.js. This will have no effect
   until 'New Thumbnails' is released.


2015-06-12
----------

Publicly visible changes:

 * Embedding improvements for multimedia (YouTube, Vimeo, oEmbed services)

Internal changes:

 * Changes the postgresql-contrib library used in vagrant from 9.1 to 9.4.


2015-05-23
----------

Publicly visible changes:

 * Fixes journal browsing and searching as a guest.


2015-05-22
----------

Publicly visible changes:

 * Staff changes: Matt, moderator to admin. (libweasyl 0.9.11)
 * Fixes several places where a user could fail to see their own
   content due to rating or blocktags.
 * Fixes a bug that could prevent a user from seeing a friend's
   friends-only submission in a list of favorites.
 * Fixes an HTML error that was preventing some pull-down menu
   defaults from being selected on page load.
 * Fixes several issues around folder previews that could make
   counts inaccurate or show previews of rating-inappropriate
   submissions.

Internal changes:

 * libweasyl bumped to 0.9.12 (contains new thumbnail logic).
 * 250px thumbnail images are now generated along with the
   square thumbnails, but not used yet.
 * `thumbnail-250px` media entries are suppressed from the API.
   This filtering should be removed after the thumbnail transition.


2015-04-12
----------

Publicly visible changes:

 * Staff changes: Capps, removed from staff.
 * Significantly updated FAQ for Weasyl mainsite.
 * pdf.js (for pdf display) updated to version 1.1.1.
 * Displayed file limits on multimedia submit page corrected. Removed
   references to premium file limits.
 * Fixed price creation for commissions: price ranges for base prices,
   proper addition of add-ons. 

Internal changes:

 * Libweasyl bump to version 0.9.10.
 * pdf.js files now prebuilt.


2015-03-29
----------

Publicly visible changes:

 * Adds Vine ( https://vine.co/ ) as an embeddable multimedia submission
   option.
 * Comment boxes now have a formatting help link. Submit button text now
   green (consistent with other submit buttons on the site). Submit button
   moved to the left side of these boxes.
 * Fixes a bug which ignored changes to the friends-only setting when editing
   a journal. (Bug introduced in 2015-03-21 release)

Internal changes:

 * URLs for banner images now served by the CDN.
 * pdf.js is not built with each run of the Weasyl environment.


2015-03-23
----------

Publicly visible changes:

 * Makes the link to the browse page (when no search results are returned)
   a properly contrasting color against a dark background.
 * Rearranges submission messages buttons to be consistent with buttons
   in the message center for watches, journals and comments.
 * Allows transparent thumbnails to be properly uploaded for characters.

Internal changes:

 * Removes old unused stat collection.


2015-03-21
----------

Publicly visible changes:

 * Adds a 'Search terms help' link under most search boxes.
 * Updates several messages/directions to reflect the 10 character
   password requirement.
 * Moves 'Ratings Guidelines' from support to policy section, in page footer.
 * Commission min/max prices may now be equal.
 * Staff changes: Kihari, director -> admin. Tiger, admin -> director.
   Removes Term from admins. (libweasyl 0.9.8)

Internal changes:

 * `thumbnail-source` media links are no longer cleared.
 * Significant clean-up to use orm models where appropriate.
 * Sessions are no longer cleared on suspension/ban. This means that
   banned/suspended users will now see an error on the next page load,
   but it should speed up banning/suspending significantly.
 * Removes page caching for guest users on detail and profile controllers.
 * Fixes a bug where an image uploaded as a cover could prevent the user
   from uploading the same image as a submission.
 * URLs for covers and full submission images now also served by the CDN.


2015-03-08
---------

Publicly visible changes:

 * Changes password checks to a 10-character minimum with no additional
   requirements and adds a password strength meter.
 * Fixes serialization of non-ASCII search terms.
 * Adds confirmation and consistent styling to some buttons that deserve them.
 * Adds maxlength attribute to note title field.
 * Restores Matt (2170) to moderators. (libweasyl 0.9.7)

Internal changes:

 * Removes leftover define.redirect() from administrator user management.
 * Makes Vagrantfile more weasyl3-compatible.
 * Allows CAPTCHA verification to be disabled for registration.
 * Updates dependencies. (libweasyl 0.9.7)
 * Miscellaneous cleanup.


2015-03-01
----------

Publicly visible changes:

 * Adds Patreon to Social media autofill. Changes Reddit site expansions
   to `https:` from `http:`.
 * Fixes Markdown emphasis immediately after punctuation characters.
   (libweasyl 0.9.6)
 * Removes FayV (21) and Stereo (1010) from staff. Promotes Skylerbunny (2402)
   to Directors. (libweasyl 0.9.6)

Internal changes:

 * Cleanup of now unused search methods, as we no longer use keys.
 * Moderator action dropdown now defaults to a 'None' action, to help prevent
   accidental moderator actions being taken.
 * Hidden submissions are now identified as such on their display pages, to
   moderators.


2015-02-07
----------

Publicly visible changes:

 * Causes notifications for friends to remain when changing a submission to
   friends-only.
 * Changes registration form day and year selection to use dropdowns instead of
   `<input type="number">`s; the latter might not be submitted in IE10 on
   Windows Phone 8.
 * Updates footer link to Weasyl’s blog from <http://weasyl.tumblr.com/> to
   <http://blog.weasyl.com/>.
 * Restores FayV (21) to admins and removes struguri (4393) from directors.
   (libweasyl 0.9.5)

Internal changes:

 * Removes unnecessary uses of `libweasyl.html.formfeeds` and related macros.
 * Removes `libweasyl.html.formfeeds` and `libweasyl.html.attributes`.
   (libweasyl 0.9.5)
 * Removes `weasyl.api`’s dependency on the rest of weasyl-old, leaving it free
   to be moved into libweasyl.
 * Cleans up some queries to use SQLAlchemy.
 * Changes Markdown test to accept current output for Markdown
   nested in `<pre>`. (libweasyl 0.9.5)


2015-02-01
----------

Publicly visible changes:

 * Fixes an issue where insecure passwords could pass our checks. Existing
   passwords will not be changed but new passwords will have to agree with this
   policy: 'We require a minimum of eight characters, with at least three of:
   lowercase, uppercase, digit, and symbol characters.'
 * Fixes an issue where changes to a user's timezone were not being reflected.
 * In-gallery playback should now be more efficient.
 * Updates to phrasing on Community Guidelines to remove references to "female
   breasts" and clarify policies on minors in Mature- or Explicit-rated
   submissions.

Internal changes:

 * Random keys now use a more secure random function.
 * Significant code cleanup and refactoring such as removing many calls to
   `weasyl.define` (this actually went in last week).
 * Mods now have the ability to remove thumbnails and cover art from literary
   and multimedia submissions. Visual submission thumbnail reset is not
   implemented yet.
