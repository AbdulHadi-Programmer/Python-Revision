# short Function: Lambda
# Normal way to create a function 
def double(x):
    return x*2
# Make Anonymous Function using Lambda:
double = lambda x: x*2
print(double(5))

# lambda is used to make short function but if we want to make complex function then lambda is not useful
def cube(x):
    return x*x*x
# lambda (1 argument is var, 2nd argument is expression what we want to do)
cube = lambda x: x*x*x
print(cube(5))

avg = lambda x, y, z: (x + y + z) / 3
print(avg(4, 6, 20))

## we can use function inside function
# the function 1st argument is given function, and 2nd value is the argument of given function
def appl(fx, value):
    return 6 + fx(value)
# appl(cube is a given function that is an argument, and 2 is an argument of given function)
print(appl(cube, 2))
# Now the function give 14 as answer, now i will explain what is happening 
# first cube of 2 is solve that is 8 and 
# then the given value is return to the appl function and it add 6 with 8 that is 14 
print(appl(cube, 5))
# We can also write function like this:
# In lambda expression first argument and expression are give the after separating with commas we write the value to the given lambda function 
print(appl(lambda x: x*x, 2))

# We can also write the Anonymous Function like this:
add = lambda x,y: print(f'{x} * {y} = {x*y}')
add(4, 5)
