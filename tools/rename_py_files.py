import os
import re

"""
    rename files  replace ' ' to '_'  and replace '-' to '_'
"""
os.chdir('..')

files = os.listdir('.')

pys = [f for f in files if re.match(r'^\d.*py$',f)]

for py in pys:
    py_r = py.replace(' ','_').replace('-','_')
    if py_r != py:
        os.rename(py, py_r)

