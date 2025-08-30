from oop import personal_details

class Students(personal_details):
    def __init__(self,name,address,age,Stu_ID):
        super().__init__(name,address,age)
        self.Stu_ID=Stu_ID
        
    def display_Students(self):
        return print("Display students details :",self.name,self.address,self.age,self.Stu_ID)
    

class Academics(personal_details):
    def __init__(self,name,address,age,tax_code,Salary):
        super().__init__(name,address,age)
        self.tax_code=tax_code
        self.Salary=Salary
    def display_Academics(self):
        return print("Display Academics details :",self.name,self.address,self.age,self.tax_code,self.Salary)

if __name__=="__main__":
    s1=Students("Uma","Onehunga","33","123")
    A1=Academics("Uma","Onehunga","33","M","100000NZD")
    s1.display_Students()
    A1.display_Academics()
