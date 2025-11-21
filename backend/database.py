from flask import g
import sqlite3
import os


DATABASE = 'app.db'

def get_db_connection():
 
    if 'db' not in g:
        conn = sqlite3.connect(
            DATABASE,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        
        conn.row_factory = sqlite3.Row
        g.db = conn
    return g.db

def init_db():
   
    conn = None
    try:
        
        conn = sqlite3.connect(
            DATABASE,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        conn.row_factory = sqlite3.Row

        print(f"Initializing database schema from create.sql")
        with open('create.sql') as f:
            conn.executescript(f.read())
            
        print(f"Inserting initial data from insert_data.sql")
        with open('insert_data.sql') as f:
            conn.executescript(f.read())
            
        conn.commit()
        print("Database initialized and populated successfully.")
        
    except FileNotFoundError as e:
        print(f"Error: Required SQL file not found. ")
        
    except sqlite3.Error as e:
        print(f"Database error during initialization: {e}")
        
    finally:
        if conn:
            conn.close()

def close_db(e=None):
   
    db = g.pop('db', None)
    if db is not None:
        db.close()


if __name__ == '__main__':
    
    init_db()