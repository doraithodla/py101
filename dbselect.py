'''
 import sqlite module
 connect to the database
 create a cursor
 select all the records and print them
 close the connection
'''


import sqlite3


conn = sqlite3.connect('knowledge.db')
cur = conn.cursor()

cur.execute('select question, answer from qa')
for row in cur:
	for field in row:
		# convert unicode data to ascii
		field.encode('ascii','ignore')
		print field,
	print



conn.close()



