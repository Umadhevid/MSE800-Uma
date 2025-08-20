from database import create_table
from user_manager import add_user, view_users, search_user, delete_user
from student_manager import add_students,view_students,search_students,delete_students

def menu():
    print("\n==== User Manager ====")
    print("1. Add User")
    print("2. View All Users")
    print("3. Search User by Name")
    print("4. Delete User by ID")
    print("5. Exit")
def stumenu():
    print("\n==== Student Manager ====")
    print("a. Add Student")
    print("b. View All Students")
    print("c. Search Student by Name")
    print("d. Delete Student by ID")
    print("e. Exit")



def main():
    create_table()
    while True:
        menu()
        choice = input("Select an option (1-5): ")
        if choice == '1':
            name = input("Enter name: ")
            email = input("Enter email: ")
            add_user(name, email)
        elif choice == '2':
            users = view_users()
            for user in users:
                print(user)
        elif choice == '3':
            name = input("Enter name to search: ")
            users = search_user(name)
            for user in users:
                print(user)
        elif choice == '4':
            user_id = int(input("Enter user ID to delete: "))
            delete_user(user_id)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")
        stumenu()
        schoice=input("Select an option (a-e): ")
        if schoice == 'a':
            Stu_name = input("Enter name: ")
            Stu_address = input("Enter address: ")
            add_students(Stu_name, Stu_address)
        elif schoice == 'b':
            users = view_students()
            for stud in users:
                print(stud)
        elif schoice == 'c':
            name = input("Enter name to search: ")
            users = search_students(name)
            for user in users:
                print(user)
        elif schoice == 'd':
            user_id = int(input("Enter student ID to delete: "))
            delete_students(user_id)
        elif schoice == 'e':
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
