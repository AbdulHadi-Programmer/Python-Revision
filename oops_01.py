# Object Oriented Programming (OOPS):
# This is the advanced concept that we are learning
# Before we was only learning Procedural Programming 
# class is main concept in oops:
# A class is a blueprint for creating objects. It defines a data structure that 
# contains attributes (characteristics) and methods (functions) that operate
# on those attributes. 
# class keyword is used to make a class:
# It is template named Person and all object contain all var, methods for each object
class Person:
    name = "Abdul Bari"
    occupation = "Programmer"
    networth = 10
    def info(self):
        print(f'{self.name} is a {self.occupation}')
    
a = Person() # Object of a class
b = Person() # New Object of a class
c = Person() # Another New Object of a class

a.name = "Maiz" # By doing this, we can change name but this is a particular object named "a"
a.occupation = "Pythonista" # change occupation

b.name = "Abdul Hadi"
b.occupation = "Businessman"

print(a.name, a.occupation) # object.var in print, print the var
print(b.name, b.occupation) # object.var in print, print the var

a.info() # a.info call the function of a class, where "a" is a object and ".info()" is method from a class
b.info()
c.info() # 'c' is default object , template of class
