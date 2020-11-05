import sqlite3

class DataBaseWrapper:
    def __init__(self, path):
        self.connection = sqlite3.connect(path)
        self.cursor = self.connection.cursor()
        
        self._create_table()
    
    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS qiwi_accounts (
            number TEXT NOT NULL,
            token TEXT NOT NULL
        )""")
        self.connection.commit()
    
    def get_accounts(self):
        self.cursor.execute("SELECT * FROM qiwi_accounts")
        
        return self.cursor.fetchall()
    
    def add_account(self, number, token):
        self.cursor.execute("INSERT INTO qiwi_accounts VALUES (?, ?)", [number, token])
        self.connection.commit()
    
    def delete_account(self, number):
        self.cursor.execute("DELETE FROM qiwi_accounts WHERE number=?", [number])
        self.connection.commit()