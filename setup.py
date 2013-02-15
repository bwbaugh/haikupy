# Copyright (C) 2013 Brian Wesley Baugh
from setuptools import setup, find_packages


program_name = "haikupy"
version = '0.0.1'


setup(
    name=program_name,
    version=version,
    packages=find_packages(),

    install_requires=open('requirements.txt').read(),
    zip_safe=False,

    author="B. W. Baugh",
    author_email="brian@brianbaugh.com",
    url="http://www.github.com/bwbaugh/" + program_name,
    long_description=open('README.md').read(),
    classifiers=[
        "Programming Language :: Python",
        ],
)
