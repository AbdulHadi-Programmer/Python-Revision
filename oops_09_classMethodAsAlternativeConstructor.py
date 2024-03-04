# Class Method as Alternative Constructor:
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    
    @classmethod
    def fromStr(cls, string):
        return cls(string.split("-")[0], string.split("-")[1])
    # We can also make multiple class method to handle different types of methods
    @classmethod
    def commasStr(cls, string):
        return cls(string.split(",")[0], string.split(",")[1])
    
    @classmethod
    def dotStr(cls, string):
        return cls(string.split(".")[0], string.split(".")[1])
    
    
e1 = Employee("Abdul Hadi", 5000)
print(e1.name)
print(e1.salary)

String = "Harry-12000" # now if data is given in this format then we can use this, but this will confused us
# e2 = Employee(string.split("-")[0], string.split("-")[1]) # Instead of Writing this:
print('Hyphen Separated Value (-)')
e2 = Employee.fromStr(String)
print(e2.name)
print(e2.salary)

e3 = Employee("Abdullah", 13000)
String = "Harry,12000" # now if data is given in this format then we can use this, but this will confused us
print('Commas Separated Value (,)')
e3 = Employee.commasStr(String)
print(e2.name)
print(e2.salary)

e4 = Employee("Abcdefg", 4500)
String = "Harry.12000" # now if data is given in this format then we can use this, but this will confused us
print('Dot Separated Value (.)')
e3 = Employee.dotStr(String)
print(e2.name)
print(e2.salary)