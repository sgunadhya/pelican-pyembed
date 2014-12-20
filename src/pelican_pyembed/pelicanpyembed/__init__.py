'''
pelican-pyembed: Main module

Copyright 2014, Sushant Srivastava
Licensed under MIT.
'''

from pyembed.rst import PyEmbedRst

def register():
    PyEmbedRst().register()

