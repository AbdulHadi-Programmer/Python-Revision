# Getter And Setter
# @property is a decorator use to write a getter it only change the var in itself 
# @var_name.setter create a setter named property which can change the 'var' in whole program
# When object is make and value is give like this:
## o = MyClass(45)
## print(o.value)
# Then Output will be:-
# first the value is 45 given, then it directly call getter function which change 
# the value in itself and then return the changed value but also remember that it 
# only change value in itself, the original is remain same as we can use show()
# to see this and now i will explain how Setter is Works:
## obj = MyClass(45)  # 1st Step
## obj.value = 67     # 2nd Step  
## print(obj.value)   # 3rd Step
## obj.show()         # 4rd Step
# Now The object is created with class and the value is given 45
# 2nd = obj.value = 67 , is changed because we use setter for this and remember this is a private var
# 3rd = print the obj.value , now the twist begin here, now the 67 is given to getter function and then it changed the value in itself and show the changed value
# obj.show method is used to show the original var, that is changed because we use setter after using this, the value is changed 

class MyClass:
    def __init__(self, value):
        self._value = value
    
    def show(self):
        print(f'Value is {self._value}')  
    
    @property  # Doesnot change the value
    def value(self):
        return 10* self._value 

    @value.setter # setter change the value
    def value(self, new_value):
        self._value = new_value / 10

obj = MyClass(45) 
print(obj.value) # get the value with performed operation (getter function)
obj.value = 67 # Set the value 
print(obj.value) # get the value with performed operation
obj.show()
# _underscoreVar is used to make a private var that is also called Incapsulation
print(obj._value)
# In python, we can directly access the private var but in other programming it 
# is stricted rules that we can't get direct access to private var


## Another Example:
# To explain Getter and Setter: 
# class named circle

# class Circle:
#     # Constructor, that has radius name argument 
#     def __init__(self, radius): 
#         self._radius = radius  # Encapsulation: Attribute is marked as protected

#     @property
#     def radius(self):  # Getter method
#         return self._radius

#     @radius.setter
#     def radius(self, value):  # Setter method
#         if value < 0:
#             print("Error: Radius must be non-negative.")
#         else:
#             self._radius = value

# # Example usage:
# circle = Circle(5)
# print(circle.radius)  # Using the getter

# circle.radius = 7  # Using the setter
# print(circle.radius)