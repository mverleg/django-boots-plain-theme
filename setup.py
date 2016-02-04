# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst', 'r') as fh:
	readme = fh.read()

setup(
	name='django_avem_theme',  # should have used a - sorry
	description='Simple bootstrap3 theme for Django',
	long_description=readme,
	url='https://github.com/mverleg/django_avem_theme',
	author='Mark V',
	maintainer='(the author)',
	author_email='mdilligaf@gmail.com',
	license='Revised BSD License (LICENSE.txt)',
	keywords=['django', 'bootstrap'],
	version='1.1',
	packages=['avem_theme'],
	include_package_data=True,
	zip_safe=False,
	classifiers=[
		'Development Status :: 5 - Production/Stable',
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'License :: OSI Approved :: BSD License',
		'Operating System :: OS Independent',
		'Programming Language :: Python',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.4',
		'Programming Language :: Python :: 3.5',
		'Programming Language :: Python :: Implementation :: PyPy',
		'Topic :: Software Development :: Libraries :: Python Modules',
	],
	install_requires=[
		'django',
		#'beautifulsoup4',
	],
)


