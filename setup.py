#!/usr/bin/env python

from setuptools import setup

setup(name='magiclan2',
      version='0.0.1',
      description='MagicLan2 API interface',
      author='Mark Wadham',
      author_email='magiclan@rkw.io',
      url='https://github.com/m4rkw/magiclan',
      packages=['.'],
      setup_requires=['requests']
     )
