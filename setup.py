'''
this code helps in the setup of local packages to be used inside the project.
-e . looks for setup.py file and inside this file we add a setup() whcih then looks for constructor files within out repo
so that any folder with constructor files can be used as a local package
'''

from setuptools import setup, find_packages

setup( 
    name='visa_approval',
    version='0.0.0',
    author='ashutosh',
    author_email='ashutoshsinha519@gmail.com',
    packages=find_packages() # finds all the constructor files and use those as a local a create -n usvisa python package 
)