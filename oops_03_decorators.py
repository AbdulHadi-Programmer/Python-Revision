# Decorators:
## Decorator is a function itself which can edit function like we want to add greeting after the function at first
# and we have almost 125 function so if we do manually it is boring and time consuming task but we can make a decorator and use
# it before every function name so that it can fulfill our task and now we can write only one decorator before every function name 
# It modify a function, @ is a keyword to write a decorator 
# *args is a tuple taking argument
# **kwargs is a dict taking argument

def greet(fx):
    def mfx(*args, **kwargs):
        print("Good Morning")
        fx(*args, **kwargs)
        print("Thanks For using this function")
    return mfx

# 1st method to use decorator:
@greet # Any one method is used to decorate any function like this:
def hello():
    print("Hello World")

@greet
def add(a, b):
    print(a+b)
    
hello()
add(5,7)
# 2nd Method to use decorator: 
# greet(hello)()  # or like this:
hello()


import logging
def log_func_call(func):
    def decorated(*args, **kwargs):
        logging.info(f"Calling {func.__name__} with args={args} and kwargs={kwargs}")
        result = func(*args, **kwargs)
        logging.info(f'{func.__name__} returned {result}')
        return result
    return decorated

@log_func_call
def ad(a, b):
    return a + b

ad(65, 78)
