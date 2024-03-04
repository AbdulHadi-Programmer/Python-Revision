# Doc-String :
# python docstring are the string literals that appear right
# after the defination of a function , method, class, or module:

def square(n): # This is a doc-string
    '''Takes a number n and return a square of n''' # But we want to print the doc-string then it only recognize the first doc-string
    """ This is also way to write doc-string """
    print(n**2)
    
square(25)
# We can also print doc-string like this:
print(square.__doc__)
# Doc-string is a string and it is not a comment
# By changing Doc-string the program output will also change 
# 2nd Scenario:
def square(n): # This is a doc-string
    print(n) # If we write any code body of function then the doc-string is none and below line is treated as comment
    '''Takes a number n and return a square of n''' # But we want to print the doc-string then it only recognize the first doc-string
    """ This is also way to write doc-string """
    print(n**2)
    
square(25)
# That's why the doc-string is written at the top of function before func body is written

## PEP 8

# Zen of Python (A poem by Tim peter)
import this
