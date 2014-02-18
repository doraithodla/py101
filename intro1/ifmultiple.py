# multipleifthen.py
# - shows if..else-if 

import sys

x, y= int(sys.argv[1]), int(sys.argv[2]) 

if (x == y):
    print 'x(%d) is equal to y(%d)' % (x,y)
elif (x >= y):
    print 'x(%d) is greater than or equal y(%d)'  % (x,y)
elif (x <= y):
    print 'x(%d) is less than or equal to y(%d)'  % (x,y)


