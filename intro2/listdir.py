# defpath.py - default path

import sys
import os

try:
	dirpath = sys.argv[1]
except:
	dirpath = ".."

list = os.listdir(dirpath)
print 

for i in list:
    print i

