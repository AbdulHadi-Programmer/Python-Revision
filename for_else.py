# For Loop with Else:
# Else is used with both loop (for and while)
for i in []: # range(0 till n-1)
    print(i)
# else is execute when the loop body executed or when loop doesnot run due to certain condition
else:
    print("Sorry no i")
# like this above example, in this for loop is used on a empty list so that loop doesnot run or executed and else is executed
# and if loop break or termiate using break statement or condition then else is not executed
## Example:
for i in range(6):
    print(i)
    if i == 4:
        break
else:
    print("Sorry no I")
# Else is only execute when loop is end or completed 
# Else is not executed when loop is break or terminated

# While loop wirh else:
# Example:
print("While loop")
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop completed")

## Break with example :
for i in range(5):
    print(i)
    if i == 2:
        print("Breaking the loop")
        break
else:
    print("Loop completed")