# -*- coding: utf-8 -*-
from setuptools import setup

setup(
    name="booley",
    version="0.1.0",
    author="Alberto Casero",
    author_email="kas.appeal@gmail.com",
    include_package_data=True,
    url="http://pypi.python.org/pypi/booley/",
    license="LICENSE.txt",
    description="A meta-language to evaluate boolean expressions using a dict keys as context variables.",
    install_requires=["pyparsing"],
)