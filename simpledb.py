# simpledb.py - a simple database app

import anydbm
db = anydbm.open('captions.db', 'c') #'c' create if it does not exist
db['Dorai'] = 'iMorph'
db['Sue'] = 'Any Inc.'

for key in db:
    print ("%s,%s") % (key, db[key])

db.close()