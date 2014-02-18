# linecount.py - Counts line in a file
import sys
try:
	file = sys.argv[1]
except:
	file = r'..\data\test.txt'

infile = open(file)
count=0
for l in infile.readlines():
	count += 1
print 'Number of lines: ', count


