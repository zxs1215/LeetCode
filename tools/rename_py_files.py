import os
import re

"""
    I use the titile to name the py files,
    Such as "292 Nim Game.py" 

    when I run i in terminal as "python 292 Nim Game.py", 
    it errors!
    cause of the spaces.

    It's trouble me a lot .

    So I create this script to rename files,
    replace ' ' to '_' .
"""
os.chdir('..')

files = os.listdir('.')

pys = [f for f in files if re.match(r'^\d.*py$',f)]

for py in pys:
    py_r = py.replace(' ','_')
    if py_r != py:
        os.rename(py, py_r)

