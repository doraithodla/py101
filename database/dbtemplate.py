'''
 database app template
 import sqlite module
 connect to the database
 create a cursor
 perform your database operations (select, insert,delete, update, create, drop)
 close the connection
'''
import sqlite3


db_name = 'knowledge.db'
conn = sqlite3.connect(db_name)
cur = conn.cursor()

'''
Add your database code here
'''

conn.close()



