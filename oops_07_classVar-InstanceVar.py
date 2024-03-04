## Instance Variable  --> var that is create inside any method or constructor
# Method first find the instance var if it find then it gives and if it does not have then it search for class Var
# Instance variables are unique to each instance of a class. They are defined inside the constructor method (__init__) using the self keyword.
# They represent the attributes specific to each object created from the class.
# Instance variables can vary from one instance to another.

### Class Variable    --> var that is create outside the method and constructor
### And also remember, class var is only change for it particular object and it cannot change the original var value
### class var is bydefault same to all objects but we can also change it as per object
### class var is always associated with class var
# Class variables are shared among all instances of a class. They are defined within a class but outside of any method.
# They are often used to store attributes or properties that are common to all instances of the class.
# To define a class variable, you use the class name followed by the variable name like 'Company_name' and remember, it is made without 'self'.
# 
class Employee:
    companyName = "Ikea"  # this var is constant for all object of a class
    noOfEmployee = 0
    
    def __init__(self, name):
        # Instance Var
        self.name = name       # and every object have different value in this var
        self.raise_amount = 0.02  # and we also change it acc to our object
        Employee.noOfEmployee += 1
    def ShowDetail(self):
        print(f'The name of the Employee is {self.name} and the raise amount in {self.noOfEmployee} sized {self.companyName} is {self.raise_amount}')
        
emp1 = Employee("Harry")
# These are instance var and they can be easily changed 
emp1.raise_amount = 0.5 # We can also change this var value and also use getter setter
emp1.companyName = "Ikea Pakistan"  # And we can also change class Var
# Employee.ShowDetail(emp1)
emp1.ShowDetail()
print(emp1.companyName) # We can also access that var like that 
print(Employee.companyName) # and also like that

emp2 = Employee("Aman")
emp2.companyName = "Ikea Netherland"  # And we can also change class Var
emp2.ShowDetail()
print(emp2.companyName)
print(Employee.companyName) # and also like that

emp3 = Employee("Abdullah")
emp3.companyName = "Ikea Italy"  # And we can also change class Var
emp3.ShowDetail()
print(emp3.companyName)
print(Employee.companyName) # and also like that
