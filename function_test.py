from query_class import Query
from file_handling import FileHandling

db = FileHandling("weekject.db")

db.initialise_weekjects("2007-03-31")



'''import sqlite3

con = sqlite3.connect("weekject.db")
cur = con.cursor()

cur.execute("PRAGMA table_info(weekject)")
print(cur.fetchall())

con.close()
'''