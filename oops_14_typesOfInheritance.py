# Single Level Inheritance:
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species 
    
    def make_sound(self):
        print("Sound make by the Animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
    
    def make_sound(self):  # Override the make_sound method
        print("Bark!")

d = Dog("Dog", "Doggerman")
d.make_sound()

a = Animal("Max", "Dog")
a.make_sound()

# Quick Quiz
# implement a cat class by using the animal class. Add some method specific to cat

class Cat(Animal):
    def __init__(self, name, color):
        Animal.__init__(self, name, species="Cat")
        self.color = color
    def make_sound(self):
        print(f"{self.name} makes meows meows sound")
        
c = Cat("Kitty", "White")
c.make_sound()

## Mutiple Inheritance:
class Employee:
    def __init__(self, name):
        self.name = name
    def show(self):
        print(f'The name is  {self.name}')
    
class Dancer:
    def __init__(self, dance):
        self.dance = dance
    def show(self):
        print(f'The dance is  {self.dance}')
    
class DancerEmployee(Employee, Dancer):
    def __init__(self, dance, name):
        self.dance = dance
        self.name = name
        
o = DancerEmployee("Kathak", "Shivani")
print(o.name)
print(o.dance)
o.show()
# Method Resolution Order = mro() , find that if function is call then it is search first in 
# sub class that is DancerEmployee and then the 1st argument of this, and then 2nd argument is search 
print(DancerEmployee.mro())

## Multi level Inheritance:
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    
    def show_details(self):
        print(f'Name: {self.name}')
        print(f'Species: {self.species}')

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Dog")
        self.breed = breed
    
    def show_details(self):
        print(f'Name: {self.name}')
        print(f'Breed: {self.breed}')

class GoldenRetriever(Dog):
    def __init__(self, name, color):
        Dog.__init__(self, name, breed="Golden Retriever")
        self.color = color
    
    def show_details(self):
        Dog.show_details(self)
        print(f'Color: {self.color}')
        
print("The Last Golden Retriever Class")
o = GoldenRetriever("Tommy", "Black")
o.show_details()        
print(GoldenRetriever.mro())

print("The Dog Class")
d = Dog("Max","German Shephert")
d.show_details()
print(Dog.mro())

print("The Animal Class")
a = Animal("Kit", "Russ")
print(Animal.mro())

## Hybrid and Hierarchical Inheritance:
# This is Simple Example of hybrid inheritance, it mean that 
class BaseClass:
    pass

class Derived1(BaseClass):
    pass

class Derived2(BaseClass):
    pass

class Derived3(Derived1, Derived2):
    pass

# Another Example of Hybrid Inheritance:
class A:
    def method_a(self):
        print("Method A from class A")

class B(A):
    def method_b(self):
        print("Method B from class B")

class C(A):
    def method_c(self):
        print("Method C from class C")

class D(B, C):
    def method_d(self):
        print("Method D from class D")

# Creating an object of class D
obj_d = D()

# Accessing methods from different classes
obj_d.method_a()  # Method A from class A
obj_d.method_b()  # Method B from class B
obj_d.method_c()  # Method C from class C
obj_d.method_d()  # Method D from class D
# In this example:
# Class A is a base class.
# Class B and C inherit from class A.
# Class D inherits from both classes B and C, creating a hybrid inheritance structure.
######### Hirarchal Inheritance: (A tree like structure is make in a class)
# like one class A 
#         A 
#       B   C 
#   D,H       E, F
# M,E,J       K, L, N
# Like this above form :
# Explore by yourself: From Chat gpt

    
