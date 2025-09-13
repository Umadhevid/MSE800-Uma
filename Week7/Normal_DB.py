import sqlite3
import time

DB_NAME = "users.db"

# ---------------------------
# Database Connection & Setup
# ---------------------------
def create_connection():
    conn = sqlite3.connect(DB_NAME)
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()

    # Users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')

    # Students table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            Stu_ID INTEGER PRIMARY KEY AUTOINCREMENT,
            Stu_name TEXT NOT NULL,
            Stu_address TEXT NOT NULL UNIQUE
        )
    ''')

    conn.commit()
    conn.close()

# ---------------------------
# CRUD Functions
# ---------------------------
def add_student(stu_name, stu_address):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO students (Stu_name, Stu_address) VALUES (?, ?)", 
                   (stu_name, stu_address))
    conn.commit()
    conn.close()
    print("Student added successfully.")

def search_students(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE Stu_name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def add_user(name, email):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        conn.commit()
        print(" User added successfully.")
    except sqlite3.IntegrityError:
        print(" Email must be unique.")
    conn.close()

def search_user(name):
    conn = create_connection()
    cursor = conn.cursor()

    start_time = time.process_time()   # start measuring here
    cursor.execute("SELECT * FROM users WHERE name LIKE ?", ('%' + name + '%',))
    rows = cursor.fetchall()
    end_time = time.process_time()     # end measuring here

    conn.close()
    print(f"Time taken to fetch user data: {end_time - start_time:.6f} seconds")
    return rows

# ---------------------------
# Main Program
# ---------------------------
def main():
    create_table()

    # Insert test data
    add_student("Uma111", "NZ111")
    add_user("Dhevi111", "dhevi111@example.com")

    start_time = time.process_time()

    # Search for user
    user = search_user("Dhevi")
    print("User Details:", user)

    end_time = time.process_time()

    # Search for student
    student = search_students("Uma")
    print("Student Details:", student)

   
    print(f"Execution time: {end_time - start_time:.20f} seconds")

if __name__ == "__main__":
    main()
