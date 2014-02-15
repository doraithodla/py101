# This program prints lines from a text file with line numbers

import sys

filename = sys.argv[1]

infile = open(filename)
count=0
for l in infile.readlines():
	count += 1
	print count,l 

print 'Total Number of lines: ', count


