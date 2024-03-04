# Tuple = Data Type
# Mutable, It can't be Changed 
# It is made by (round bracker and comma is necessary, ) and tuple() this is also used to make a tuple
# make one value tuple and also remember comma
tup = (1, 2, 4, 8, 5, "green", True)
print(type(tup), tup)
print(tup[0])
print(tup[1])
print(tup[2])
# Ways to handle negative indexing:
print(tup[-1])         # way no 1
print(tup[len(tup)-1]) # way no 2
print(tup[7-1])        # way no 3
print(tup[6])          # way no 4

if 2 in tup:
    print("Yes 2 is present in a tuple")
    
# Tuple Slicing:
# By slicing, this can make a new tuple like this:
tup2 = tup[1:4]
print(tup2)

## Tuple Method:
# For Example 1:
# For Changing tuple, first we need to change this into a list by typecasting
countries = ("Spain", "Italy", "Pakistan", "England", "Germany")
# print(countries) # print the whole tuple 
temp = list(countries)
temp.append("Russia") # Add item in the end to list
temp.pop(3) # remove item
# print(temp) # print the temp list that have additional "russia" item and remove 3rd element in list
temp[3] = "Finland"
countries = tuple(temp)
print(countries)

# For Example 2:
# This can merge two tuple and make a 3rd new tuple
countries = ("Pakistan", "Afghanistan", "Turkey", "Saudi Arab")
country = ("Egypt", "Qatar", "Jordan")
Mus_countries = countries + country
print(Mus_countries)

## Tuple Methods:
# count() = Count how many time the given element is present
# index() = give the index of given element at first occurence
#           and it will give value error if the given elment is not present
# () =
# () =
# () =
# index() And it raise value error when the elemeny is not present in tuple
tup1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 1, 2, 2, 2, 2, 4, 2)
# res = tup1.count(2)
# print('Count of 2 in tuple is:', res)
# res = tup1.index(4)
## Tuple Slicing:
res = tup1.index(3,         4,   8)
#             (argument, start, End)
print(res)