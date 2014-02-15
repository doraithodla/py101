# dbread.py
# - read the records from the object db
import shelve


db = shelve.open('persondb')                  # Reopen the shelve

print len(db)                                       # Three 'records' stored

for key in db:                # Iterate, fetch, print
     print key,db[key]
