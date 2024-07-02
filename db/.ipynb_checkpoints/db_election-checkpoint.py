import sqlite3

class Database:
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()

    def create_tables(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS voters (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                birth_date TEXT NOT NULL,
                                constituency TEXT NOT NULL,
                                voted INTEGER DEFAULT 0
                            )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS parties (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL
                            )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS candidates (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL,
                                party_id INTEGER NOT NULL,
                                FOREIGN KEY (party_id) REFERENCES parties (id)
                            )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS constituencies (
                                id INTEGER PRIMARY KEY,
                                name TEXT NOT NULL
                            )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS votes (
                                voter_id INTEGER NOT NULL,
                                candidate_id INTEGER NOT NULL,
                                FOREIGN KEY (voter_id) REFERENCES voters (id),
                                FOREIGN KEY (candidate_id) REFERENCES candidates (id)
                            )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS admin (
                                id INTEGER PRIMARY KEY,
                                username TEXT NOT NULL,
                                password TEXT NOT NULL
                            )''')

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS voter (
                                id INTEGER PRIMARY KEY,
                                username TEXT NOT NULL,
                                password TEXT NOT NULL
                            )''')

        self.conn.commit()
        self.conn.close()
