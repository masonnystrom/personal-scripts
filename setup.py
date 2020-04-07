# setup.py file

# setup code for updating scripts
# python setup.py sdist bdist_wheel

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="personal-scripts-mason", # the name that you will install via pip
    version="1.2",
    author="Mason Nystrom",
    author_email="masonnystrom@gmail.com",
    description="A compilation of personal python scripts",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/masonnystrom/personal-scripts",
    #keywords="",
    packages=find_packages() # ["personal-scripts"]
)