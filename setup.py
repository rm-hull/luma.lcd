#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from io import open
from setuptools import setup


def read_file(fname, encoding='utf-8'):
    with open(os.path.join(os.path.dirname(__file__), fname), encoding=encoding) as r:
        return r.read()


README = read_file("README.rst")
CONTRIB = read_file("CONTRIBUTING.rst")
CHANGES = read_file("CHANGES.rst")
version = read_file("VERSION.txt").strip()

needs_pytest = {'pytest', 'test', 'ptr'}.intersection(sys.argv)
pytest_runner = ['pytest-runner'] if needs_pytest else []
test_deps = [
    'mock;python_version<"3.3"',
    'pytest>=3.1',
    'pytest-cov'
]

setup(
    name="luma.lcd",
    version=version,
    author="Richard Hull",
    author_email="richard.hull@destructuring-bind.org",
    description=("A library to drive PCD8544 and ST7735 LCDs"),
    long_description="\n\n".join([README, CONTRIB, CHANGES]),
    license="MIT",
    keywords="raspberry pi rpi lcd nokia 5110 display screen pcd8544 st7735 spi 84x48 160x128",
    url="https://github.com/rm-hull/luma.lcd",
    download_url="https://github.com/rm-hull/luma.lcd/tarball/" + version,
    namespace_packages=["luma"],
    packages=["luma.lcd"],
    zip_safe=False,
    install_requires=["luma.core>=1.1.0"],
    setup_requires=pytest_runner,
    tests_require=test_deps,
    extras_require={
        'docs': [
            'sphinx >= 1.5.3'
        ],
        'qa': [
            'rstcheck',
            'flake8'
        ],
        'test': test_deps
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Education",
        "Intended Audience :: Developers",
        "Topic :: Education",
        "Topic :: System :: Hardware",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6"
    ]
)
