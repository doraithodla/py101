# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Creating a Dictionary
# with Integer Keys
Dict = {1: 'HP', 2: 'compaq', 3: 'dell'}
print("\nDictionary with the use of Integer Keys: ")
print(Dict)

# Creating a Dictionary
# with Mixed keys
Dict = {'Name': 'HP', 1: [1, 2, 3, 4]}
print("\nDictionary with the use of Mixed Keys: ")
print(Dict)

# Creating a Dictionary
# with dict() method
Dict = dict({1: 'HP', 2: 'compaq', 3: 'dell'})
print("\nDictionary with the use of dict(): ")
print(Dict)

# Creating a Dictionary
# with each item as a Pair
Dict = dict([(1, 'HP'), (2, 'Dell')])
print("\nDictionary with each item as a pair: ")
print(Dict)

# Creating a Nested Dictionary
Dict = {1: {'A': 'dell', 'B': 'HP', 'C': 'asus'},
        2: {'D': 'HCl', 'E': 'lenovo', 'F': 'IBM'}}
print("\nNested Dictionary: ")
print(Dict)

# Creating an empty Dictionary
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# Adding elements one at a time
Dict[0] = 'HP'
Dict[2] = 'DELL'
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Adding set of values
# to a single Key
Dict['Value_set'] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)

# Updating existing Key's Value
Dict[2] = 'Welcome'
print("\nUpdated key value: ")
print(Dict)

# Adding Nested Key value to Dictionary
Dict[5] = {'Nested': {'1': 'Life', '2': 'Geeks'}}
print("\nAdding a Nested Key: ")
print(Dict)

# Initial Dictionary
Dict = {5: 'dell', 6: 'hp', 7: 'asus',
        'A': {1: 'something', 2: 'to', 3: 'do'},
        'B': {1: 'something', 2: 'else'}}
print("Initial Dictionary: ")
print(Dict)

# Deleting a Key value
del Dict[6]
print("\nDeleting a specific key: ")
print(Dict)

# Deleting a Key from
# Nested Dictionary
del Dict['A'][2]
print("\nDeleting a key from Nested Dictionary: ")
print(Dict)

# Deleting a Key
# using pop()
Dict.pop(5)
print("\nPopping specific element: ")
print(Dict)

# Deleting a Key
# using popitem()
Dict.popitem()
print("\nPops first element: ")
print(Dict)

# Deleting entire Dictionary
Dict.clear()
print("\nDeleting Entire Dictionary: ")
print(Dict)
