#!/usr/bin/env python

"""The setup script for the OddEvenGame package."""

import io
from os import path as op
from setuptools import setup, find_packages

# Read the README file for the long description
with open('README.md', encoding='utf-8') as readme_file:
    readme = readme_file.read()

# Set up the absolute path to the current directory
here = op.abspath(op.dirname(__file__))

# Parse the requirements file for dependencies
with io.open(op.join(here, "requirements.txt"), encoding="utf-8") as f:
    all_reqs = f.read().splitlines()

install_requires = [x.strip() for x in all_reqs if x.strip() and not x.startswith("#")]
dependency_links = [x.strip().replace("git+", "") for x in all_reqs if "git+" in x]

setup(
    author="Siddharth Yadav",
    author_email="siddharthdis3432@gmail.com",
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Games/Entertainment :: Simulation",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    description="A fun and interactive Odd-Even cricket game where you play against the computer.",
    install_requires=install_requires,
    dependency_links=dependency_links,
    license="MIT License",
    long_description=readme,
    long_description_content_type="text/markdown",
    include_package_data=True,
    keywords=[
        "OddEvenGame", "Odd Even Game", "Cricket Game", "Odd Even", 
        "Python Game", "Interactive Game", "Siddharth Yadav"
    ],
    name="OddEvenGame",
    packages=find_packages(include=["oddevengame", "oddevengame.*"]),
    setup_requires=["wheel"],
    url="https://github.com/siddharthdis/OddEvenGame",
    version="0.0.15",
    zip_safe=False,
)
