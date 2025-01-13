# https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/#setup-py
# python3 setup.py --help-commands

import os
from codecs import open
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

os.chdir(here)

with open(
    os.path.join(here, "LONG_DESCRIPTION.rst"), "r", encoding="utf-8"
) as fp:
    long_description = fp.read()

version_contents = {}
with open(os.path.join(here, "duitku", "_version.py"), encoding="utf-8") as f:
    exec(f.read(), version_contents)

setup(
    name="duitku",
    version=version_contents["VERSION"],
    description="Python bindings for the Duitku API",
    long_description=long_description,
    long_description_content_type="text/x-rst",
    author="Duitku",
    author_email="support@duitku.com",
    url="https://github.com/duitku/duitku-python",
    license="MIT",
    keywords="duitku api payments",
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={"duitku": ["data/ca-certificates.crt", "py.typed"]},
    zip_safe=False,
    python_requires=">=3.13.1",
    project_urls={
        "Bug Tracker": "https://github.com/duitku/duitku-python/issues",
        "Changes": "https://github.com/duitku/duitku-python/blob/master/CHANGELOG.md",
        "Documentation": "https://duitku.com/docs/api/?lang=python",
        "Source Code": "https://github.com/duitku/duitku-python",
    },
)