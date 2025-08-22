Project scope (short paragraph):

Write a  story that defines the purpose and scope of the database. Describe the main entities (e.g., students, lecturers, etc).
Yoobee college need to biuld the database for managing academic and administration data.
The database should have the all the details about the Schedules, students, lecturers, course detials, fee structure.
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

Attributes: Schedule_Id (PK), Course_Id (FK), Lecturer_Id (FK), Room_No, StartTime, EndTime.


Actors:
1.Student
2.Lecturer
3.Course
4.Fee
5.Schedules


Use Cases:
1. Student-> Register for the course in college
        ->View /edit personal detials
        ->view the schedules for the course/timetable
        ->check for the fee payment details
        -> make fee payment
2. Lecture-> Manage and access course content
        ->See the total students for the particular course
        ->correct the assignment
        -> view/modify schedules
3. Course-> provides courses avialable in the college
        ->provides no of students registered for which course
        -> Lecturer linked to the course
        -> schedules time table , class room and timing
4. Fee->Record payment
    -> calculate due amount
    ->Generate fee reports
    ->Link fee for course
5.Schedules-> create timetable
            -> manage conflicts
            -> access to student and lecture
            ->update schedule