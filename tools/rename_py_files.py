import os
import re

"""
    rename files  replace ' ' to '_' 
"""

files = os.listdir('..')

pys = [f for f in files if re.match(r'^\d.*py$',f)]

for py in pys:
    py_r = py.replace(' ','_')
    os.rename(py, py_r)

