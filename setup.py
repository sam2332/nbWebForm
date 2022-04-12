import setuptools
from setuptools.command.install import install
from subprocess import getoutput

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("LICENSE", "r") as fh:
    long_license = fh.read()



setuptools.setup(
    name="nbWebForm",
    version="0.01.1",
    scripts=["nbWebForm"],
    author="Sam Rudloff",
    author_email="sam.rudloff@gmail.com",
    description="Simple jupyter Notebook WebForm System",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sam2332/nbWebForm",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    License=long_license,
    install_requires=["argparse", "nbformat", "nbclient","nbparameterise",]
)
