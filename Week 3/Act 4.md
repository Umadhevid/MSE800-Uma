Project scope (short paragraph):

Write a  story that defines the purpose and scope of the database. Describe the main entities (e.g., students, lecturers, etc).
Yoobee college need to biuld the database for managing academic and administration data.
The database should have the all the details about the administration, students, lecturers, course detials, fee structure.
The purpose of the database is to reduce redundancy,and provide accurate information.

Main Entities and Their Roles
1.   Student
Represents individuals enrolled at Yoobee College.

Attributes: Student_Id (PK), First_Name, Last_Name, Date_Of_Birth, Course_Id (FK), Lecturer_ID (FK)

2.Lecturer
Represents teaching staff responsible for delivering courses.

Attributes: Lecturer_ID (PK), Course_Id (FK), First_Name, Last_Name, Date_Of_Birth

3.Course
Represents academic courses offered by the college.

Attributes: Course_ID (PK), Course_Name, Credits, Department_ID

4. Fee
Represents academic fee details and due payments for each student.

Attributes: Fee_Id (PK), Course_Id (FK), Total_Fee, Due_Date

5.Schedules
Represents the timetable for classes conducted by lecturers for students.

Attributes: Schedule_Id (PK), Course_Id (FK), Lecturer_Id (FK), Room_No, StartTime, EndTime


Table Details:

Student (
    Student_ID      INT PRIMARY KEY,
    First_Name      VARCHAR(50),
    Last_Name       VARCHAR(50),
    Date_Of_Birth   DATE,
    Course_ID       INT,
    Lecturer_ID     INT,
    FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID),
    FOREIGN KEY (Lecturer_ID) REFERENCES Lecturer(Lecturer_ID)
);



Lecturer (
    Lecturer_ID     INT PRIMARY KEY,
    First_Name      VARCHAR(50),
    Last_Name       VARCHAR(50),
    Date_Of_Birth   DATE,
    Course_ID       INT,
    FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID)
);


Course (
    Course_ID       INT PRIMARY KEY,
    Course_Name     VARCHAR(100),
    Credits         INT,
    Department_ID   INT
);


Schedule (
    Schedule_ID     INT PRIMARY KEY,
    Course_ID       INT,
    Lecturer_ID     INT,
    Room_No         VARCHAR(10),
    StartTime       TIME,
    EndTime         TIME,
    FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID),
    FOREIGN KEY (Lecturer_ID) REFERENCES Lecturer(Lecturer_ID)
);


Fee (
    Fee_ID          INT PRIMARY KEY,
    Course_ID       INT,
    Total_Fee       DECIMAL(10,2),
    Due_Date        DATE,
    FOREIGN KEY (Course_ID) REFERENCES Course(Course_ID)
);




