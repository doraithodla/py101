# getenv.py -- exploring a few os functions

import os

print os.getenv.__doc__
print

for var in  os.getenv('path').split(';'):
    print var


