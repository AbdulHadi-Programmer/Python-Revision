## Sets = Data Type
#   {}  = open in this bracket
# It is unordered and it doesnot contain duplicate value
# We can't access set particular element using its index bcz it is unordered
"""
s = {3, 2, 4, 5, 2, 4}
print(s)

info = {"Carla", 19, True, 5.9, 19, 8, 4}
print(info)

# Creating an Empty Set
har = set()
print(type(har))

# Acessing the value from loop:
for value in info:
    print(value)
"""
## Set Method:
# those method which are end with update mean that it update the original set
# union(var) = combine two sets, but the both sets are untouched
# var2.update(var) = take the var element and combine it into other set name var2
# intersection(var) = give the comman element of both set
# symmetric_difference(var) = give those value which are not comman in both set 
# difference(var) = give only item that are present in original set and not in both set (A-B)
# isdisjoint(var) = check if both set have no comman element then it return True otherwise return False
# issuperset(var) = check if the var set is a part of other set or not (It mean that if var contain all element that are available in other set then it return True else False)
# issubset() = 
# add() = add a single item 
# remove() = remove an item and raise error if element is not present 
# discard() = remove an item and does nothing when item is not present
# pop() = remove a random item and we can also access it using print(item) after using the pop
# del = delete the entire set 
# clear() = delete the entire set and show the empty set 
s1 = {1, 2, 5, 6}
s2 = {3, 6, 7}
print(s1.union(s2))
s1.update(s2)
print(s1, s2)

# For Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
# cities3 = cities.union(cities2)
# cities3 = cities.intersection(cities2)
cities.intersection_update(cities2)
print(cities)

# For Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
# cities3 = cities.symmetric_difference(cities2)
cities3 = cities.difference(cities2)
print(cities3)

# Example
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Tokyo", "Seoul", "Kabul", "Madrid"}
print(cities.isdisjoint(cities2))

# Example:
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Seoul", "Kabul"}
print(cities.issuperset(cities2)) # check if cities2 is a part of cities  
cities3 = {"Tokyo", "Madrid", "Delhi"}
print(cities.issuperset(cities3)) # and if cities are part of this then it return True else False 
print(cities3.issubset(cities)) # check all the item of the original set are present in a particular set it is then return True else False

# Example:
cities = {"Tokyo", "Madrid", "Berlin","Delhi"}
cities2 = {"karachi", "Seoul", "Delhi"}
# cities.add("Helsinki")
# cities.update(cities2)
cities.remove("Delhi")
cities.discard("London")
print(cities)
item = cities.pop() # Store the pop element
print(cities)
print(item) # and now we can see the element

# del cities
cities = {"Tokyo", "Madrid", "Berlin","Delhi"}
cities.clear()
print(cities)

