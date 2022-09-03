from turtle import *
from random import randint

def moveto(x,y):
    penup()
    goto(x,y)
    pendown()

begin_poly()
for i in range(100):
    x = randint(1,100)
    y = randint(1,100)
    length = randint(10,100)
    angle = randint(1,90)
    right(angle)
    moveto(x,y)
    forward(length)
end_poly()
input()

