from setuptools import setup, find_packages

setup(
    name='BookLover package',
    version='1.0.0',
    url='https://github.com/rlipps/BookLover',
    author='Ryan Lipps',
    author_email='rhl8pk@virginia.edu',
    license = 'MIT',
    description='Package for hw09. Makes BookLover class :)',
    packages=find_packages(),
    install_requires=['pandas >= 1.5.3'], 
)