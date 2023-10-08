from setuptools import find_packages, setup
import os
import sys
import platform

if sys.argv[-1] == 'publish':
  if platform.system() == 'Windows':
    os.system('python setup.py bdist_wheel sdist')
    os.system('twine check dist/*')
    os.system('twine upload dist/*')
    sys.exit()

with open('README.md', 'r') as f:
  long_description = f.read()

setup(
  name='pyhwid',
  version='0.0.1',
  description='HWID generator for Windows & MacOS',
  packages=find_packages(),
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/aaronlyy/pyhwid',
  author='Aaron Levi (aaronlyy) Can',
  author_email='aaronlevican@gmail.com',
  license='MIT',
  classifiers=[
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12'
  ],
  extra_requires={
    'dev': ['twine']
  },
  python_requires='>=3.6'
)