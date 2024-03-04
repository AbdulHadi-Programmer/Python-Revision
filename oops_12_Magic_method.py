# Magic Method / Dunder Method:
# __len__ = len of var
# __str__ = This is used to change this "<emp_12.Employee object at 0x000001D92DF05090>"
# into this our own words: "The name of the employee is harry"
# __repr__ = This is also same as above str but we can print both in this ways:
# print(str(e))
# print(repr(e))
## __call__ = this is call using e() and we can use this: 
class Employee:
    def __init__(self, name):
        self.name = name
        
    def __len__(self):
        ## 1st Method: # Both are same 
        # i = 0
        # for c in self.name:
        #     i += 1
        # return i
        ## 2nd Method:
        return len(self.name)
    
    def __str__(self):
        return f'The name of the employee is {self.name}'
    def __repr__(self):
        return f"Employee('{self.name}')"
    def __call__(self):     # Call method is call when we write instance name as a function like e is an instance/object then e() is callable method
        print("I am a call method")
    
e = Employee("Harry")
print(str(e))
print(repr(e))
e()
# print(e.name)
# print(len(e))

# print(len(e.name)) # And we can also see the len with this