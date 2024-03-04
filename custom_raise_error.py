# Raise Keyword 
# we can raising custom error by using raise
a = int(input("Enter the number betweem 4 and 9: "))

if (a<4 or a>9):
    raise ValueError("Value should between 4 and 9")

## learn more about this topic on Chat gpt or Youtube 
# Write a program if user enter quit in lower case then the program run and no error occurs
a = input("Enter the num between 5 and 9: ").lower()
if (a == 'quit'):
    print("Program Successfully Run")
    
elif (int(a)<4 or int(a)>9):
    raise ValueError("Value Should between 4 and 9")
