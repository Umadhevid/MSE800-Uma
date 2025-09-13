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
shape = factory.create_shape("circle")   
print(shape.draw())  

#indicates that the program attempted to call the draw() method on a NoneType object.
#  This occurred because the ShapeFactory.create_shape("triangle") method returned None, as "triangle" is not a recognized shape type in the factory logic.
#  Consequently, the variable shape was assigned None, and invoking shape.draw() triggered the exception.