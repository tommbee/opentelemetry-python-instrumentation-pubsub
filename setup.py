"""
Setuptools setup module
"""
from codecs import open
from os import path
from re import compile as re_compile

import toml
from setuptools import find_packages, setup

"""
NOTE: As of PEP-518 (https://www.python.org/dev/peps/pep-0518/)
and PEP-621 (https://www.python.org/dev/peps/pep-0621/)
setup.py is no longer the preferred way to build
and package python libraries. However, to avoid the duplication of information
in both pyproject.toml and setup.cfg, until setuptools reading from
pyproject.toml is supported (see: https://github.com/pypa/setuptools/issues/1688),
the information is pulled from pyproject.toml to use in here.
"""

HERE = path.abspath(path.dirname(__file__))

# Get the requirements from the requirements.txt
with open(path.join(HERE, 'pyproject.toml'), encoding='utf-8') as f:
    project_meta = toml.load(f)['project']

setup(
    name=project_meta['name'],
    description=project_meta['description'],
    author=[item['name'] for item in project_meta['authors'] if 'name' in item][0],
    author_email=[item['email'] for item in project_meta['authors'] if 'email' in item][
        0
    ],
    packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
    install_requires=project_meta['dependencies'],
    extras_require=project_meta['optional-dependencies'],
    python_requires=project_meta['requires-python'],
    classifiers=project_meta['classifiers'],
)
