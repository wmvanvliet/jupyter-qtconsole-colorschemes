======================================
 Color Schemes for IPython QT Console
======================================

Various color schemes for `IPython <http://ipython.org/>`_ QT Console.

List of color schemes
=====================

* Solarized (Light and Dark)
* Tomorrow
* Zenburn

HowTo
=====

Add ``*.py`` files to your Python distribution's
``/site-packages/pygments/styles`` folder. Then put the style names (e.g.:
``solarizedlight`` or ``solarizeddark``) for the option
``c.IPythonWidget.syntax_style`` in your ``ipython_qtconsole_cofig.py`` file::

    c.IPythonWidget.syntax_style = "solarizeddark"

For the stylesheet (``.css``), you can either start QT console with
``--stylesheet=solarizeddark.css`` option or put path to the css file into the
option ``c.IPythonQtConsoleApp.stylesheet`` in your
``ipython_qtconsole_config.py`` file::

    c.IPythonQtConsoleApp.stylesheet = "/path/to/solarizeddark.css"

