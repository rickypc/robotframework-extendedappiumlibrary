Extended Appium mobile native app testing library for Robot Framework
=====================================================================

Introduction
------------

ExtendedAppiumLibrary is an Appium_ mobile native app testing library
for `Robot Framework`_ with `iOS UIAutomation`_ and `Android UIAutomator`_ support
that leverages the AppiumLibrary_ project.

More information about this library can be found in the `Keyword Documentation`_.

Installation
------------

Using ``pip``
'''''''''''''

The recommended installation method is using pip_:

.. code:: bash

    pip install robotframework-extendedappiumlibrary

The main benefit of using ``pip`` is that it automatically installs all
dependencies needed by the library. Other nice features are easy upgrading
and support for un-installation:

.. code:: bash

    pip install --upgrade robotframework-extendedappiumlibrary
    pip uninstall robotframework-extendedappiumlibrary

Notice that using ``--upgrade`` above updates both the library and all
its dependencies to the latest version. If you want, you can also install
a specific version or upgrade only the Appium-Python-Client project used by the library:

.. code:: bash

    pip install robotframework-extendedappiumlibrary==x.x.x
    pip install --upgrade Appium-Python-Client
    pip install Appium-Python-Client==x.xx

Proxy configuration
'''''''''''''''''''

If you are behind a proxy, you can use ``--proxy`` command line option
or set ``http_proxy`` and/or ``https_proxy`` environment variables to
configure ``pip`` to use it. If you are behind an authenticating NTLM proxy,
you may want to consider installing CNTML_ to handle communicating with it.

For more information about ``--proxy`` option and using pip with proxies
in general see:

- http://pip-installer.org/en/latest/usage.html
- http://stackoverflow.com/questions/9698557/how-to-use-pip-on-windows-behind-an-authenticating-proxy
- http://stackoverflow.com/questions/14149422/using-pip-behind-a-proxy

Manual installation
'''''''''''''''''''

If you do not have network connection or cannot make proxy to work, you need
to resort to manual installation. This requires installing both the library
and its dependencies yourself.

- Make sure you have `Robot Framework installed`_.

- Download source distributions (``*.tar.gz``) for the library and its dependencies:

  - https://pypi.python.org/pypi/robotframework-extendedappiumlibrary
  - https://pypi.python.org/pypi/robotframework-appiumlibrary
  - https://pypi.python.org/pypi/Appium-Python-Client

- Download PGP signatures (``*.tar.gz.asc``) for signed packages.

- Find each public key used to sign the package:

.. code:: bash

    gpg --keyserver pgp.mit.edu --search-keys D1406DE7

- Select the number from the list to import the public key

- Verify the package against its PGP signature:

.. code:: bash

    gpg --verify robotframework-extendedappiumlibrary-x.x.x.tar.gz.asc robotframework-extendedappiumlibrary-x.x.x.tar.gz

- Extract each source distribution to a temporary location.

- Go to each created directory from the command line and install each project using:

.. code:: bash

       python setup.py install

If you are on Windows, and there are Windows installers available for
certain projects, you can use them instead of source distributions.
Just download 32bit or 64bit installer depending on your system,
double-click it, and follow the instructions.

Directory Layout
----------------

doc/
    `Keyword documentation`_

src/
    Python source code

test/
     Test files

     utest/
           Python unit test

Usage
-----

To write tests with Robot Framework and ExtendedAppiumLibrary,
ExtendedAppiumLibrary must be imported into your Robot test suite.
See `Robot Framework User Guide`_ for more information.

Building Keyword Documentation
------------------------------

The `Keyword Documentation`_ can be found online, if you need to generate the keyword documentation, run:

.. code:: bash

    make doc

Run Unit Tests and Test Coverage Report
---------------------------------------

.. code:: bash

    make test

License
-------

Copyright (c) 2015 Richard Huang.

This library is free software, licensed under: `GNU Affero General Public License (AGPL-3.0)`_.

Documentation and other similar content are provided under `Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License <http://creativecommons.org/licenses/by-nc-sa/4.0/>`_.

.. _Android UIAutomator: https://developer.android.com/tools/testing-support-library/index.html#UIAutomator
.. _Appium: http://appium.io/
.. _AppiumLibrary: https://jollychang.github.io/robotframework-appiumlibrary/doc/AppimuLibrary.html
.. _CNTML: http://cntlm.sourceforge.net
.. _GNU Affero General Public License (AGPL-3.0): http://www.gnu.org/licenses/agpl-3.0.en.html
.. _iOS UIAutomation: https://developer.apple.com/library/mac/documentation/DeveloperTools/Conceptual/InstrumentsUserGuide/UsingtheAutomationInstrument/UsingtheAutomationInstrument.html
.. _Keyword Documentation: https://rickypc.github.io/robotframework-extendedappiumlibrary/doc/ExtendedAppiumLibrary.html
.. _pip: http://pip-installer.org
.. _Robot Framework: http://robotframework.org
.. _Robot Framework installed: http://code.google.com/p/robotframework/wiki/Installation
.. _Robot Framework User Guide: http://code.google.com/p/robotframework/wiki/UserGuide
