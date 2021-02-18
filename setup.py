# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in food_odering/__init__.py
from food_odering import __version__ as version

setup(
	name='food_odering',
	version=version,
	description='Simple Food Ordering Application',
	author='Sherin',
	author_email='sherinkrply@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
