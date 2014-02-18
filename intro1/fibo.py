#Create an array of the first two numbers in the Fibonacci series
# accept the range from command line
# usage:
# python fibo.py count

import sys
try:
	count = int(sys.argv[1])
except:
	count = 20

fs =[1,2] 

for n in range(count-2):
	# Except for the first two every number in the series is the sum of two previous numbers
	s = fs[n]+fs[n+1]

	# Add it to the series
	fs.append(s)

#print the series
for n in  fs:
	print n


