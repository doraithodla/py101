'''
random_ints.py - generates 10 random numbers and stores it in a list
'''

from  random import randint

# Create a list (aka array) to hold the random numbers

list1 = []

for i in range(10):
    list1.append(randint(0, 100))
print(list1)

'''
Practice Exercises:
1. Can you change the program to create 10 floating point numbers?
2. Can you explore the random module and list three functions that you may want to use?
3. Can you generate random numbers but store only odd numbers in the list?

