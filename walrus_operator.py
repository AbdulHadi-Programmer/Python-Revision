# Walrus Operator (:=) 
# This Operator assign value to a variable within the Expression
# Basic Example :
a = True
# print(a==False)  # Research on this:
# print(a=False) #  If we write this and change the value of a in print then it gives an error
# but if we want to change the value then we use walrus operator, like below 
print(a:=False) 
print(a) # The value is change in above so we get False

numbers = [1, 2, 3, 4, 5]
while (n := len(numbers)) > 0:
    print(numbers.pop())

# Another Example But this is without Walrus:
# foods = list()
# while True:
#     food = input("Enter Food you want to like?: ")
#     if food == "quit":
#         break
#     foods.append(food)

# With Walrus:
foods = list()
while (food := input("Enter Food you want to like?: ")) != "quit":
    foods.append(food)
