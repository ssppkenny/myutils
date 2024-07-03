from distutils.core import setup, Extension
import numpy 
import sys
from os import getenv

PLATFORM = sys.platform

if getenv('LIBLINK'):
    PLATFORM = 'android'

extension = Extension('utils', ['utils.c', 'pdf.c'], libraries=["pdfium"], library_dirs=["lib"], include_dirs=["include", numpy.get_include()])
setup(name="utils",
      version="0.0.9",
      ext_modules = [
        extension
    ]
)
