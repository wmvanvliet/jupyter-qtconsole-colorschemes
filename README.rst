====================================
Color Schemes for Jupyter Qt Console
====================================

Original author: Joon Ro, this repo was forked by Marijn van Vliet.

Various color schemes for `Jupyter <http://jupyter.org>`_ `Qt Console <http://jupyter.org/qtconsole>`_. It was originally for `IPython <http://ipython.org>`_ Qt
Console, but as of IPython 4.0, the language-agnostic parts of the project
including the qtconsole have moved to new projects under the name
Jupyter. Each color scheme consists of a ``.py`` file for the pygments style and
a ``.css`` file for Qt Console specific color settings.

List of color schemes
---------------------

My current favorites are ``material-light`` and Base16 Ocean Dark.

- `Base16 <https://github.com/chriskempson/base16>`_

  - Ocean Dark (``base16_ocean_dark``)

- Blackboard (``blackboard``, thanks to `Marijn van Vliet <https://github.com/wmvanvliet/>`_)

- `Material Theme for Emacs <https://github.com/cpaulik/emacs-material-theme>`_

  - Light (``material_light``)

- `monokai <http://www.monokai.nl/blog/2006/07/15/textmate-color-theme/>`_ (``monokai``)

- `Solarized <http://ethanschoonover.com/solarized>`_ 

  - Light (``solarizedlight``)

  - Dark (``solarizeddark``)

- `Tomorrow <https://github.com/ChrisKempson/Tomorrow-Theme>`_: ``tomorrow``

- `Zenburn <http://kippura.org/zenburnpage/>`_: ``zenburn``

Installation
------------

Thanks to `Antony Lee <https://bitbucket.org/anntzer/>`_, now the color schemes are in a module called
``jupyter_qtconsole_colorschemes``. You can install it with ``pip``:

.. code:: sh

    pip install jupyter_qtconsole_colorschemes

Usage
-----

In ``~/.jupyter/jupyter_qtconsole_config.py``, add the following with the color
scheme name you want to use (the example shown with ``zenburn``):

.. code:: python

    color_theme = 'zenburn'  # specify color theme

    import importlib.util
    spec = importlib.util.find_spec("jupyter_qtconsole_colorschemes")
    if spec is None or not spec.submodule_search_locations:
        raise ImportError("jupyter_qtconsole_colorschemes not found")
    c.JupyterQtConsoleApp.stylesheet = f"{spec.submodule_search_locations[0]}/{color_theme}.css"
    c.JupyterWidget.syntax_style = color_theme



License
-------

Released under the `MIT License <LICENSE>`_
