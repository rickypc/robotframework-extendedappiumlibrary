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

import AppiumLibrary
from ExtendedAppiumLibrary.locators import ExtendedElementFinder
from ExtendedAppiumLibrary.version import get_version

__version__ = get_version()


class ExtendedAppiumLibrary(AppiumLibrary.AppiumLibrary):
    """ExtendedAppiumLibrary is an Appium testing library for Robot Framework with UI Automation and UI Automator support.

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
    to find an element by specifying a lookup strategy as a locator prefix.

    Supported strategies are:

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
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

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
