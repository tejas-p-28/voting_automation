from db.db_election import Database

class Admin:
    def __init__(self, db_name):
        self.db = Database(db_name)

    def add_admin(self, username, password):
        self.db.cursor.execute('''INSERT INTO admin (username, password) VALUES (?, ?)''', (username, password))
        self.db.conn.commit()

    def create_voter(self, name, birth_date, constituency):
        self.db.cursor.execute('''INSERT INTO voters (name, birth_date, constituency) 
                                  VALUES (?, ?, ?)''', (name, birth_date, constituency))
        self.db.conn.commit()

    def add_party(self, party_name):
        self.db.cursor.execute('''INSERT INTO parties (name) VALUES (?)''', (party_name,))
        self.db.conn.commit()
        data = self.db.cursor.execute(f'''select id from parties where name = "{party_name}"''')
        party_id = data.fetchall()[0][0]
        print(f'Party Added with Part id : {party_id}')

    def add_candidate(self, candidate_name, party_id):
        self.db.cursor.execute('''INSERT INTO candidates (name, party_id) VALUES (?, ?)''', (candidate_name, party_id))
        self.db.conn.commit()

    def add_constituency(self, name):
        self.db.cursor.execute('''INSERT INTO constituencies (name) VALUES (?)''', (name,))
        self.db.conn.commit()

    def update_voter_info(self, voter_id, new_info):
        # Assuming new_info is a dictionary containing fields to update
        columns = ', '.join('{} = ?'.format(col) for col in new_info.keys())
        values = tuple(new_info.values())
        self.db.cursor.execute('''UPDATE voters SET {} WHERE id = ?'''.format(columns), values + (voter_id,))
        self.db.conn.commit()

    def start_election(self, constituency):
        # Code to start the election
        self.db.cursor.execute('''select count(name) from constituencies''')

    def view_pool_results(self, constituency):
        # Code to view poll results
        pass

