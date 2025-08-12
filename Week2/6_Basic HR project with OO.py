class Human_Resource:
    def __init__(self,name,salary,job_title):
        
        self.name=name
        self.salary=salary
        self.job_title=job_title

    def display_info(self):
        print("First Employee name: " ,self.name,": Employee Job Title: ",self.job_title," Employee Salary(NZD): ",self.salary)
        return
    def give_raise(self,new_salary):
        self.salary=self.salary+int(new_salary)
        print('Updated salary is :',self.salary)
        return

    def emp_cal():
            
        Employee1=Human_Resource("Uma",130000,"Technology Lead")
        Employee2=Human_Resource("Durai",230000,"Program Manager")
        Employee3=Human_Resource("Arjun",100000,"Software Engineer")
        while True:
            emp_no=input("Enter employee #:(Enter 1/2/3): ")
            if emp_no=='1':

                Employee1.display_info()
            elif emp_no=='2':
                
                Employee2.display_info()
            else:
                
                Employee3.display_info()
            con2=input("Want to increase the Employee salary? Enter Y or N:")
            if con2=='Y':
                sal_emp_no=input("Enter the employee # whom you want to increase the salary:(Enter 1/2/3):")
                new_amount=input("Enter the amount you want to increase")
                if sal_emp_no=='1':
                    

                    new_Sal=Employee1.give_raise(new_amount)
                    # print("Updated salary for Employee:", Employee1.salary)
                elif sal_emp_no=='2':
                
                    new_Sal=Employee2.give_raise(new_amount)
                    print("Updated salary for Employee:", new_Sal)
                else:
                
                    new_Sal=Employee3.give_raise(new_amount)
                    print("Updated salary for Employee:", new_Sal)

            con=input("Want to see other employee details: Enter Y or N:")
            if con=='Y':
                continue
            elif con=='N':
                print("Thanks for seeing the detials: Good Day")
                break
            
if __name__=='__main__':
    Human_Resource.emp_cal()


    