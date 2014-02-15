# filter.py - filter a list of items

list1= [1,2,3,4,5,6,7,9]
list2 = []
list3 = []

#Select odd numbers
def odd(x):
    return x % 2

# Conventional code
for i in list1:
    if odd(i):
        list2.append(i)
print "List2: ", list2

'''pythonic (using list iteration)
Loops through the list and calls odd with
each element. If odd returns a true value
(remember, any non?zero value is true in Python), then the
element is included in the returned list, otherwise
it is filtered out. The result is a list of only the odd
numbers from the original list, in the same order as they
appeared in the original.
'''
list3= [e for e in list1 if odd(e)]
print 'List3: ', list3

