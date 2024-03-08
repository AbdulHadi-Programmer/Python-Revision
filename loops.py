# For loops:
# loop is used to perform a repeatable task
name = "Abdul Hadi"
#for i in name:
#    print(i)
#    if (i=="b"):
#        print("This is the something special!")
    
#colors = ['Red', 'Green', 'Blue', 'Yellow']
#for color in colors:
#    print(color)
#    for i in color:
#        print(i)

# range is a builtin function
# [start : stop: step] and start % End is Excluding

# For Loop: It is based on iteration
print("1st K loop: ")
for k in range(5):   # Run 5 times
    print(k + 1)

print("2nd K loop: ")
for k in range(1, 9):  # Run until i become 9.
    print(k)

print("Table Example loop: ")
# print the table calculator
for i in range(0, 20, 2):
    print(i+2)

print("While Loops Topic Started:- ")
## While Loops:
for i in range(3):
    print(i)
    
print("\nWhile Loops Start")
i = int(input("Enter the number: "))
while (i<=38):
    i = int(input("Enter the number: "))
    print(i)
    
print("Loops Body End")

'''
# decrement while loop
count = 5
# Condition: count is equal to 0, when condition is true then 
while (count > 0):
    print(count)
    count -= 1
else:
    print("I am in Else")

i = 0
while True:
    print(i)
    i += 1
    if (i%100 ==0):
        break
'''