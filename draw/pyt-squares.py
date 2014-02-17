# simple.py
# - a simple python program
import turtle

side =10
for i in range(10):
    side = side + 10
    for j in range(4):
            forward(side)
            left(90)
sleep(1)
done()