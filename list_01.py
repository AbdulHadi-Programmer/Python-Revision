# Today we discuss about list 
## list: we can store multiple item of same/different data type 
# list index start from 0 like if we want to access the 1st letter
# of list "l" then we write ( l[0] )
# list item are separated by commas and closed within square bracket [].
"""
l = [3, 5, 6]
print(l)
print(type(l))
# We can make an empty list like that:
lst = list() # 1st method
print(lst)
lst = []     # 2nd method
print(lst)

# Example :
marks = [3, 5, 6, "Harry", True, 6, 7, 2, 32, 345, 23]
print(marks)
print(type(marks))
# Index start from 0
# and length is always start from 1
print(f"The length of list is {len(marks)}")

# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
## Now we discuss about negative indexing 
print(marks[-3])           # Negative Indexing
print(marks[len(marks)-3]) # Positive Indexing
# now how it work:
print(marks[5-3]) # 5 is the length of current list
print(marks[2])   # 5-3= 2 then it print (2nd index) list element 
print(marks[-1])  # This can print last element of a list
# check any specific element is present in a list or not using if-else:
if "Harry" in marks:
    print("Yes")
else:
    print("No")
## Same thing apply for string as well
#  check string contain str
if "ar" in "harry":
    print("Yes")
    
## List slicing
# [start: End: Jump/Step]
print(marks)
print(marks[:]) # [0:len(marks)] ,this is by default set
print(marks[1:]) # [1:len(marks)] , we can change it as well
print(marks[1:-1]) # [1:len(marks)-1] = [1:4] , len(marks) = 5
print(marks[1:9:3]) # print and skip one element , it repeat until the end
"""
#     [1:    4:   2]
#    start: End: jump
# Start is by default 0 until we change it
# End is by default len(marks) until we change it
# jump is by default 1 until we change it 

## List Comprehension :
lst = [i for i in range(4)] # Output: [0, 1, 2, 3]
lst = [i*i for i in range(4)] # Output: [0, 1, 4, 9]
print(lst)
# We can write condition On generating list that is if (i*i) is divisible by 2 and its remainder is 0 then add the num in list
lst = [i*i for i in range(4) if i%2 ==0 ] # Output: 
print(lst)
lst = [i for i in range(10) if i%2 == 0] # Output: [0, 1, 2, 3]
print(lst)
lst = [i for i in range(21) if i%3 == 0] # Output: [0, 1, 2, 3]
print(lst)
