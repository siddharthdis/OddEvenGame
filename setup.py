#!/usr/bin/env python

"""The setup script."""

import io
from os import path as op
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

here = op.abspath(op.dirname(__file__))

# get the dependencies and installs
with io.open(op.join(here, "requirements.txt"), encoding="utf-8") as f:
    all_reqs = f.read().split("\n")

install_requires = [x.strip() for x in all_reqs if "git+" not in x]
dependency_links = [x.strip().replace("git+", "") for x in all_reqs if "git+" not in x]

requirements = [ ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Siddharth Yadav",
    author_email='siddharthdis3432@gmail.com',
    python_requires='>=3.8',
    classifiers=[
        'Intended Audience :: Developers',
        "Development Status :: 1 - Planning",
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Operating System :: Microsoft :: Windows',
    ],
    description="This is a game in which you have to play cricket with a computer.",
    install_requires=install_requires,
    dependency_links=dependency_links,
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords=['Game', 'Odd', 'Even', 'Odd Even', 'Odd Even game', 'Cricket', 'Cricket Game', "oddevengame", "OddEvenGame", 'Game with Computer', "Siddharth Yadav", "Siddharth", "Yadav"],
    name='OddEvenGame',
    packages=find_packages(include=['oddevengame', 'oddevengame.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/siddharthdis/OddEvenGame',
    version='0.0.12',
    zip_safe=False,
)
