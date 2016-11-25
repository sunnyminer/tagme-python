'''
Setup for Tagme API Wrapper.
'''

import codecs
from os import path
from setuptools import setup

HERE = path.abspath(path.dirname(__file__))

with codecs.open(path.join(HERE, 'README.rst'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='tagme',
    version='0.1.2',
    description='Official TagMe API wrapper for Python',
    long_description=LONG_DESCRIPTION,
    url='https://github.com/marcocor/tagme-python',
    author='Marco Cornolti',
    author_email='cornolti@di.unipi.it',
    license='Apache',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
    ],

    keywords='entity-linking nlp tagme api',

    packages=['tagme'],

    install_requires=[
        'iso8601utils',
        'requests',
        'simplejson',
    ],

    extras_require={
        'test': [],
    },
)