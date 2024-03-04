# dir, __dict__ (Attribute not method), help method
# They make it easy to resolve various function and execute code. The above three are builtin function 
## dir():
# The dir() function returns a list of attributes and methods for a given object. 
# It can be used without arguments to list the names in the current local scope or 
# with an object as an argument to get information about its attributes and methods.
## __dict__:
# 
# Dir is used to find all method and attribute of a given data type
x = [1, 2, 3]
print(dir(x))
print(x.__add__)

x = (1, 2, 3)
print(dir(x))

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Harry", 30)
print(p.__dict__)