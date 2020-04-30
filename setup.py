#!/usr/bin/env python

VERSION = '1.0'

from io import open
from os import path
from setuptools import setup

here = path.abspath(path.dirname(__file__))


def main():

    packages = ['svalinn_tools]
    package_data = {'': ['*.png']}
    setup_kwargs = {
        "name": "svalinn_tools",
        "version": VERSION,
        "description": 'DAGMC Visualization Tools',
        "long_description": open(path.join(here,'README.md')).read(),
        "long_description_content_type": 'text/markdown',
        "author": 'Svalinn Development Team',
        "url": 'https://github.com/svalinn/DAGMC-viz',
        "classifiers": ['Programming Language :: Python :: 2.7'],
        "install_requires": ['numpy'],
        "packages": packages,
        "package_data": package_data,
        "entry_points": {
                        "console_scripts": ["graveyard_removal = svalinn_tools.graveyard_removal:main",
                                            "data_loading = svalinn_tools.data_loading:main",
                                            "tag_expansion = svalinn_tools.tag_expansion:main"],
                        }
        }
    rtn = setup(**setup_kwargs)

    return rtn


if __name__ == "__main__":
    main()
