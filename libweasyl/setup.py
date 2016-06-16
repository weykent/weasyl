import os
import sys

from setuptools import setup
from pip.download import PipSession
from pip.req import parse_requirements


here = os.path.dirname(os.path.abspath(__file__))

# As of pip 6, parse_requirements requires a 'session' argument. This is required
# for remote files, but not local ones. In prior versions of pip, a blank
# PipSession object was used if no 'session' object was passed.
reqs = [str(r.req)
        for r in parse_requirements(
            os.path.join(here, 'requirements.txt'),
            session=PipSession())
        if r.req is not None]

if sys.version_info < (3, 3):
    reqs.append('backports.lzma')

if sys.version_info < (3, 4):
    reqs.append('enum34')


setup(
    name='libweasyl',
    description='common code across weasyl projects',
    author='Weasyl LLC',
    packages=[
        'libweasyl', 'libweasyl.models',
        'libweasyl.test', 'libweasyl.models.test',
    ],
    include_package_data=True,
    install_requires=reqs,
    extras_require={
        'development': [
            'coverage',
            'flake8',
            'pytest',
            'sphinx',
            'sphinxcontrib-napoleon',
            'tox',
            'vcversioner',
        ],
    },
    setup_requires=['vcversioner'],
    vcversioner={
        'version_file': os.path.join(here, 'version.txt'),
        'version_module_paths': ['libweasyl/_version.py'],
        # The git repo root is one directory above this setup.py.
        'root': os.path.dirname(here),
    },
)