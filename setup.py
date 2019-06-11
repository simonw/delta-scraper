from setuptools import setup, find_packages
import io
import os

VERSION = "0.1a1"


def get_long_description():
    with io.open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="delta-scraper",
    description="Python library for scraping data sources and creating readable deltas",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    version=VERSION,
    license="Apache License, Version 2.0",
    packages=find_packages(exclude="tests"),
    install_requires=["click", "requests", "github-contents"],
    setup_requires=["pytest-runner"],
    extras_require={"test": ["pytest", "black"]},
    entry_points="""
        [console_scripts]
        delta-scraper=delta_scraper.cli:cli
    """,
    tests_require=["delta-scraper[test]"],
    url="https://github.com/simonw/delta-scraper",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
    ],
)
