from setuptools import setup

setup()

# from codecs import open
# from os import path
# from re import compile as re_compile
# from setuptools import find_packages, setup
#
#
# HERE = path.abspath(path.dirname(__file__))
#
# # Get the requirements from the requirements.txt
# with open(path.join(HERE, 'pyproject.toml'), encoding='utf-8') as f:
#     project_meta = toml.load(f)['project']
#
# setup(
#     name=project_meta['name'],
#     description=project_meta['description'],
#     url=project_meta['urls']['repository'],
#     author=[item['name'] for item in project_meta['authors'] if 'name' in item][0],
#     author_email=[item['email'] for item in project_meta['authors'] if 'email' in item][
#         0
#     ],
#     packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
#     install_requires=project_meta['dependencies'],
#     extras_require=project_meta['optional-dependencies'],
#     python_requires=project_meta['requires-python'],
#     classifiers=project_meta['classifiers'],
# )
