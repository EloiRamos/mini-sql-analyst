import sqlite3

conn = sqlite3.connect('sample_data/sample.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name TEXT,
        email TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        amount REAL,
        date DATE,
        FOREIGN KEY(customer_id) REFERENCES customers(id)
    )
''')

# Insert sample data
cursor.execute("INSERT INTO customers (name, email) VALUES ('Alice', 'alice@example.com')")
cursor.execute("INSERT INTO customers (name, email) VALUES ('Bob', 'bob@example.com')")

cursor.execute("INSERT INTO orders (customer_id, amount, date) VALUES (1, 150.0, '2024-01-01')")
cursor.execute("INSERT INTO orders (customer_id, amount, date) VALUES (1, 200.0, '2024-02-01')")
cursor.execute("INSERT INTO orders (customer_id, amount, date) VALUES (2, 300.0, '2024-01-15')")

conn.commit()
conn.close()