# -*- coding: utf-8 -*-
from setuptools import setup
from flake8_plone_api import __version__


short_description = \
    'Checks for code usages that can be replaced with Plone API method calls.'


long_description = '{0}\n{1}'.format(
    open('README.rst').read(),
    open('CHANGES.rst').read()
)


setup(
    name='flake8-plone-api',
    version=__version__,
    description=short_description,
    long_description=long_description,
    classifiers=[
        'Development Status :: 3 - Alpha',
        "Framework :: Plone",
        "Framework :: Plone :: 4.3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development',
    ],
    author='Gil Forcada Codinachs',
    author_email='gil.gnome@gmail.com',
    url='https://github.com/gforcada/flake8-plone-api',
    license='GPL 2.0',
    keywords='pep8 flake8 plone',
    py_modules=['flake8_plone_api', ],
    install_requires=[
        'flake8',
    ],
    entry_points={
        'flake8.extension': ['P00 = flake8_plone_api:CodingChecker'],
    },
)
