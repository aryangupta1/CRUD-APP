import sqlite3


class Database:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, firstName text, lastName text, age int , occupation text)")
        self.conn.commit()

    def fetch(self):
        self.cur.execute('SELECT * FROM users')
        rows = self.cur.fetchall()
        return rows

    def insert(self, firstName, lastName, age, occupation):
        self.cur.execute("INSERT INTO users VALUES (NULL, ?, ?, ?, ?)", (firstName, lastName,
                                    age, occupation))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM users WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, firstName, lastName, age, occupation):
        self.cur.execute("UPDATE users SET firstName = ?, lastName = ?, age = ?, occupation = ? WHERE id = ?",
                         (firstName, lastName, age, occupation, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()

#db = Database('users.db')
#db.insert("Aryan", "Gupta", "18", "Student")
#db.insert("ANDY", "GUPTA")
