#!/usr/bin/env python

from distutils.core import setup

setup(name='SetupSample',
		version='1.0',
		description='Example',
		author='Tim Hsu',
		author_email='tim.yellow@gmail.com',
		url='https://www.python.org/sigs/distutils-sig/',
		py_modules = ['hi'],
		## below are some magic
		scripts=['cat2', ],
	 )
