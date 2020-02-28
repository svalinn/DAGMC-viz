#!/usr/bin/env python

VERSION = '0.1'

from setuptools import setup
from os import path
from io import open

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
        "packages": packages,
        "package_dir": pack_dir,
        }
    rtn = setup(**setup_kwargs)

    return rtn


if __name__ == "__main__":
    main()
