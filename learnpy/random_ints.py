'''
random_ints.py - generates 10 random numbers and stores it in a list
'''

from  random import randint

# Create a list (aka array) to hold the random numbers

list1 = []

for i in range(10):
    list1.append(randint(0, 100))
print(list1)
