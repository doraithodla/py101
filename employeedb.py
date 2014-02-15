# simple.py
# - a simple python program
from employee import Person, Employee

dorai=Employee('Dorai Thodla','dorait@imorph.com','555-1212','CTO')
sue=Employee('Sue Campbell', 'sue@imorph.com', '575-1212','BizDev')

import shelve
db = shelve.open('persondb')                    # Filename where objects are stored
for object in (dorai, sue):                  # Use object's name attr as key
    db[object.name] = object                    # Store object on shelve by key
db.close()


