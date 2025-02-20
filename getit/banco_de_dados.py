import json
import sqlite3 as sql
con = sql.connect('db_web.db')

#Create a Connection
cur = con.cursor()

#Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS users")

#Create users table  in db_web database
sql ='''CREATE TABLE "users" (
    "UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
    "UNAME"	TEXT,
    "CONTACT"	TEXT
)
'''
cur.execute(sql)
cur.execute("DROP TABLE IF EXISTS texto")
sql = '''CREATE TABLE "texto" (
    "id"  INTEGER PRIMARY KEY AUTOINCREMENT,
    "titulo"  TEXT,
    "detalhes"  TEXT
    )
'''
cur.execute(sql)

#commit changes
con.commit()

#close the connection
con.close()

        