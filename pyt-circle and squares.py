from turtle import *

def square():
    for i in range(4):
     forward(100)
     right(90)
def polygon(sides):
    for i in range(sides):
     forward(100)
     right(360/sides)

def triangle():
    for i in range(3):
        forward(100)
        right(120)

#square()
#triangle()


for i in range(20):
    right(95)
    polygon(4)


done()
