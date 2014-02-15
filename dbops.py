# create qa database
# create a qa
import sqlite3
conn = sqlite3.connect('qa.db')
cur = conn.cursor()
cur.execute('drop table if exists qa')
cur.execute('create table qa (question text, answer text)')
conn.close()

