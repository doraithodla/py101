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

db_name = 'knowledge.db' 
conn = sqlite3.connect(db_name)
cur = conn.cursor()

while True:
	question=input("Question : ")
	if len(question) > 0:
		answer = input("New Answer : ")
		cur.execute("select answer from qa where question = ?", [question])
		row = cur.fetchone()[0]
		print ("OLD VALUE : ", row)
		cur.execute("UPDATE qa SET answer=? WHERE question=?", (answer, question)) 
		conn.commit()
		cur.execute("select answer from qa where question = ?", [question])
		row = cur.fetchone()[0]
		print ("UPDATED VALUE : ", row)
	else:
		break


conn.close()



