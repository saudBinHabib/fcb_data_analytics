import os
from runpy import run_path

from setuptools import find_packages, setup

# read the program version from version.py (without loading the module)
__version__ = run_path("src/fcb_data_providers/version.py")["__version__"]


def read(fname):
    """Utility function to read the README file."""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_prod_requirements():
    """Read all the prod requirements from the requirements directory."""
    requirements = []
    requirements_dir = os.path.join(os.path.dirname(__file__), "requirements")
    prod_requirements_file = os.path.join(requirements_dir, "prod.txt")

    if os.path.isfile(prod_requirements_file):
        with open(prod_requirements_file, "r") as f:
            requirements = f.read().splitlines()

    return requirements


setup(
    name="fcb_data_providers",
    version=__version__,
    author="Saud Bin Habib",
    author_email="saud.habib@alexanderthamm.com",
    description="This is a python package to handle the data providers for the scouting models",  # noqa
    url="",
    packages=find_packages("src"),
    package_dir={"": "src"},
    package_data={"fcb_data_providers": ["res/*"]},
    long_description=read("README.md"),
    install_requires=get_prod_requirements(),
    tests_require=[
        "pytest",
        "pytest-cov",
        "pre-commit",
    ],
    platforms="any",
    python_requires=">=3.11",
)
