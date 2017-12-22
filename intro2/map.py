# map.py - Demonstrate how map statement works
'''
map takes a function and a list and returns a new list by calling
the function with each element of the list in order.
In this case, the function simply multiplies each element by 2.
'''


def double(n):
    return n * 2


li = [1, 2, 3, 5, 9, 10, 256, 3]

# applies the function 'double' to all the elements of list
print(map(double, li))

# this is equivalent to the list iteration
print([double(n) for n in li])

# which can be done this way too
newlist = []
for n in li:
    newlist.append(double(n))
print(newlist)
