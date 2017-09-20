from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='SimpleLogger',
    version='0.1.0',
    description='A Simple Logger',
    long_description=readme,
    author='Felix Scheja',
    author_email='Felix.Scheja@outlook.de',
    url='https://github.com/FancyChaos/SimpleLogger',
    license=license,
    packages=['SimpleLogger']
)