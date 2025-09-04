from oop import personal_details

class Students(personal_details):
    def __init__(self,name,address,age,Stu_ID):
        super().__init__(name,address,age)
        self.Stu_ID=Stu_ID
        
    def display_Students(self):
        super().display()
        return print("Display students ID :",self.Stu_ID)
    

class Academics(personal_details):
    def __init__(self,name,address,age,tax_code,Salary):
        super().__init__(name,address,age)
        self.tax_code=tax_code
        self.Salary=Salary
    def display_Academics(self):
        super().display()
        return print("Display Academics Tax code and salary :",self.tax_code,self.Salary)
class Generalstaff(personal_details):
    def __init__(self,name,address,age,tax_code,payrate):
        super().__init__(name,address,age)
        self.tax_code=tax_code
        self.payrate=payrate
    def display_GeneralStaff(self):
        super().display()
        return print("Display General staff Tax code and payrate :",self.tax_code,self.payrate)


if __name__=="__main__":
    s1=Students("Uma","Onehunga","33","123")
    A1=Academics("Dhevi","Epsom","39","M","100000NZD")
    G1=Generalstaff("Arjun","Epsom","49","S","100NZD/PH")
    s1.display_Students()

    A1.display_Academics()
    G1.display_GeneralStaff()
