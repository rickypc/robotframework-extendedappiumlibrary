Extended Appium Library End of Life (2015.07.26)
================================================

What does this mean?
--------------------

Extended Appium Library project has been merged back upstream to `Appium Library <https://github.com/jollychang/robotframework-appiumlibrary>`_ project via Github pull request `#55 <https://github.com/jollychang/robotframework-appiumlibrary/pull/55>`_.

The `android` and `ios` locator strategies have been accepted as part of `Appium Library`_ supported strategies and released at version `1.3.0 <https://pypi.python.org/pypi/robotframework-appiumlibrary>`. You can rest assured that you are going to continue to use both locator strategies as before without any problem, and seamless transition back from Extended Appium Library to Appium Library.

More information can be found in the `Appium Library Keyword Documentation <https://jollychang.github.io/robotframework-appiumlibrary/doc/AppimuLibrary.html>`_.

What's next?
------------

Uninstall Extended Appium Library
'''''''''''''''''''''''''''''''''

You need to uninstall Extended Appium Library to prevent any possible conflict.

.. code:: bash

    pip uninstall robotframework-extendedappiumlibrary

Upgrade to the latest Appium Library
''''''''''''''''''''''''''''''''''''

Please upgrade to the latest Appium Library.

.. code:: bash

    pip install -U robotframework-appiumlibrary

Thank you!
----------

I would like to take this opportunity to thank all of you (1300+ of you) who installed and tried this library.

Previous `README <README.old.rst>` and `Keyword Documentation`_ are still available for viewing.

.. _Keyword Documentation: https://rickypc.github.io/robotframework-extendedappiumlibrary/doc/ExtendedAppiumLibrary.html
