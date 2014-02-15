# listiter.py - filtering lists
# [mapping?expression for element in source?list if filter?expression]

list=['this', 'is', 'a', 'test', 'for', 'list', 'iteration']

print list
list2= [i for i in list if len(i) > 3]
print list2