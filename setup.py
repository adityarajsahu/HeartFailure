import io
import os
from pathlib import Path

from setuptools import find_packages, setup

NAME = "HeartFailure"
DESCRIPTION = "Heart Failure Prediction"
URL = "https://github.com/adityarajsahu"
EMAIL = "adityaraj2019.sahu@gmail.com"
AUTHOR = "Adityaraj Sahu"
REQUIRES_PYTHON = ">=3.9.19"

pwd = os.path.abspath(os.path.dirname(__file__))

def list_reqs(fname = "requirements.txt"):
    with io.open(os.path.join(pwd, fname), encoding='utf-8') as file:
        return file.read().splitlines()
    
try:
    with io.open(os.path.join(pwd, 'README.md'), encoding='utf-8') as file:
        long_description = '\n' + file.read()
except FileNotFoundError:
    long_description = DESCRIPTION

ROOT_DIR = Path(__file__).resolve().parent
PACKAGE_DIR = ROOT_DIR / NAME
about = {}
with open(PACKAGE_DIR / 'VERSION') as file:
    _version = file.read().strip()
    about['__version__'] = _version

setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    python_requires=REQUIRES_PYTHON,
    url=URL,
    packages=find_packages(exclude=('tests',)),
    package_data={'HeartFailure': ['VERSION']},
    install_requires=list_reqs(),
    extras_require={},
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)