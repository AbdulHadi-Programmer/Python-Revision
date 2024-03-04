# Super Keyword:
# call the method or variable of parent class
# If my child class has same method name as above like parent_method then after calling from an object it call the 
# child class method and show that method and if we want to call the method of parent class that is parent_method then we can use super to call them
"""
class ParentClass:
    def parent_method(self):
        print("This is the parent method1")
        
class ChildClass(ParentClass):
    def parent_method(self):
        print("Harry2")
        super().parent_method()  # Call the above class method
        
    def child_method(self):
        print("This is a Child Method2")
        super().parent_method()  # In this, super inherit this method from above class
    
child_obj = ChildClass()
child_obj.child_method() # this print child and parent line in both function
child_obj.parent_method()  
"""

# New Example :
# Now we inherit Constructor var from one class to another class
class Employee:   # Super Class 
    def __init__(self, name, id):
        self.name = name 
        self.id = id
        
class Programmer(Employee):  # Sub Class
    def __init__(self, name, id, lang):
        super().__init__(name, id)  # now super inherit all var using constructor in this class
        self.lang = lang


rohan = Employee("Rohan Das", "420")
harry = Programmer("Harry", "100", "Python")

print(harry.name)
print(harry.id) 
print(harry.lang)