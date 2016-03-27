#!/usr/bin/env python

from os.path import exists
from setuptools import setup, find_packages

setup(
    name='flynn-utils',
    version=open('VERSION').read().strip(),
    # Your name & email here
    author='',
    author_email='',
    # If you had flynn_utils.tests, you would also include that in this list
    packages=find_packages(),
    # Any executable scripts, typically in 'bin'. E.g 'bin/do-something.py'
    scripts=[],
    url='https://github.com/adamcharnock/flynn-utils',
    license='MIT',
    description='Utilities for managing your flynn apps',
    long_description=open('README.rst').read() if exists("README.rst") else "",
    install_requires=[
        'click>=6.0',
    ],
    entry_points={
        'console_scripts': [
            'flynnutils = flynn_utils.cli:cli'
        ]
    }
)
