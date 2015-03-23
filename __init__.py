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

import AppiumLibrary
from ExtendedAppiumLibrary.locators import ExtendedElementFinder
from ExtendedAppiumLibrary.version import get_version

__version__ = get_version()


class ExtendedAppiumLibrary(AppiumLibrary.AppiumLibrary):
    """ExtendedAppiumLibrary is a App testing library with custom improvement for Robot Framework.

    *Locating elements*

    All keywords in ExtendedAppiumLibrary that need to find an element on the app
    take an argument, `locator`. By default, when a locator value is provided,
    it is matched against the key attributes of the particular element type.
    For example, `id` and `name` are key attributes to all elements, and
    locating elements is easy using just the `id` as a `locator`. For example::

    Click Element  my_element

    Appium additionally supports some of the _Mobile JSON Wire Protocol_
    (https://code.google.com/p/selenium/source/browse/spec-draft.md?repo=mobile) locator strategies
    It is also possible to specify the approach ExtendedAppiumLibrary should take
    to find an element by specifying a lookup strategy with a locator
    prefix. Supported strategies are:

    | *Strategy*        | *Example*                                                                       | *Description*                     |
    | identifier        | Click Element `|` identifier=my_element                                         | Matches by @id or @name attribute |
    | id                | Click Element `|` id=my_element                                                 | Matches by @id attribute          |
    | name              | Click Element `|` name=my_element                                               | Matches by @name attribute        |
    | xpath             | Click Element `|` xpath=//UIATableView/UIATableCell/UIAButton                   | Matches with arbitrary XPath      |
    | class             | Click Element `|` class=UIAPickerWheel                                          | Matches by class                  |
    | accessibility_id  | Click Element `|` accessibility_id=t                                            | Matches by Accessibility options  |
    | android           | Click Element `|` android=new UiSelector().className("android.widget.TextView") | Matches by Android UI Automator   |
    | ios               | Click Element `|` ios=.buttons().withName('Continue')                           | Matches by iOS UI Automation      |
    """

    ROBOT_EXIT_ON_FAILURE = True
    ROBOT_LIBRARY_SCOPE = 'TEST SUITE'

    def __init__(self, run_on_failure='Capture Page Screenshot'):
        """ExtendedAppiumLibrary can be imported with optional arguments.

        `run_on_failure` specifies the name of a keyword (from any available
        libraries) to execute when a ExtendedAppiumLibrary keyword fails. By default
        `Capture Page Screenshot` will be used to take a screenshot of the current page.
        Using the value `No Operation` will disable this feature altogether. See
        `Register Keyword To Run On Failure` keyword for more information about this
        functionality.

        Examples:
        | Library | ExtendedAppiumLibrary | run_on_failure=No Operation | # Sets default timeout to 10 seconds and does nothing on failure |
        """
        AppiumLibrary.AppiumLibrary.__init__(self, run_on_failure)
        self._element_finder = ExtendedElementFinder()