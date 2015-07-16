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

from AppiumLibrary.locators import ElementFinder


class ExtendedElementFinder(ElementFinder):
    """Extend parent class with UI Automation and UI Automator locators support."""

    def __init__(self):
        """Initialize extended locators."""
        ElementFinder.__init__(self)
        strategies = {
            'android': self._find_by_android,
            'ios': self._find_by_ios,
        }
        self._strategies.update(strategies)

    def _find_by_android(self, browser, criteria, tag, constraints):
        """Find element matches by UI Automator."""
        return self._filter_elements(
            browser.find_elements_by_android_uiautomator(criteria),
            tag, constraints)

    def _find_by_ios(self, browser, criteria, tag, constraints):
        """Find element matches by UI Automation."""
        return self._filter_elements(
            browser.find_elements_by_ios_uiautomation(criteria),
            tag, constraints)
