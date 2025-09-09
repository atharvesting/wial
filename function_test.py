from query_class import Query
from file_handling import FileHandling

db = FileHandling("weekject.db")
db.add_tag_to_weekject("2025-09-09", ["coding", "quiz"])




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