## Access Modifier:
# Public Access Modifier = All var are public which is used by anyone
# Private Access Modifier = 
# Protected Access Modifier = Protected Var, can't access directly but can be indirectly


# Public Access Modifier
class Employee :
    def __init__(self):
        self.name = "Harry"  # Public Variable
        self.age = 32        # Public Variable
a = Employee()
print(a.name)

# Private Access Modifier
class Employee:
    def __init__(self):
        self._name = 'Abdul Hadi'      # Private Var
        
b = Employee()
print(b._name)

# Protected Access Modifier = Protected Varible 
class Employee:
    def __init__(self):
        self.__name = 'Abdul Bari' # Protected var
        
c = Employee()
# print(c.__name)  # We can't access it directly, and this will throw any error
print(c._Employee__name)  # We can access it indirectly 