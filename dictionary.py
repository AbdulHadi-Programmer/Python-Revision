# Dictionary:
# it is key value pair data type
# This is empty dictionary {} or dict()
"""
dic = {
    344:"Harry",
    56:"Subah",
    678:"Zakir",
    567:"Oswald"
}
## For accessing the value, we give key like this:
# There are two ways for accessing the key value pair
# This method will give an error if key is not present
print(dic[567])
# This method doesnot give error if key is not present 
print(dic.get(56))
print(dic)

info = {"name":"Abdullah", "age":19,"eligible":True}
print(info)
# print all the key of info dictionary
print(info.keys())
print(info.values()) 

for key in info.keys():
    #print(key) # this can print all key
    print(f"The value corresponding to the key is {key} is {info[key]}")
"""
"""
info = {"name":"Abdullah", "age":19,"eligible":True}
# print(info.items())
print(info)
for key, value in info.items():
    print(f"The value corresponding to the key is {key} is {value}")
"""
## Dictionary Dictionairy: 
ep1 = {122: 45, 123: 89, 567: 69, 670:69} # Sr. Manager dic
ep2 = {222: 67, 566: 98} # manager dic

# ep1.update(ep2)     # add another dictionary to one
# ep1.clear()         # delete all items
# ep1.pop(122)        # pop mean delete any specific key value pairs but key argument is neccessary to give
# ep1.popitem()       # popitem remove last item in a dictionary
# del ep1             # del delete the entire dictionary
# del ep1[123]          # delete any specific entry
# print(ep1)

### Now I am revising Dictionary Topics: (23/02/2023)

dic = {
    "Harry" : "Human Being",
    "Spoon": "Object",
    "car": "Vehicle"
}
print(dic["car"])  

emp = {
    111: "Abdul Hadi",
    122: "Maaiz",
    133: "Sohail",
    144: "Ahmed Raza"   
}
print(emp[122])

info = {
    "name": 'Karan',
    "age": 10,
    "eligible": True
}
print(info)
print(info["name"])
print(info["eligible"])  # This will throw an error 
print(info.get("name2"))  # this is also used to get value with key, but if key is not present then it return none.

print(info.keys()) # to get all keys form dictionary
print(info.values()) # to get all values form dictionary

for key in info.keys():
    print(f"The Value to the key \'{key}\' is \'{info[key]}\'")

print(info.items())
for key, value in info.items():
    print("The value corresponding ")

