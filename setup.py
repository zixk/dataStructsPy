from distutils.core import setup
from setuptools import find_packages

requires = []

if __name__ == "__main__":
    setup(
        name="python_basics",
        version="0.0.1",
        packages=find_packages(),
        author='zixk',
        author_email='d.bladek@gmail.com',
        install_requires=requires,
        description='Python Basic Data Structures, Algorithms, etc.',
        include_package_data=True,
    )