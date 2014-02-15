# functions.py
# - a simple python program to illustrate functions

# A function is defined using def, contains name and a list of arguments.
# A function returns a value using return

def sqr(x):
    return (x*x)

# A function is invoked using variables or literals
a=5
print sqr(a)
print sqr(-3)
print(sqr(sqr(3)))

"""
Functions are polymorphic
You can send different types of parameters to a function
"""

def times(a,b):
    print a*b
times (5,6)
times (2.2, 5)
times ([1,2,3], 3)