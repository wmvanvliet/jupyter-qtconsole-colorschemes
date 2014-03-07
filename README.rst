=================================
 IPython QtConsole Color Schemes
=================================

Pygments style file and .css file of Solarized theme for IPython QT console.

Add ``*.py`` files to your Python distribution's
``/site-packages/pygments/styles`` folder. Then use either ``solarizedlight``
or ``solarizeddark`` for the option ``c.IPythonWidget.syntax_style`` in your
``ipython_qtconsole_cofig.py`` file::

    c.IPythonWidget.syntax_style = "solarizeddark"

For ``solarizeddark.css`` file, and you
can either start QT console with ``--stylesheet=solarizeddark.css`` option or put
path to the css file into the option ``c.IPythonQtConsoleApp.stylesheet`` in
your ``ipython_qtconsole_config.py`` file::

    c.IPythonQtConsoleApp.stylesheet = "/path/to/solarizeddark.css"

