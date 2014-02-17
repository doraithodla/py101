# getenv.py -- exploring a few os functions

import os

print os.getenv.__doc__
for var in  os.getenv('path').split(';'):
    print var


