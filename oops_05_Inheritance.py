## Inheritance : ( OOPS Main Pillar)
#
class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        
    def showDetail(self):
        print(f"The name of Employee: {self.id} is {self.name}")

# Make another class that contain all method and var of above class
# Employee is a part of 
class Programmer(Employee):
    def showLanguage(self):
        print("The default Language is Python")
    def method(self):
        pass

# Make two Object of Employee Class
e1 = Employee("Asif", 400)
e1.showDetail()
# Object of Other Class
e2 = Programmer("Haroon", 100)
e2.showDetail()
e2.showLanguage()
#################################################
#################################################
#################################################
#################################################
# class Animal:
#     def __init__(self, species):
#         self.species = species

#     def make_sound(self):
#         print("Some generic sound")

# class Dog(Animal):
#     def __init__(self, breed, name):
#         # Additional attributes specific to the Dog class
#         self.breed = breed
#         self.name = name

#     def dog_info(self):
#         print(f"{self.name} is a {self.breed}.")

# # Example usage
# my_dog = Dog(breed="Golden Retriever", name="Buddy")

# # Accessing attributes from the base class
# print("Dog Species:", my_dog.species)

# # Accessing methods from the base class
# my_dog.make_sound()

# # Accessing attributes specific to the derived class
# print("Dog Breed:", my_dog.breed)
# print("Dog Name:", my_dog.name)

# # Using a method specific to the derived class
# my_dog.dog_info()


