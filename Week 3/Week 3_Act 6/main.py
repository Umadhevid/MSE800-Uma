from database import create_table
from student_manager import add_student,view_students,search_students,delete_students
from lecture_manager import add_lecturer,view_lecturer,search_lecturer,delete_lecturer


def main():

    create_table()
    while True:
        
        stu_choice=input("Enter 'a' to add student details /or enter '1' to enter lecture detials")
        if stu_choice=='a':
            first_name=input("Enter first name of student")
            last_name=input("Enter last name of student")
            dob=input("Enter dob in dd/mm/yyyy format")

            add_student(first_name, last_name, dob)
            print("student detial added successfully")
        stu_choice=input("Enter 'a' to add student details /or enter '1' to enter lecture detials")
        if stu_choice=='1':
            first_name=input("Enter first name of lecturer")
            last_name=input("Enter last name of lecturer")
            dob=input("Enter dob in dd/mm/yyyy format")

            add_lecturer(first_name, last_name, dob)
        input_choice=input("want to view the database of student and lecturer(Y?N)")
        if input_choice=='Y':
            users = view_students()
            for user in users:
                print(user)
            print("Student DB")
            users=view_lecturer()
            for user in users:
                print(user)
            print("Lecturer DB")
        delete_input=input("Want to delete any student or lecturer(s/l)")
        if delete_input=='s':
            user_id = int(input("Enter user ID to delete: "))
            delete_students(user_id)
            users = view_students()
            for user in users:
                print(user)
        if delete_input=='l':
            user_id=int(input("Enter Lecture ID to delete"))
            delete_lecturer(user_id)
            users=view_lecturer()
            for user in users:
                print(user)


        
    
        user_input=input("want to contine the process:Y/N")
        if user_input=='Y':
            continue
        else:
            break

if __name__=='__main__':
    main()