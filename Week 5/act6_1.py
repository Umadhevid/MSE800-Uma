class Student:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected
        self.__grade = 'A'     # private

    def get_grade(self):
        return self.__grade
    def student_details(self):
        print("Student detials",self.name,self._age,self.__grade)
class admin(Student):
    def __init(self,name,age):
        super().__init(self,name,age)
    def admin_student(self):
        print("Admin student", self.name)
        print("Admin student age", self._age)
        print("Admin student grade", self.get_grade())


s = Student('Ali', 20)
print(s.name)         # accessible
print(s._age)         # discouraged
print(s.get_grade())  # correct way
s.student_details()
a=admin("Uma",22)
a.admin_student()