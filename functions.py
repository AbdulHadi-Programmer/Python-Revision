# Function: (We use function to reuse our code again and again)
# def is a keyword used to make a function

# This is a simple way to write code without function, we have to write all code again and again:
a = 9
b = 8
gmean = (a*b)/(a+b)
print(gmean)
c = 8
d = 7
gmean = (c*d)/(c+d)
print(gmean)

# After making Functions:
def calculategmean(a, b):
    mean = (a*b)/(a+b)
    print(mean)
    
calculategmean(4, 12)
calculategmean(8, 2)
calculategmean(5, 22)

def isgreater(a, b):
    # Check a is greater than b
    if (a>b):
        print("First Num is greater")
    # Check b is greater than or equal to a
    else:
        print("Second Number is greater or equal")

isgreater(5, 2)
isgreater(15, 15)
isgreater(8, 9)

# pass is the keyword when we want to write code later, the interpreter ignore pass
def islesser(a, b):
    pass

# Builtin function: (It is builtin Func)
# User defined function: (User defined or make this function)