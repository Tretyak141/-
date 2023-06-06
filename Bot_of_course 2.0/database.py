import sqlite3 as sql

conn = sql.connect('students.db')
cur = conn.cursor()
cur.execute("SELECT * FROM students_base;")
cur.execute("DELETE FROM students_base;")
conn.commit()
conn.close()