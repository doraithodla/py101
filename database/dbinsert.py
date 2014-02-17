'''
 database insert 
 import sqlite module
 connect to the database
 create a cursor
 perform your database operations (select, insert,delete, update, create, drop)
 close the connection
'''


import sqlite3

conn = sqlite3.connect('knowledge.db')
cur = conn.cursor()

while True:
	question = raw_input("Question: ")
	if len(question) == 0:
		break
	else:
		answer = raw_input("Answer: ")
		cur.execute ('insert into qa (question, answer) values (?,?)',
			(question, answer))
		conn.commit()
	


'''
Add your database code here
'''

conn.close()



