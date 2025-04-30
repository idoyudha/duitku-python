"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name="duitku",
    version="0.2.5",
    description="Duitku Python SDK",
    long_description=long_description,
    url="https://github.com/idoyudha/duitku-python",
    author="Ido Yudhatama",
    author_email="idowidya.yudhatama@gmail.com",
    keywords=["duitku", "duitku api", "duitku python"],
    packages=find_packages(include=["duitku*"], exclude=["tests", "tests.*"]),
    python_requires='>=3.5',
    install_requires=[
        "requests>=2.25.0",
    ],
)