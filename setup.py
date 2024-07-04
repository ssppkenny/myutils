from distutils.core import setup, Extension
import numpy 
import sys
from os import getenv

PLATFORM = sys.platform

if getenv('LIBLINK'):
    PLATFORM = 'android'

library_dirs = ['lib/' + os.environ['ARCH']]

extension = Extension('utils', ['utils.c', 'pdf.c'], libraries=["pdfium"], library_dirs=library_dirs, include_dirs=["include", numpy.get_include()])
setup(name="utils",
      version="0.1.0",
      ext_modules = [
        extension
    ]
)
