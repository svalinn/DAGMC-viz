#!/usr/bin/env python

VERSION = '0.1.0'

from io import open
from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))


def main():

    packages = ['dagmc-viz']
    pack_dir = {'dagmc-viz': 'scripts'}
    setup_kwargs = {
        "name": "dagmc-viz",
        "version": VERSION,
        "description": 'DAGMC Visualization Tools',
        "long_description": open(path.join(here,'README.md'), encoding = 'utf-8').read(),
        "author": 'Svalinn Development Team',
        "url": 'https://github.com/svalinn/DAGMC-viz',
        "classifiers": ['Programming Language :: Python :: 2.7'],
        "install_requires": ['numpy', 'pytest', 'xmldiff'],
        "packages": packages,
        "package_dir": pack_dir,
        }
    rtn = setup(**setup_kwargs)

    return rtn


if __name__ == "__main__":
    main()
