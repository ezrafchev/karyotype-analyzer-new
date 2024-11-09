
import sqlite3
import json
from datetime import datetime

class Database:
    def __init__(self, db_file='karyotype_analysis.db'):
        self.db_file = db_file
        self.conn = None
        self.create_table()

    def connect(self):
        self.conn = sqlite3.connect(self.db_file)
        return self.conn.cursor()

    def close(self):
        if self.conn:
            self.conn.close()

    def create_table(self):
        cursor = self.connect()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS analysis_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            image_path TEXT,
            chromosome_count INTEGER,
            analysis_result TEXT,
            timestamp DATETIME
        )
        ''')
        self.conn.commit()
        self.close()

    def insert_result(self, image_path, chromosome_count, analysis_result):
        cursor = self.connect()
        timestamp = datetime.now().isoformat()
        cursor.execute('''
        INSERT INTO analysis_results (image_path, chromosome_count, analysis_result, timestamp)
        VALUES (?, ?, ?, ?)
        ''', (image_path, chromosome_count, analysis_result, timestamp))
        self.conn.commit()
        self.close()

    def get_all_results(self):
        cursor = self.connect()
        cursor.execute('SELECT * FROM analysis_results ORDER BY timestamp DESC')
        results = cursor.fetchall()
        self.close()
        return results

if __name__ == "__main__":
    # Test the database functions
    db = Database()
    db.insert_result("test_image.jpg", 46, "Normal")
    results = db.get_all_results()
    print("Test results:", results)
