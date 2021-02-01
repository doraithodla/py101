# dictionary - Various uses of dictionaries
# Creating a Dictionary

users = {'firstname': 'John', 'lastname': 'Smith', 'age': 27}

rain_percent = {1980: '17%', 1981: '15%', 1982: '10%'}
print(rain_percent)
print(rain_percent[1980])

# Specifying Key-Value Pairs
# You can also create and initialize a dictionary using name value pairs as keyword arguments to the dict() constructor.

population = dict(California=37253956, Colorado=5029196, Connecticut=3574097, Delaware=897934)
print(population)

# Accessing Python Dictionary Elements
print(population['Delaware'])

# Checking for Existence
print(1980 in rain_percent)
# Modifying Elements
# Change the value by assigning to the required key.
users = {'firstname': 'John', 'lastname': 'Smith', 'age': 27}
users['age'] = 29
print(users["age"])

# Deleting elements

users = {'firstname': 'John', 'lastname': 'Cena', 'age': 27}
del users['age']
print(users)

# Use the pop() method instead, when you want the deleted value back.
users = {'firstname': 'John', 'lastname': 'Cena', 'age': 27}
print(users.pop('age'))

# Looping With Python Dictionaries
users = {'firstname': 'John', 'lastname': 'Cena', 'age': 27}
for k in users:
    print(k, '=>', users[k])
