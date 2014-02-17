# simple.py
# - a simple python

from turtle import *

def polygon(sides,step):
    for i in range(sides):
     forward(step)
     right(360/sides)

for i in range(30):
    right(95)
    polygon(4,100)