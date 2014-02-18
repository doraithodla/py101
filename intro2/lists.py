'''
lists.py -- A small taste of lists 
'''

fruits = ['mango', 'banana', 'apple', 'orange']
print "\n\nList of fruits\n\n"
for fruit in fruits:
    print fruit

# lists can be nested
print "\n\nList of fruits and vegetables\n\n"
eatables = [fruits, ['carrots','cabbage']]

for items  in eatables:
    for item in items:
        print item
