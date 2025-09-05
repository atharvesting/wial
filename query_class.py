import sqlite3
import datetime

class Query:
    
    def __init__(self, weekject:str):
        self.con = sqlite3.connect(weekject)
        self.cur = self.con.cursor()
        
    def query_weekject_from_date(self, date:str):
        query = """
        SELECT * FROM weekject
        WHERE ? >= start_date AND ? <= end_date
        """
        self.cur.execute(query, (date, date))
        row = self.cur.fetchone()

        print(row)
        return row
    
    
class Append:
    
    def __init__(self, weekject):
        self.con = sqlite3.connect(weekject)
        self.cur = self.con.cursor()
    
    def add_tag(self, tag_list:list, weekject):
        '''for item in tag_list:
            self.cur.'''
            
        # first import the tags in a list, then check if new tag is already there, if not, then append to the column