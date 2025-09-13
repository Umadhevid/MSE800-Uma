class Circle:
    def draw(self):
        return "Drawing a Circle"

class Square:
    def draw(self):
        return "Drawing a Square"

class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        if shape_type == "square":
            return Square()
        else:
            return None


factory = ShapeFactory()
shape = factory.create_shape("Triangle")   
print(shape.draw())  

#basically means your code tried to call .draw() on something that doesn’t exist. 
# In this case, when you asked the ShapeFactory to create a "triangle", 
# it didn’t know how to handle that request, so it returned None.
#  Then, the program tried to run shape.draw() — but since shape is actually None, 
# Python throws an error because None doesn’t have a draw() method.


# The problem here is we are writing logic for each shape in ShapeFactory. In future 
# if the shape is increased, the logic will be complicated and  every time we need to change the entire code
# To make the logic easy, we need to have factory method.
# Factory methods will have Abstract Base class. The child will inherit all the abstract methods from parent class.
# so whenever new functionality come, we can add those part logic wihtout changing the entire logic