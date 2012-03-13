#!/usr/bin/python
from distutils.core import setup
import sys
import os
import re

if os.path.isfile("MANIFEST"):
    os.unlink("MANIFEST")

verpat = re.compile("__version__ *= *\"(.*)\"")
data = open("editmoin").read()
m = verpat.search(data)
if not m:
    sys.exit("error: can't find __version__")
VERSION = m.group(1)

setup(name="editmoin",
      version = VERSION,
      description = "Edit Moin pages remotely with your preferred editor",
      author = "Gustavo Niemeyer",
      author_email = "gustavo@niemeyer.net",
      url = "http://labix.org/editmoin",
      license = "GPL",
      long_description = 
"""\
This program allows you to edit moin (see http://moinmo.in)
pages with your preferred editor. It means you can easily edit your
pages, without the usual limitations of most web browsers' text areas.
""",
      scripts = ["editmoin"],
      data_files = [('share/man/man1', ['editmoin.1'])],
      )
