# modules.py
# - create a simple module

from turtle import *

def polygon(side, edgecount):
    " Draw a polygon at the current point"
    for i in range(edgecount):
        forward(side)
        right(360/edgecount)

if __name__ == '__main__':           # Only when run
    	print __name__

	polygon(50,4)                         # Not when imported

	done()
