import sqlite3
import os

class Storage:
    def __init__(self, db_path):
        os.makedirs(os.path.dirname(db_path), exist_ok=True)
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self._setup_tables()

    def _setup_tables(self):
        self.cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS messages(
                id INTEGER PRIMARY KEY,
                platform TEXT,
                user_id TEXT,
                message TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            """
        )
        self.conn.commit()

    def log_message(self, platform, user_id, message):
        self.cursor.execute(
            "INSERT INTO messages(platform, user_id, message) VALUES (?, ?, ?)",
            (platform, str(user_id), message),
        )
        self.conn.commit()
