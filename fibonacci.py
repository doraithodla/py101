#Create an array of the first two numbers in the Fibonacci series

fs =[1,2] 

for n in range(20):
	# Except for the first two every number in the series is the sum of two previous numbers
	s = fs[n]+fs[n+1]

	# Add it to the series
	fs.append(s)

#print the series
print fs

