# Polymorphism (Method Overloading):
# One Method behave like other things in different files as we changed method and it is called method overloading .

class Shape:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__(radius, radius)
        
    def area(self):
        # return 3.14 * self.radius * self.radius
        return 3.14 * super().area()  # super call the parent class method that gives a and b and above we defined x, y in our constructor

# rec = Shape(3, 4)
# print(rec.area())

c = Circle(5)
print(c.area())