# create a database called kb (for knowledge base)
# create a qa

import sqlite3

conn = sqlite3.connect('knowledge.db')
cur = conn.cursor()
cur.execute('drop table if exists qa')
cur.execute('create table qa (question text, answer text)')
conn.close()



