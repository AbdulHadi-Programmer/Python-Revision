# map =
# filter =
# reduce =
# Advanced Function Builtin 

def cube(x):
    return x*x*x

print(cube(2))

# Now we want to apply cube function on every list Element:
# this is Complex method and we can do better than this: 
# Shortcut method to make this:
l = [1, 2, 4, 6, 4, 3]
newl = []
for item in l:
    newl.append(cube(item))
print(newl)

# Map Method 
newl = map(cube, l) # This will also do same thing 
# but this can return map object and we can convert it into list
newl = list(map(cube, l)) # Like this: 

print(newl)