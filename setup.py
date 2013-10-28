# coding=utf8

import glob
import os
import re

from distutils.core import setup


def get_version():
    return re.search(r"""__version__\s+=\s+(?P<quote>['"])(?P<version>.+?)(?P=quote)""", open('asiri/__init__.py').read()).group('version')

def find_packages(toplevel):
    return [directory.replace(os.path.sep, '.') for directory, subdirs, files in os.walk(toplevel) if '__init__.py' in files]

setup(name         = "asiri",
      version      = get_version(),
      author       = "Saúl Ibarra Corretgé",
      author_email = "saghul@gmail.com",
      url          = "https://github.com/saghul/python-asiri",
      description  = "Utilities for interfacing with Asiri board",
      classifiers  = [
            "Development Status :: 4 - Beta",
            "License :: OSI Approved :: BSD License",
            "Operating System :: OS Independent",
            "Programming Language :: Python"
                     ],
      packages     = find_packages("asiri"),
      )

