import sqlite3
from misc import one_element_tuple_list_to_normal_list

class TagRepository:
    def __init__(self, weekject: str):
        self.con = sqlite3.connect(weekject)
        self.cur = self.con.cursor()
    
    def tag_existence_check(self, tag_name: str):
        query = "SELECT tag_name FROM tags WHERE tag_name = ?"
        return bool(self.cur.execute(query, (tag_name.lower(),)).fetchone())
        
    def query_tags_from_date(self, date:str) -> list:
        query = """
        SELECT week_tag.tag_id, tags.tag_name
        FROM week_tag
        INNER JOIN tags
        ON week_tag.tag_id = tags.tag_id
        """
        return self.cur.execute(query).fetchall()
    
    def query_all_tags(self) -> list:
        query = "SELECT tag_name FROM tags ORDER BY tag_name ASC"
        return self.cur.execute(query).fetchall()
    
    def add_tag_to_weekject(self, date:str, new_tags:list):
        for tag in new_tags:
            if self.tag_existence_check(tag):
                break
            