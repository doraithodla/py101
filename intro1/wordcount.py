#countwords.py
# Opens a text file and prints a count of the number of words
import sys

try:
	file = sys.argv[1]
except:
	file = r"..\data\test.txt"

try:
	f=open(file)
except:
	print "File %s does not exist" % (file)
count=0

for line in f.readlines():
    line.split()
    a=len(line.split())
    count += a


print "File %s has %d words" % (file, count)
