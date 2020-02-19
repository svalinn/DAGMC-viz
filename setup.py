#!/usr/bin/env python

from setuptools import setup
from io import open


VERSION = '0.1'


def main():

    packages = ['dagmc-viz']
    pack_dir = {'dagmc-viz': 'PythonTool'}
    setup_kwargs = {
        "name": "dagmc-viz",
        "version": VERSION,
        "description": 'DAGMC Visualization Tools',
        "long_description": open('README.md').read(),
        "author": 'Svalinn Development Team',
        "url": 'https://github.com/svalinn/DAGMC-viz',
        "packages": packages,
        "package_dir": pack_dir,
        }
    rtn = setup(**setup_kwargs)

    return rtn


if __name__ == "__main__":
    main()
