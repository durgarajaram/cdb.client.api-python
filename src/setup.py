#!/usr/bin/python
""" setup script """

import cdb
from distutils.core import setup
from distutils.file_util import move_file
import sys

setup(
    name="cdb",
    version=cdb.__version__,
    description="Configuration Database client",
    author="MICE",
    author_email='mice-cdb@jiscmail.ac.uk',
    packages=['cdb'],
    url="http://cdb.mice.rl.ac.uk",
    requires=["suds"],
    provides=["cdb"],
)

if sys.argv[1] == "sdist":
    move_file("dist/cdb-" + cdb.__version__ + ".tar.gz", "../dist")
