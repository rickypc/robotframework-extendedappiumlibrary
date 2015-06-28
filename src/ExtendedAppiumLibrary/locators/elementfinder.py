#!/usr/bin/env python
# -*- coding: utf-8 -*-

#    Extended Appium Library - an Appium testing library with UI Automation and UI Automator support.
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

from AppiumLibrary.locators import ElementFinder


class ExtendedElementFinder(ElementFinder):
    def __init__(self):
        self._strategies = {
            'accessibility_id': self._find_element_by_accessibility_id,
            'android': self._find_by_android,
            'class': self._find_by_class_name,
            'css': self._find_by_css_selector,
            'id': self._find_by_id,
            'identifier': self._find_by_identifier,
            'ios': self._find_by_ios,
            'link': self._find_by_link_text,
            'name': self._find_by_name,
            'tag': self._find_by_tag_name,
            'xpath': self._find_by_xpath,
            None: self._find_by_default
        }

    def _find_by_android(self, browser, criteria, tag, constraints):
        return self._filter_elements(
            browser.find_elements_by_android_uiautomator(criteria),
            tag, constraints)

    def _find_by_ios(self, browser, criteria, tag, constraints):
        return self._filter_elements(
            browser.find_elements_by_ios_uiautomation(criteria),
            tag, constraints)
