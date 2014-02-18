'''
filecount.py - count the files of a specific type in the current directory.
os module is a pretty powerful one and contains all kinds of cool stuff you
can play with. We will look at os.walk in this app

walk() generates the file names in a directory tree, by walking the tree either top down or bottom up. For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).
'''
import os, sys
count = 0

try:
	type = sys.argv[1]
except:
	type = '.py'


for (dirname, dirs, files) in os.walk('.'):
	for filename in files:
		if filename.endswith(type) :
			print filename
			count = count + 1

print 'There are %d %s files in this directory' % (count, type)

