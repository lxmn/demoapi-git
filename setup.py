# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages
import re

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()


def get_version():
    with open("demoapi/__version__.py") as f:
        for line in f:
            if line.startswith("__version__"):
                return eval(line.split("=")[-1])

setup(
    name='demoapi',
    version=get_version(),
    description='Sample package for Python API',
    long_description=readme,
    author='Laxman Kumar Mandal',
    author_email='lxmnkumar187@gmail.com',
    url='',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

