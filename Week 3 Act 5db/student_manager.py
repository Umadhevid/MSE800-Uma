from database import create_connection
import sqlite3

def add_students(Stu_name, Stu_address):
    conn = create_connection()
    cursor = conn.cursor()
   
    cursor.execute("INSERT INTO students (Stu_name, Stu_address) VALUES (?, ?)", (Stu_name, Stu_address))
    conn.commit()
    print(" Student added successfully.")
    
    conn.close()

def view_students():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_students(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students WHERE name LIKE ?", ('%' + Stu_name + '%',))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_students(user_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE id = ?", (Stu_ID,))
    conn.commit()
    conn.close()
    print("🗑️ students deleted.")
# Please add a new table named "Students" with 
# three columns: Stu_ID, Stu_name, and Stu_address.
#  Insert two sample records into Students, then display all rows from both the Users and Students tables.