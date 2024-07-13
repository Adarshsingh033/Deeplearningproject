from setuptools import find_packages, setup

with open("requirements_dev.txt") as f:
    required = f.read().splitlines()

setup(
    name="Xray",
    version="0.0.1",
    author="Adarsh Singh",
    author_email="adarsharunsingh7@gmail.com",
    install_requires=required,
    packages=find_packages()
)
