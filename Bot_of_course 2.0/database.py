import sqlite3 as sql

conn = sql.connect('rasp141.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS monday
    (
        first TEXT,
        second TEXT,
        third TEXT,
        fourth TEXT,
        fiveth TEXT
    );""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS tuesday
    (
        first TEXT,
        second TEXT,
        third TEXT,
        fourth TEXT,
        fiveth TEXT
    );""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS wednesday
    (
        first TEXT,
        second TEXT,
        third TEXT,
        fourth TEXT,
        fiveth TEXT
    );""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS thursday
    (
        first TEXT,
        second TEXT,
        third TEXT,
        fourth TEXT,
        fiveth TEXT
    );""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS friday
    (
        first TEXT,
        second TEXT,
        third TEXT,
        fourth TEXT,
        fiveth TEXT
    );""")
conn.commit()

cur.execute("""CREATE TABLE IF NOT EXISTS saturday
    (
        first TEXT,
        second TEXT,
        third TEXT,
        fourth TEXT,
        fiveth TEXT
    );""")
conn.commit()