'''
 dbupdate.py - update a selected record
 database app template
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
	question=raw_input("Question : ")
	answer = raw_input("New Answer : ")
	if len(question) > 0:
		#statement = "select question, answer from qa where question = '"+question+"'"
		cur.execute("select answer from qa where question = ?", [question])
		row = cur.fetchone()
		print row
		cur.execute("UPDATE qa SET answer=? WHERE question=?", (answer, question)) 
		conn.commit()
		break
		
	else:
		break


conn.close()



