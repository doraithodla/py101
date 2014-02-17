# simple.py
# - a simple python

from turtle import *

def polygon(sides,step):
    for i in range(sides):
     forward(step)
     right(360/sides)

polygon(4,100)
