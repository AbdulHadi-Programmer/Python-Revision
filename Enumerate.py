# Enumerate Function : # Day 42
# Enumerate is used to write index in for loop 
marks = [21, 23, 54, 90, 76, 48, 1, 4]

# This is without Enumerate function:
index = 0
for mark in marks:
    print(mark)
    if (index == 3):
        print("Harry, Awesome!")
    index += 1
    
print("By Using Enumerate Function:")
# We can also define the starting index in the start of loop
for index, mark in enumerate(marks, start=1):
    print(mark) # print only list element 
    # print(index, mark)  # print the index with index
    if (index == 4):
        print("Harry, Awesome!")


# My new Programmer list are ready to learn
lst1 = ["Abdul Hadi", "Maiz"] # we are working and are learning above 
lst = ["Sohail", "Ahmed Raza", "Farman"]


