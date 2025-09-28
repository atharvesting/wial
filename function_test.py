from query_and_append import Query, Append
from file_handling import FileHandling
from tag_classes import TagRepository

tagdb = TagRepository("weekject.db")



'''

db.initialise_weekjects("2007-03-31")

print(db.query_obj.query_weekject_from_date("2025-09-09"))'''

'''import sqlite3

con = sqlite3.connect("weekject.db")
cur = con.cursor()

cur.execute("PRAGMA table_info(weekject)")
print(cur.fetchall())

con.close()
'''