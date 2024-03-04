# Before python 3.6 version: To Format String:
## format method = not a convient  method
letter = "Hey my name is {0} and I am from {1}"
country ="Pakistan"
name = "Abdul Hadi"
print(letter.format(name, country))

# F-String:
print(f"Hey my name is {name} and I am from {country}")

# For example 1:
price=49.0999999
# and price is a var and ( : .2f) is used to take 2 decimal point in a num
txt = f"for only {price:.2f} dollars!"
print(type(txt))

# Now if we want to show on screen how this f-string then 
print(f"We use f-string like this: Hey my name is {{name}} and I am from {{country}}")