import sqlite3
from datetime import datetime, timedelta
import os
from misc import calculate_age_given_birthdate_and_current_date
from query_class import Query

class FileHandling:

    def __init__(self, weekject: str):
        self.con = sqlite3.connect(weekject)
        self.cur = self.con.cursor()
        self.query_obj = Query(weekject)

    def initialise_tag_db(self):
        self.cur.executescript(""" 
            DROP TABLE IF EXISTS tags;
            CREATE TABLE tags (
                tag_id INTEGER PRIMARY KEY,
                tag_name TEXT
            );
        """)
        self.con.commit()

    def initialise_week_tag_db(self):
        self.cur.executescript("""
            DROP TABLE IF EXISTS week_tag;
            CREATE TABLE week_tag (
                week_no INTEGER,
                tag_id INTEGER,
                FOREIGN KEY (week_no) REFERENCES weekject(week_no),
                FOREIGN KEY (tag_id) REFERENCES tags(tag_id),
                PRIMARY KEY (week_no, tag_id)
            );
        """)
        self.con.commit()

    def initialise_weekjects(self, birth_date):
        self.birth_date = birth_date
        """
        Initialize the entire backend for the Weekject application.
        
        This does the following in one clean sweep:
        1. Drops any existing `weekject` table and recreates it.
        2. Pre-generates ~90 years (4680 weeks) of week entries starting from 2007-03-31.
        3. Creates a corresponding empty Markdown log file for each week inside the `logs/` folder.
        4. Stores the full path to each log file inside the database.
        """
        # --- Step 1: Reset the database ---
        self.cur.executescript("""
            DROP TABLE IF EXISTS weekject;
            CREATE TABLE weekject (
                week_no INTEGER PRIMARY KEY,
                start_date TEXT, end_date TEXT,
                age INTEGER, rating INTEGER, log_file TEXT
            );
        """)

        # --- Step 2: Prepare week data ---
        start_date = datetime.strptime(self.birth_date, "%Y-%m-%d")
        weeks_data = []

        current_date = start_date
        end_date = start_date + timedelta(days=6)

        # Ensure log directory exists
        os.makedirs("logs", exist_ok=True)

        for i in range(1, (90*52+1)):  # 90 years of weeks
            
            # Format dates as YYYY-MM-DD
            start_str = current_date.strftime("%Y-%m-%d")
            end_str = end_date.strftime("%Y-%m-%d")
            age = calculate_age_given_birthdate_and_current_date(self.birth_date, start_str)

            # Construct log file name
            file_name = f"logs/W{i:04d}_A{age:03d}_{start_str}.md"

            # Create the empty markdown file (only if it doesn’t already exist)
            if not os.path.exists(file_name):
                with open(file_name, "w") as log:
                    pass

            # Append week data including log file path
            weeks_data.append((i, start_str, end_str, age, 0, file_name))

            # Advance to the next week
            current_date += timedelta(days=7)    # add 7 days to the current date
            end_date += timedelta(days=7)        # add 7 days to the end date

        # --- Step 3: Bulk insert into database ---
        print("Inserting data into the database...")
        self.cur.executemany(
            "INSERT INTO weekject (week_no, start_date, end_date, age, rating, log_file) VALUES (?, ?, ?, ?, ?, ?)",
            weeks_data
        )

        self.initialise_tag_db()
        self.initialise_week_tag_db()
        print("Databases and log files successfully initialized!")

        self.con.commit()
    

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
