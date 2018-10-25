#!/usr/bin/env python3

from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read

setup(name='mhall',
        version='1.0',
        description='A monty hall problem simulation',
        author='Nathan Cairns',
        long_desrciption=readme,
        license=license,
        packages=find_packages(exclude='docs','tests','examples')
        )
