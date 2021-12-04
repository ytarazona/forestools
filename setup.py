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

requirements = ['Click>=7.0', ]

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Yonatan Tarazona",
    author_email='geoyons@gmail.com',
    python_requires='>=3.5',
    version="0.1.4",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Tools for detecting deforestation and forest degradation",
    install_requires=install_requires,
    dependency_links=dependency_links,
    license="MIT license",
    long_description=readme,
    long_description_content_type='text/markdown',
    include_package_data=True,
    keywords='forestools',
    name='forestools',
    packages=find_packages(include=['forestools', 'forestools.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/ytarazona/forestools',
    zip_safe=False,
)
