# func1.py
# Defining and using a python function
# This is a bad way to use a function (printing inside)
import sys

# define a function - def, function name, argument list

def hello(name):
    greeting =  "Hello "+name
    return greeting

# use a function
try:
	name = sys.argv[1]
except:
	name = "Dorai"

print hello(name)

