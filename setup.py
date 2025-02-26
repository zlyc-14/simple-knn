# setup.py
from setuptools import setup, find_packages

setup(
    name="simple-knn",
    version="0.1.0",
    author="Your Name",
    description="A simple K-Nearest Neighbors implementation",
    packages=find_packages(),
    install_requires=["numpy>=1.20.0"],
    python_requires=">=3.7",
)
