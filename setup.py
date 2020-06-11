import pathlib

from setuptools import setup, find_packages

import tutorial

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name=tutorial.__package_name__,
    version=tutorial.__version__,
    description="SQL Alchemy for Expression Language Tutorial",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/apecr/sqlalchemy-expression-language-tutorial",
    author="Alberto Eyo",
    author_email="alberto.eyo@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["sqlalchemy"]
)


