
"""Main module to check database services."""

from Normal_DB import User_Serivce, Student_Serivce


class CheckDb:
    """Class to check user and student services."""

    def __init__(self):
        pass  # No need for self.self

    def timecheck(self):
        """Check and print user and student service results."""
        user_service = User_Serivce.search_user("Uma")
        print(f"UserService user list: {user_service}")

        stud_service = Student_Serivce.search_user("Dhevi")
        print(f"StudentService user list: {stud_service}")


if __name__ == "__main__":
    checker = CheckDb()
    checker.timecheck()



