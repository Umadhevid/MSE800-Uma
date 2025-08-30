class Student:
    def __init__(self, name, age):
        self.name = name       # public
        self._age = age        # protected
        self.__grade = 'A'     # private

    def get_grade(self):
        return self.__grade
    def set_grade(self, grade):
        if isinstance(grade, str) and len(grade) > 0:
            self.__grade = grade
        else:
            print("Invalid Grade. It must be a non-empty string.")

    def student_details(self):
        print("Student detials",self.name,self._age,self.__grade)
class admin(Student):
    def __init(self,name,age):
        super().__init(self,name,age)
    def admin_student(self):
        print("Admin student", self.name)
        print("Admin student age", self._age)
        print("Admin student grade", self.get_grade())# unable to directly access to grade, since its private we can access via get_grade
    def updated_info(self):
        if self.get_grade()=='A':
            self.set_grade('A+')
            print("Uodated student grade is :",self.get_grade())
            


s = Student('Ali', 20)
print(s.name)         # accessible
print(s._age)         # discouraged
print(s.get_grade())  # correct way
s.student_details()
a=admin("Uma",22)
a.admin_student()
a.updated_info()