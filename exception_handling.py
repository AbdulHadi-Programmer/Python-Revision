# Try Except Exception :
# Error Handling: 
'''
a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
# Check the code, if it run then it execute 
# and if there is an error then the control of program give to the except keyword
try:
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")

# except Exception as e:
except Exception:
    # print(e)
    print("Invalid Input")
    
print("Some imp lines of Code")
print("End of Program")
'''
## Another Example:
# This is used to handle error
try:
    num = int(input("Enter an Integer: "))
    a = [6, 3, 2]
    print(a[num])
    
except ValueError:
    print("Number Entered is not Integer")
# this handle IndexError like if user enter out of range index 
except IndexError: 
    print("Index Error")

