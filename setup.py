#!/usr/bin/env python3

from setuptools import setup
from setuptools import find_packages


setup(
    name="pcbhdl",
    version="0.1",
    description="Python toolbox for designing printed circuit boards",
    long_description=open("README.md").read(),
    author="whitequark",
    author_email="whitequark@whitequark.org",
    #url="https://pcbhdl.org",
    download_url="https://github.com/pcbhdl/pcbhdl",
    license="BSD-3-clause",
    platforms=["Any"],
    keywords="HDL PCB hardware design",
    classifiers=[
        "Topic :: Scientific/Engineering :: Electronic Design Automation (EDA)",
        "Environment :: Console",
        "Development Status :: Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
    ],
    packages=find_packages(),
    include_package_data=True,
    entry_points={
        # "console_scripts": [
        #     "pcbhdl=pcbhdl.cli:main",
        # ],
    },
    install_requires=["lxml"],
    tests_require=["lxml-asserts"]
)
