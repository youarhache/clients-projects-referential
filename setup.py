#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='projectsref',
    version='0.1.0',
    description="A web API for managing clients projects, teams composition and skills following a clean architecture.",
    long_description=readme + '\n\n' + history,
    author="Youssef Ouarhache",
    author_email='youarhache@gmail.com',
    url='https://github.com/youarhache/projectsref',
    packages=[
        'projectsref',
    ],
    package_dir={'projectsref':
                 'projectsref'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='projectsref',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
