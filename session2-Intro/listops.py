# listops.py
# - a simple python program to Append , Delete, Insert in a list

fruits = ["apple", "orange", "mango"]

# Iterating through the list

print fruits

# append some items
print "-- append banana and pineapple"
fruits.append("banana")
fruits.append("pineapple")

print fruits

# delete apple

fruits.remove('apple')
print fruits

fruits.insert(2,'strawberry')
print fruits
print
print "Number of items in fruits is: ", len(fruits)
print
# sort
fruits.sort()
print fruits
print
for item in fruits:
    print item


#reverse
fruits.reverse()
print fruits

