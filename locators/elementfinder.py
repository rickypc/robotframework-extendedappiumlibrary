#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright 2015 Richard Huang <rickypc@users.noreply.github.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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