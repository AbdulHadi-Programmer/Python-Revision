## Oops Concept Day no 2:
# Constructor is used to make object
# __init__ is a construction, which is a initialize method

class Person :
    # This init called whenever class is created and executed
    def __init__(self, n, o): # This function run everytime when the class is call by an object
        print("Hey I am a Person")
        self.name = n
        self.occ = o
    
    def info(self): # self is a required to make any method
        print(f'{self.name} is a {self.occ}')

# These two argument are given bcz it is required, to see this check init 'n' and 'o'
a = Person("Abdul Hadi", "Python Programmer")
b = Person("Mohtashim", "Flutter Developer")
c = Person()

# Now we can change name and occ like this but we have a faster way to write this:
a.info()
b.info()

