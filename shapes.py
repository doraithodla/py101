from turtle import forward, right

def shape(sides,length):
    for i in range(sides):
        forward(length)
        right(360/sides)
'''
length = int(input("Length: "))
sides = int(input("Number of sides:"))
'''
for sides in range(3,5):
    shape(sides, 100)
    

