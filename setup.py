from setuptools import setup, find_packages

setup(
    name="rgrg",
    version="1.0",
    packages=find_packages(where="src"),
    package_dir={"src": "src"},
)
