# -*- coding: utf-8 -*-
from setuptools import setup


short_description = \
    'Checks for code usages that can be replaced with Plone API method calls.'


long_description = '{0}\n{1}'.format(
    open('README.rst').read(),
    open('CHANGES.rst').read()
)


setup(
    name='flake8-plone-api',
    version='1.2',
    description=short_description,
    long_description=long_description,
    # Get more from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Framework :: Plone :: 5.0',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
    ],
    keywords='pep8 flake8 plone',
    author='Gil Forcada',
    author_email='gil.gnome@gmail.com',
    url='https://github.com/gforcada/flake8-plone-api',
    license='GPL version 2',
    py_modules=['flake8_plone_api', ],
    include_package_data=True,
    test_suite='run_tests',
    zip_safe=False,
    install_requires=[
        'flake8',
    ],
    entry_points={
        'flake8.extension': ['P00 = flake8_plone_api:PloneAPIChecker'],
    },
)
