class personal_details:
    def __init__(self,name,address, age):
        self.name=name
        self.address=address
        self.age=age
        
    def display(self):
        print(f"Display all detials",{self.name},{self.address},{self.age})
        return
if __name__=="__main__":
   p1= personal_details("Uma","Onehunga","33")
   p1.display()
