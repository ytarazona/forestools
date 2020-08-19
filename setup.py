#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="forestools",
    version="0.0.8",
    author="Yonatan Tarazona Coronel",
    author_email="geoyons@gmail.com",
    description="Tools for detecting deforestation and forest degradation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ytarazona/forestools",
    install_requires=[
      'numpy',
      'pandas'
    ],
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        "License :: OSI Approved :: MIT License",
        'Natural Language :: English',
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.5',
)

