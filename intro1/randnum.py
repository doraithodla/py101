# random.py
# -  a few samples of random number generation

from random import *

print "10 random integers"
for i in range(10):
	print int(random()*i),
print
print

print "10 random numbers between 50 and 90"
for i in range(10):
	print randint(50,90),
print
print

print "10 random floating point numbers"
for i in range(10):
	print random()

