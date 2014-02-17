# getting an argument from command line
import sys

argcount = len(sys.argv)

for i in range(argcount):
	print "Argument %s is %s"%(i,sys.argv[i])
