# ifelse.py
# - if then else statements

import sys
try:
	x = int(sys.argv[1])
except:
	x = 5

def oddoreven(x):
	if (x % 2):
    	    return 'odd'
	else:
	    return 'even'
def positiveornegative(x):
  if x < 0:
     return 'negative'
  else:
     return 'positive'

print '%d is ' % (x) + oddoreven(x)+' and ' +positiveornegative(x)

