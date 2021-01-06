# connect to the database named knowledge
# create a qa table 
import sqlite3

db_name = 'knowledge.db'
conn = sqlite3.connect(db_name)
cur = conn.cursor()
cur.execute('drop table if exists qa')
cur.execute('create table qa (question text, answer text)')
conn.close()