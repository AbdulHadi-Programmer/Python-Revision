# Finally Keyword:
# It is used with Try Except Error Handle
# Finally is always executed
try:
    l = [1, 2, 3, 4]
    i = int(input("Enter the index: "))
    print(l[i])
except:
    print("Some Error Occured")
    
finally: 
    print("I am always Executed")

# Diff b/w print and finally using after try except:
# In this print will run :
def func1():
    try:
        l = [1, 2, 3, 4]
        i = int(input("Enter the index: "))
        print(l[i])
    except:
        print("Some Error Occured")
    # And this print is outside the except and try block
    print("I am always Executed")
func1()

# Now we see the main of finally, after executing return the function is close
# but if we use finally then the code will always executed 
print("\nFinally use function\n====================")
def func1():
    try:
        l = [1, 2, 3, 4]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some Error Occured")
        return 0
    # finally: 
    #     print("I am always Executed")
    # And now we using print but it can't be executed
    print("I am always Executed")
x = func1()
print(x)
