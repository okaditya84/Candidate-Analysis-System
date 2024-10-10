import sqlite3
from flask import g

DATABASE = 'candidate_analysis.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
    return db

def init_db():
    with sqlite3.connect(DATABASE) as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS analyses
            (id INTEGER PRIMARY KEY AUTOINCREMENT,
             type TEXT NOT NULL,
             result TEXT NOT NULL,
             timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)
        ''')

def close_db(e=None):
    db = g.pop('_database', None)
    if db is not None:
        db.close()