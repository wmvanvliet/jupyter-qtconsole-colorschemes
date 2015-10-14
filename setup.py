#!/usr/bin/env python
from setuptools import setup

setup(
    name="color-schemes-for-jupyter-qtconsole",
    version="0.0",
    author="Joon Ro",
    author_email="joon.ro@outlook.com",
    description="Color Schemes for Jupyter Qt Console",
    packages=["jupyter_qtconsole_colorschemes"],
    package_data={"jupyter_qtconsole_colorschemes": ["*.css"]},
    entry_points={"pygments.styles": [
        "solarizeddark = jupyter_qtconsole_colorschemes.solarizeddark:SolarizeddarkStyle",
        "solarizedlight = jupyter_qtconsole_colorschemes.solarizedlight:SolarizedlightStyle",
        "tomorrow = jupyter_qtconsole_colorschemes.tomorrow:TomorrowStyle",
        "zenburn = jupyter_qtconsole_colorschemes.zenburn:ZenburnStyle"]}
)

