# Today we discus about function and its arguments

# Now a and b are default argument:
def avg(a, b):
    print("The Average is", (a+b)/2)
avg(4, 8)

# Now a and b are default argument:
def avg(a=9 , b=1):
    print("The Average is", (a+b)/2)

# if we call func, and argument define above
avg()
# and if we defined at the end with above then
# it take function calling argument as important 
# And ignore above  argument
avg(4, 8)
# a is given and b is taken from above, b = 1
avg(5)


# keyword Argument:
avg(b=6, a=7)

# b is given and a is taken above, a = 9
avg(b=14)
# a is given and b is taken from above
avg(a=5)

def average(a,b, c=1):
    print("The average is",(a+b+c)/3)

# In this function c is defined above 
# and a , b is required argument, we have to define it below
average(5, 16)

# this can create a tupe 
# and we can make avg of multiple limit 
def avg(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("Average is:", sum/len(numbers))
    
average(5, 65, 15)

# This argument can make a dictionary
def name(**name):
    print(type(name))
    print("Hello", name["fname"], name["mname"], name["lname"])

name(mname = "Bachan", lname="Barnes", fname="James")

# Now we disuss about "return"
def avg(*numbers):
    sum = 0
    for i in numbers:
        sum = sum + i
    #print("Average is:", sum/len(numbers))
    return sum/len(numbers)
    # 

c = avg(5, 65, 15)
print(c)