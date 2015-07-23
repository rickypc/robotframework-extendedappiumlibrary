#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Extended Appium Library - an Appium testing library
#    with UI Automation and UI Automator support.
#    Copyright (C) 2015  Richard Huang <rickypc@users.noreply.github.com>
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Extended Appium Library - an Appium testing library with UI Automation and UI Automator support.
"""

# To use a consistent encoding
import codecs
from os.path import abspath, dirname, join
# Always prefer setuptools over distutils
from setuptools import setup, find_packages

LIBRARY_NAME = 'ExtendedAppiumLibrary'
CWD = abspath(dirname(__file__))
execfile(join(CWD, 'src', LIBRARY_NAME, 'version.py'))

with codecs.open(join(CWD, 'README.rst'), encoding='utf-8') as reader:
    LONG_DESCRIPTION = reader.read()

setup(
    name='robotframework-%s' % LIBRARY_NAME.lower(),
    version=VERSION,  # pylint: disable=undefined-variable  # noqa
    description='Extended Appium mobile native app testing library for Robot Framework '
                'with iOS UI Automation and Android UI Automator support',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/rickypc/robotframework-%s' % LIBRARY_NAME.lower(),
    author='Richard Huang',
    author_email='rickypc@users.noreply.github.com',
    license='AGPL 3',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='robot framework extended testing automation appium mobile ios '
             'android uiautomation uiautomator native app apptesting softwaretesting '
             'appdev webdev selenium selenium2 webdriver',
    platforms='any',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['robotframework-appiumlibrary >= 1.2.5']
)
