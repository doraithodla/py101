infile = open('test.txt')
count=0
for l in infile.readlines():
	count += 1
print 'Number of lines: ', count


