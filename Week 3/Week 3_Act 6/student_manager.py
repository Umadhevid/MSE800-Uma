from database import create_connection
import sqlite3

def add_student(first_name, last_name, dob, course_id=None, lecturer_id=None):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO students (First_Name, Last_Name, Date_Of_Birth, Course_ID, Lecturer_ID)
        VALUES (?, ?, ?, ?, ?)
    ''', (first_name, last_name, dob, course_id, lecturer_id))
    conn.commit()
    conn.close()
    print("✅ Student added successfully.")

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
    cursor.execute("SELECT * FROM students WHERE First_Name LIKE ? OR Last_Name LIKE ?", 
                   ('%' + name + '%', '%' + name + '%'))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_students(student_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM students WHERE Student_ID = ?", (student_id,))
    conn.commit()
    conn.close()
    print("🗑️ Student deleted successfully.")


