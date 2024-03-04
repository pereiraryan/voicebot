import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('doctor_availability.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Create doctor availability table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS doctor_availability (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        doctor_name TEXT NOT NULL,
        day_of_week TEXT NOT NULL,
        time_slot TEXT NOT NULL
    )
''')

# Commit changes and close connection
conn.commit()
conn.close()
