import sqlite3
import datetime
from misc import one_element_tuple_list_to_normal_list, check_rating_validity

class Query:
    
    def __init__(self, weekject:str):
        self.con = sqlite3.connect(weekject)
        self.cur = self.con.cursor()
        
    def query_weekject_from_date(self, date:str)  -> tuple:
        query = """
        SELECT * FROM weekject
        WHERE start_date <= ? AND end_date >= ?
        """
        self.cur.execute(query, (date, date))
        row = self.cur.fetchone()

        return row
    
    '''def query_tags_from_date(self, date:str) -> list:
        query = """
        SELECT week_tag.tag_id, tags.tag_name
        FROM week_tag
        INNER JOIN tags
        ON week_tag.tag_id = tags.tag_id
        """ 
        
        return self.cur.execute(query).fetchall()'''
    
    '''def query_all_tags(self) -> list:
        query = """
        SELECT tag_name FROM tags
        ORDER BY tag_name ASC
        """

        return one_element_tuple_list_to_normal_list(self.cur.execute(query).fetchall())'''

    def query_rating_from_date(self, date: str) -> list:
        week_no = self.query_weekject_from_date(date)[0]
        query = """
        SELECT rating FROM weekject
        WHERE week_no = ?
        """
        return self.cur.execute(query, (week_no,)).fetchone()
        

class Append:
    
    def __init__(self, weekject):
        self.con = sqlite3.connect(weekject)
        self.cur = self.con.cursor()
        self.query_obj = Query("weekject.db")
            
    def add_tag_to_weekject(self, date:str, new_tags:list):
        week_no = self.query_obj.query_weekject_from_date(date)[0]
        for tag in new_tags:
            tag = tag.lower()
            row = self.cur.execute("SELECT * FROM tags WHERE tag_name = ?", (tag,)).fetchone()
            if row:
                week_tag_check = self.cur.execute(
                    "SELECT * FROM week_tag WHERE week_no = ? AND tag_id = ?",
                    (week_no, row[0])).fetchone()
                if week_tag_check:
                    print(f"Tag #{tag} already applied to this weekject.")
                else:
                    self.cur.execute("INSERT INTO week_tag (week_no, tag_id) VALUES (?, ?)", (week_no, row[0]))
                    print("Tag(s) added successfully")
                    
            else:
                self.cur.execute("INSERT INTO tags(tag_name) VALUES (?)", (tag,))
                tag_id = self.cur.lastrowid
                self.cur.execute("INSERT INTO week_tag(week_no, tag_id) VALUES (?, ?)", (week_no, tag_id))
                print("Tag was not there in the database. Successfully added to tag and week_tag DB.")    
        
        self.con.commit()
            
    def set_rating(self, date, rating:int):
        if not check_rating_validity(rating):
            print("Invalid rating. Choose integer between -2 and 2 inclusive.")
            return
        
        current_rating = self.query_obj.query_rating_from_date(date)
        print(f"Current rating: {current_rating}")
        confirmation = input("Change rating? (Y/n) ").lower()
        if confirmation in ("y", "yes"):
            week_no = self.query_obj.query_weekject_from_date(date)[1]
            query = """
            UPDATE weekject SET rating = ? WHERE week_no = ?
            """
            self.cur.execute(query, (rating, week_no))
            print(f"Rating successfully changed to {rating}")
        else:
            print(f"No changes made. Rating remains {current_rating}")