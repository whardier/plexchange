#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# MIT License
#
# Copyright (c) 2018 Shane R. Spencer
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from setuptools import setup, find_packages
from pip.req import parse_requirements
import plexchange
import os

# Solution from http://bit.ly/29Yl8VN
def resolve_requires(requirements_file):
    requirements = parse_requirements("./%s" % requirements_file,
            session=False)
    return [str(ir.req) for ir in requirements]

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
# Solution from: http://bit.ly/2mig8RT
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

# We still running: python setup.py sdist upload --repository=testpypi
# Twine isn't handling long_descriptions as per:
# https://github.com/pypa/twine/issues/262
setup(
    name="plexchange",
    version=".".join(map(str,plexchange.__version__)),
    description="Exchange ActiveSync Multiplexer",
    long_description=read('README.md'),
    license="MIT",
    author="Shane Spencer",
    author_email="spencersr@gmail.com",
    maintainer="Shane Spencer",
    maintainer_email="spencersr@gmail.com",
    install_requires=resolve_requires("requirements/requirements.txt"),
    #extras_require = {
    #    'otherthing': resolve_requires("requirements/otherthing.txt"),
    #},
    url="https://github.com/whardier/plexchange",
    packages=find_packages(),
    package_dir={'plexchange': "plexchange"},
    include_package_data=True,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Environment :: Console",
        "Environment :: Web Environment",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
	"Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
	"Programming Language :: Python :: Implementation :: CPython",
	"Topic :: Communications :: Email",
        "Topic :: Internet :: Proxy Servers",
        "Topic :: Internet :: WWW/HTTP",
    ],
    #scripts=["plexchange/bin/plexchange-cli.py"],
    #entry_points={'console_scripts': [
    #    "plexchange = plexchange.management:run_from_command_line",
    #]},
)
