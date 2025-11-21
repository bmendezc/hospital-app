from flask import g
import sqlite3
import os

# Set the database file name
DATABASE = 'app.db'

def get_db_connection():
    """
    Establishes a connection to the SQLite database ('app.db').
    It uses flask.g to store the connection, ensuring that only one connection 
    is used per request cycle (crucial for resource management in a web application).
    """
    if 'db' not in g:
        conn = sqlite3.connect(
            DATABASE,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        # Set row_factory to sqlite3.Row for dict-like access to column names
        conn.row_factory = sqlite3.Row
        g.db = conn
    return g.db

def init_db():
    """
    Initializes the database schema and inserts initial data by executing
    the SQL scripts ('create.sql' and 'insert_data.sql').
    """
    conn = None
    try:
        # NOTE: For standalone initialization (running 'python database.py'), 
        # we bypass flask.g and use a direct connection to allow running the script outside Flask's context.
        # However, for simplicity and integration, we'll use get_db_connection for consistency.
        conn = sqlite3.connect(
            DATABASE,
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        conn.row_factory = sqlite3.Row

        print(f"Initializing database schema from create.sql...")
        with open('create.sql') as f:
            conn.executescript(f.read())
            
        print(f"Inserting initial data from insert_data.sql...")
        with open('insert_data.sql') as f:
            conn.executescript(f.read())
            
        conn.commit()
        print("Database initialized and populated successfully.")
        
    except FileNotFoundError as e:
        print(f"Error: Required SQL file not found. Ensure '{e.filename}' exists in the current directory.")
        
    except sqlite3.Error as e:
        print(f"Database error during initialization: {e}")
        
    finally:
        if conn:
            conn.close()

def close_db(e=None):
    """
    Closes the database connection stored in flask.g at the end of a request.
    This function is called automatically by Flask's teardown process.
    """
    # Pop the 'db' connection from the request context's global (g) storage
    db = g.pop('db', None)
    if db is not None:
        db.close()

# Entry point for manual setup
if __name__ == '__main__':
    # Running 'python database.py' will execute this to set up 'app.db'
    init_db()