#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

#with open('README.rst') as readme_file:
#    readme = readme_file.read()

#with open('HISTORY.rst') as history_file:
#    history = history_file.read()

requirements = [
    'Click>=6.0',
]

test_requirements = [
]

setup(
    name='SIR',
    description="SIR is an interface designed for the SIR model course plan of Girls Talk Math Camp at UNC Chapel Hill",
#    long_description=readme + '\n\n' + history,
    author="Maggie P Cai",
    packages=find_packages(),
    package_dir={'SIR':
                 'SIR'},
    py_modules=['SIR'],
    entry_points={
        'console_scripts': [
            'SIR=SIR:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='SIR',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
