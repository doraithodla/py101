#A simple list
from pprint import pprint

fruits = ['mango', 'banana', 'apple', 'orange']
for fruit in fruits:
    print fruit

# lists can be nested
eatables = [fruits, ['carrots','cabbage']]
pprint(eatables)

for items  in eatables:
    for item in items:
        print item
