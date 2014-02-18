# Count the number of lines in a text file
# 1. Demonstrates opening, closing and reading lines from a file

file=open(r'..\data\test.txt')
count=0

for line in file.readlines():
    count+=1
file.close()

print "Count of lines in a file %d" % (count)

