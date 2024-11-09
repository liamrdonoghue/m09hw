from setuptools import setup

setup(
    name = 'BookLover',
    version = '0.1.0',
    author = 'Liam Donoghue',
    author_email = 'bat7kt@virginia.edu',
    packages = ['booklover', 'test'],
    license = 'LICENSE.txt',
    description = 'Makes a Book Lover object, and tests it',
    long_description = open('README.txt').read(),
    install_requires = [
        "pandas",
    ]
)