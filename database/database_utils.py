import sqlite3

# Function to connect to the SQLite database
def connect_to_database(database_name):
    try:
        conn = sqlite3.connect(database_name)
        print("Connected to SQLite database")
        return conn
    except sqlite3.Error as e:
        print("Error connecting to SQLite database:", e)
        return None

# Function to create tables in the database
def create_tables(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_name TEXT NOT NULL,
                appointment_date TEXT NOT NULL
            )
        ''')
        print("Tables created successfully")
    except sqlite3.Error as e:
        print("Error creating tables:", e)

# Function to insert a new appointment record into the database
def insert_appointment(conn, patient_name, appointment_date):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO appointments (patient_name, appointment_date) VALUES (?, ?)
        ''', (patient_name, appointment_date))
        conn.commit()
        print("Appointment record inserted successfully")
    except sqlite3.Error as e:
        print("Error inserting appointment record:", e)

# Function to retrieve appointments from the database
def get_appointments(conn):
    try:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM appointments')
        appointments = cursor.fetchall()
        return appointments
    except sqlite3.Error as e:
        print("Error retrieving appointments:", e)
        return None

# Additional functions for updating and deleting records can be added as needed
