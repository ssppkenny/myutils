from distutils.core import setup, Extension
import numpy 
import sys
from os import getenv

PLATFORM = sys.platform

if getenv('LIBLINK'):
    PLATFORM = 'android'

extension = Extension('utils', ['utils.c', 'pdf.m'], libraries=[], library_dirs=[], include_dirs=[numpy.get_include()], extra_compile_args=["-framework Foundation -framework CoreFoundation"])
setup(name="utils",
      version="0.0.6",
      ext_modules = [
        extension
    ]
)
