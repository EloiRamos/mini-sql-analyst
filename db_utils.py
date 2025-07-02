import sqlite3

def get_connection():
    """Returns a connection to the SQLite database."""
    return sqlite3.connect('sample_data/sample.db')

def execute_query(query):
    """Executes a SQL query and returns all results."""
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        results = cursor.fetchall()
        conn.close()
        return results
    except Exception as e:
        return {"error": str(e)}