## Local vs Global Variable:
# local var that is made inside a function and we can't use it outside the function
# global var that is made outside the function and we can use it anywhere we can
# global var is make using global keyword, and by using we can change the local var into global and global is being ignored
x = 4         # Global Var
print(x)

def hello():
    x = 5         # local Var
    y = 1
    print(f"The local var is {x}")
    print("Hello harry")
# This will print the function var as it is local var
print(f"The global var is {x}")
hello()

# This will print 4 as it is global var
print(f"The global var is {x}")

# Another Example:
# Now by using global, now x value is change from 10 to 4 like we see below
x = 10     # Global var
print("\nAnother Example:")
def func():
    global x
    x = 4
    y = 5  # local Var
    print(y)


func()
print(x)
# print(y)


a = 10 
def abc():
    global a # this global keyword change the existing var
    a += 10
    print(a)
    
abc()
print(a) # with gloal; output 20
print(a) # without gloal; output 10
