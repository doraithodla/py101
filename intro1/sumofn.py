# sumofn.py
# Calculates the sum of n natural numbers

import sys

n=int(sys.argv[1])

sum=0
for j in range(1,n+1):
	sum += j

print 'sum of', n, 'natural numbers is ', sum

