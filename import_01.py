# Day 44
# import keyword = is used to get modules
import math as m # this is a short abbrevation to use module name while using its function
# we can also specify, which function we want to import like below:
# Now we can use function without using module name

# And we can also import all function and use it by only function name
# from math import sqrt, pi
from math import *
## We can also use abbrevation
# from math import sqrt as s
## now pi is imported normal but sqrt is imported with abbrevation
from math import pi, sqrt as s
print(s(25))

# a = m.floor(4.232)
a = sqrt(169) * pi

print(a)
print(13*3.14)

## dir function is used to show all function of a specific Function
import math
print(dir(math))
# we can also find the type of a function that takes which var
print(math.nan.__doc__, type(math.nan))
# Now we can see the doc_String of a function
print(math.__loader__.__doc__)


# Now we can see the module function using loop
'''
a = dir(math)
for index, i in enumerate(a, start=1):
    print(index, i)
'''

# from harry_imp import harry, welcome
# from harry_imp import *
import harry_imp as hr
# These are function and var that is using from other files
hr.welcome()
print(hr.harry)