import sqlite3

def create_connection():
    conn = sqlite3.connect("YoobeeClg.db")
    return conn

def create_table():
    conn = create_connection()
    cursor = conn.cursor()
        # Student Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Student (
            Student_ID INTEGER PRIMARY KEY,
            First_Name TEXT NOT NULL,
            Last_Name TEXT NOT NULL,
            Date_Of_Birth TEXT,
            Course_ID INTEGER,
            Lecturer_ID INTEGER,
            FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID),
            FOREIGN KEY (Lecturer_ID) REFERENCES Lecturer(Lecturer_ID)
        )
    ''')
    
    # Lecturer Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Lecturer (
            Lecturer_ID INTEGER PRIMARY KEY,
            First_Name TEXT NOT NULL,
            Last_Name TEXT NOT NULL,
            Date_Of_Birth TEXT,
            Course_ID INTEGER,
            FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID)
        )
    ''')
    
    # Course Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Course (
            Course_ID INTEGER PRIMARY KEY,
            Course_Name TEXT NOT NULL,
            Credits INTEGER,
            Department_ID INTEGER
        )
    ''')
    
    # Schedule Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Schedule (
            Schedule_ID INTEGER PRIMARY KEY,
            Course_ID INTEGER,
            Lecturer_ID INTEGER,
            Room_No TEXT,
            StartTime TEXT,
            EndTime TEXT,
            FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID),
            FOREIGN KEY (Lecturer_ID) REFERENCES Lecturer(Lecturer_ID)
        )
    ''')
    
    # Fee Table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Fee (
            Fee_ID INTEGER PRIMARY KEY,
            Course_ID INTEGER,
            Total_Fee REAL,
            Due_Date TEXT,
            FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID)
        )
    ''')
    
    conn.commit()
    conn.close()
    
# Table Details:

# Student (
#     Student_ID      INT PRIMARY KEY,
#     First_Name      VARCHAR(50),
#     Last_Name       VARCHAR(50),
#     Date_Of_Birth   DATE,
#     Course_ID       INT,
#     Lecturer_ID     INT,
#     FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID),
#     FOREIGN KEY (Lecturer_ID) REFERENCES Lecturer(Lecturer_ID)
# );



# Lecturer (
#     Lecturer_ID     INT PRIMARY KEY,
#     First_Name      VARCHAR(50),
#     Last_Name       VARCHAR(50),
#     Date_Of_Birth   DATE,
#     Course_ID       INT,
#     FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID)
# );


# Course (
#     Course_ID       INT PRIMARY KEY,
#     Course_Name     VARCHAR(100),
#     Credits         INT,
#     Department_ID   INT
# );


# Schedule (
#     Schedule_ID     INT PRIMARY KEY,
#     Course_ID       INT,
#     Lecturer_ID     INT,
#     Room_No         VARCHAR(10),
#     StartTime       TIME,
#     EndTime         TIME,
#     FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID),
#     FOREIGN KEY (Lecturer_ID) REFERENCES Lecturer(Lecturer_ID)
# );


# Fee (
#     Fee_ID          INT PRIMARY KEY,
#     Course_ID       INT,
#     Total_Fee       DECIMAL(10,2),
#     Due_Date        DATE,
#     FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID)
# );
