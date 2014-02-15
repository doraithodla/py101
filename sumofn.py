import sys

n=int(sys.argv[1])

i=1
sum=0
for j in range(n):
	sum += j+1
	#i += 1
print 'sum of', n, 'natural numbers is ', sum

