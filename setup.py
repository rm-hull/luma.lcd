#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), "README.rst")).read()
CONTRIB = open(os.path.join(os.path.dirname(__file__), "CONTRIBUTING.rst")).read()
CHANGES = open(os.path.join(os.path.dirname(__file__), "CHANGES.rst")).read()
version = open(os.path.join(os.path.dirname(__file__), "VERSION.txt")).read()

setup(
    name="luma.lcd",
    version=version,
    author="Richard Hull",
    author_email="richard.hull@destructuring-bind.org",
    description=("A small library to drive the PCD8544 LCD"),
    long_description="\n\n".join([README, CONTRIB, CHANGES]),
    license="MIT",
    keywords="raspberry pi rpi lcd nokia 5110 display screen pcd8544 spi 84x48",
    url="https://github.com/rm-hull/luma.lcd",
    download_url="https://github.com/rm-hull/luma.lcd/tarball/" + version,
    namespace_packages=["luma"],
    packages=["luma.lcd"],
    install_requires=["luma.core"],
    setup_requires=["pytest-runner"],
    tests_require=["mock", "pytest", "pytest-cov", "python-coveralls"],
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Topic :: Education",
        "Topic :: System :: Hardware",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5"
    ]
)
