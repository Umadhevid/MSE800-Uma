from Normal_DB import User_Serivce,Student_Serivce

class Check_Db:
    def __init__(self):
        self.self=self
    def timecheck(self):
        user_service=User_Serivce.search_user("Uma")
        print("f UserService user list {user_service}")
        stud_service=Student_Serivce.search_user("Dhevi")
        print("f UserService user list {user_service}")

if __init__=="__main__":
    Check_Db.timecheck()
