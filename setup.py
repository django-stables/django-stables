#!/usr/bin/env python
from setuptools import setup

setup(
    name='django-stables',
    version='0.1.0',
    description='Cross-project test metrics for Django and related "stable" packages.',
    long_description=open('README.rst').read(),
    author='Django Stables Team',
    author_email='tyson@clugg.net',
    url='https://github.com/django-stables/django-stables',
    license='MIT',
    packages=['stables'],
    install_requires=[
        'django>=1.8',
    ],
    tests_require=[
        'tox>=2.1',
    ],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Environment :: Web Environment",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Topic :: Development :: Testing",
        "Framework :: Django",
    ],
)
