from database import create_connection
import sqlite3

def add_lecturer(first_name, last_name, dob, course_id=None):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO Lecturer (First_Name, Last_Name, Date_Of_Birth, Course_ID)
        VALUES ( ?, ?, ?, ?)
    ''', (first_name, last_name, dob, course_id))
    conn.commit()
    conn.close()
    print(" Lecturer added successfully.")

def view_lecturer():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Lecturer")
    rows = cursor.fetchall()
    conn.close()
    return rows

def search_lecturer(name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Lecturer WHERE First_Name LIKE ? OR Last_Name LIKE ?", 
                   ('%' + name + '%', '%' + name + '%'))
    rows = cursor.fetchall()
    conn.close()
    return rows

def delete_lecturer(lecturer_ID):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Lecturer WHERE Lecturer_ID = ?", (lecturer_ID,))
    conn.commit()
    conn.close()
    print(" Lecturer deleted successfully.")

