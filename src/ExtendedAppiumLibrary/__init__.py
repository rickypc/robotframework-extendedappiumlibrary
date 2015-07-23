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

from AppiumLibrary import AppiumLibrary
from ExtendedAppiumLibrary.locators import ExtendedElementFinder
from ExtendedAppiumLibrary.version import get_version

__version__ = get_version()


class ExtendedAppiumLibrary(AppiumLibrary):
    # pylint: disable=line-too-long
    """ExtendedAppiumLibrary is an Appium mobile native app testing library for Robot Framework
    with iOS ``UI Automation`` and Android ``UI Automator`` support.

    See https://developer.apple.com/library/ios/documentation/DeveloperTools/Reference/UIAutomationRef/
    for more information on iOS ``UI Automation``.

    See https://developer.android.com/tools/testing-support-library/index.html#uia-apis
    for more information on Android ``UI Automator``.

    *Extended Locators Support*

    | *Extended Strategy* | *Example*                                                                       | *Description*                   |
    | android             | Click Element `|` android=new UiSelector().className("android.widget.TextView") | Matches by Android UI Automator |
    | ios                 | Click Element `|` ios=.buttons().withName('Continue')                           | Matches by iOS UI Automation    |

    *Locating elements*
    """
    # pylint: disable=line-too-long

    # let's not confuse people with different name
    __doc__ += AppiumLibrary.__doc__.split('*Locating elements*', 1)[-1]. \
        replace('AppiumLibrary', 'ExtendedAppiumLibrary')

    ROBOT_EXIT_ON_FAILURE = True
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    ROBOT_LIBRARY_VERSION = __version__

    def __init__(self, run_on_failure='Capture Page Screenshot'):
        # pylint: disable=line-too-long
        """ExtendedAppiumLibrary can be imported with optional arguments.

        `run_on_failure` specifies the name of a keyword (from any available
        libraries) to execute when a ExtendedAppiumLibrary keyword fails. By default

        `Capture Page Screenshot` will be used to take a screenshot of the current page.
        Using the value `No Operation` will disable this feature altogether. See

        `Register Keyword To Run On Failure` keyword for more information about this
        functionality.

        Examples:
        | Library | ExtendedAppiumLibrary | run_on_failure=No Operation | # Does nothing on failure |
        """
        # pylint: disable=line-too-long
        AppiumLibrary.__init__(self, run_on_failure)
        self._element_finder = ExtendedElementFinder()
