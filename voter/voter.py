from db.db_election import Database


class Voter:
    def __init__(self, db_name):
        self.db = Database(db_name)

    def add_voter(self, username, password):
        self.db.cursor.execute('''INSERT INTO voter (username, password) VALUES (?, ?)''', (username, password))
        self.db.conn.commit()

    def cast_vote(self, voter_id, candidate_id):
        self.db.cursor.execute('''INSERT INTO votes (voter_id, candidate_id) VALUES (?, ?)''', (voter_id, candidate_id))
        self.db.cursor.execute('''UPDATE voters SET voted = 1 WHERE id = ?''', (voter_id,))
        self.db.conn.commit()

    def view_pool_results(self, constituency):
        # Code to view poll results
        self.db.cursor.execute('''select count(candidate_id) from votes;''')
        self.db.conn.commit()