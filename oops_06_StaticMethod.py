### Static Method:  # self is not used in its function argument
# It is a part of class and we can call it while making object like:
# a = Math.add(6, 3)
## The @staticmethod decorator is used to define a static method in a class.
## Static methods don't have access to the instance or its attributes,
## they are more like standalone functions within the class.
# Static methods can be called on the class itself or on an instance.
# They don't have access to the instance (self) or its attributes.
# Static methods are functions that are defined within a class but are not bound to an instance of the class.
# They are decorated with @staticmethod or defined within the class without the self parameter.
# They cannot access or modify instance attributes directly.


### Instance Method:
# Instance methods are functions that are associated with an instance of a class.
# They are defined using the def keyword within the class and take self as their first parameter, which represents the instance.
# They can access and modify instance attributes.
# Instance methods are called on instances of a class.
# They can access and modify instance variables using self. 

class Math:
    def __init__(self, num):
        self.num = num 
    
    # Instance Method
    def addtonum(self, n):
        self.num = self.num + n
        # self.m = self.num + n      # create new var for changes
    
    @staticmethod
    def add(a, b):
        return a+b
    
    

# Creating an object of the Math class and giving it the num value 5
a = Math(5)
print(a.num)  # Printing the num variable value

# Calling the addtonum method to add 14 to the num value
a.addtonum(14)
print(a.num)  # Printing the updated num value

# We can also call the add method through the instance
print(a.add(4, 5))

# Alternatively, calling the add method through the class name
print(Math.add(10, 5))

# Correcting the call to the add method (using the class name or instance)
print(Math.add(5, 78))