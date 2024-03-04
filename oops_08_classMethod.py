# Class method is used to change class var 
# 1) Accessing or Modifying Class Variables:
# Class methods are often used when you need to access or modify class-level variables. Since they have access to the class itself (cls), they can work with class variables without needing an instance.
# They are defined using the @classmethod decorator.
# Class methods have access to the class itself as their first parameter, often named cls.

class Employee:
    company = "Apple"
    def show(self):
        print(f'The name is {self.name} and Company is {self.company}')
    
    @classmethod
    def changeCompany(cls, newCompany): # cls take class as an argument not an instance all other method which take instance as argument
        cls.company = newCompany
        
        
e1 = Employee()
e1.name = "Abdul Hadi"
e1.show()
e1.changeCompany('Tesla')  # Any method can't change the value of class var but it will only change for it object
e1.show()

# Employee.company = "Google"   # And we can also change class var like this also 

print(Employee.company)
