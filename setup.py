#!/usr/bin/env python
# -*- coding: utf-8 -*-
try:
    from setuptools import setup
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup

install_requires = [
#     'Django==1.5.8',
]

tests_require = [

]

setup(
    name='django-fieldsignals',
    version='1.0.0',
    description='django-fieldsignals.',
    author='.',
    author_email='example@aa.com',
    long_description=open('README.rst', 'r').read(),
    url='https://github.com/craigds/django-fieldsignals',
    packages=[
        'django-fieldsignals',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
    zip_safe=False,
    install_requires=install_requires,
    tests_require=tests_require,
)
