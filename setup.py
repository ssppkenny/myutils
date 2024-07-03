from distutils.core import setup, Extension
import numpy 
import sys
from os import getenv

PLATFORM = sys.platform

if getenv('LIBLINK'):
    PLATFORM = 'android'


setup(name="utils",
      version="0.0.1",
      ext_modules = [
        Extension('utils', ['utils.c', 'pdf.m'], libraries=[], library_dirs=[], include_dirs=[numpy.get_include()])
    ]
)
