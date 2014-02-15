import time

s=1

t1=time.time()
for i in range(100):
	s *= i+1
	print s

t2= time.time()
print 'it took', t2-t1

