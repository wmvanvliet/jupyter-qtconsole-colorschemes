#!/usr/bin/env python
from setuptools import setup


setup(
    name="color-schemes-for-ipython-qtconsole",
    version="0.0",
    author="...",
    author_email="...",
    description="...",
    packages=["ipython_colorschemes"],
    package_data={"ipython_colorschemes": ["*.css"]},
    entry_points={"pygments.styles": [
        "solarizeddark = ipython_colorschemes.solarizeddark:SolarizeddarkStyle",
        "solarizedlight = ipython_colorschemes.solarizedlight:SolarizedlightStyle",
        "tomorrow = ipython_colorschemes.tomorrow:TomorrowStyle",
        "zenburn = ipython_colorschemes.zenburn:ZenburnStyle"]}
)
