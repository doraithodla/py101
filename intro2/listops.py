# listops.py
# - a simple python program to Append , Delete, Insert in a list

fruits = ["apple", "orange", "mango"]

# Iterating through the list

print(fruits)

# append some items
print("\n-- append banana and pineapple")
fruits.append("banana")
fruits.append("pineapple")

print(fruits)

# delete apple

print("\n-- delete apple from the list")
fruits.remove('apple')
print(fruits)

print("\n-- insert strawberry into the list")
fruits.insert(2, 'strawberry')
print(fruits)
print()
print("\nNumber of items in fruits is: ", len(fruits))
print()
# sort
print("\nSort items in fruits ")
fruits.sort()
print(fruits)
print()
for item in fruits:
    print(item)

print("\nSort items in fruits in reverse")
# reverse
fruits.reverse()
print(fruits)
