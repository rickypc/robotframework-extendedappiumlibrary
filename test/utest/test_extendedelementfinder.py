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

from sys import path
path.append('src')
from ExtendedAppiumLibrary.locators import ExtendedElementFinder
import mock
import unittest


class ExtendedElementFinderTests(unittest.TestCase):
    """ExtendedElementFinder keyword test class."""

    def setUp(self):
        """Instantiate the extended element finder class."""
        self.browser = mock.Mock()
        self.finder = ExtendedElementFinder()

    def test_should_have_extended_strategies(self):
        """Extended Element Finder instance should contain extended strategies of
        UI Automator and UI Automation.
        """
        self.assertTrue('android' in self.finder._strategies)
        self.assertTrue('ios' in self.finder._strategies)

    def test_should_use_android_finder(self):
        """android strategy should use android finder."""
        self.finder.find(self.browser, 'android=UI Automator', tag=None)
        self.browser.find_elements_by_android_uiautomator("UI Automator")

    def test_should_use_ios_finder(self):
        """ios strategy should use ios finder."""
        self.finder.find(self.browser, 'ios=UI Automation', tag=None)
        self.browser.find_elements_by_ios_uiautomation("UI Automation")
