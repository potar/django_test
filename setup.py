# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import django_test
version = django_test.__version__

setup(
    name='django_test',
    version=version,
    author='',
    author_email='Your email',
    packages=[
        'django_test',
    ],
    include_package_data=True,
    install_requires=[
        'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['django_test/manage.py'],
)