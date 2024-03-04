# break : Terminate the loop at specific condition
for i in range(12):
    if (i == 10):
        break 
    print("5 x",i+1, "=", 5*(i+1))

print("Loop ko terminates kardo")


# Continue: Leave or terminate the iteration
for i in range(12):
    if (i==10):
        print("Skip the Iteration")
        continue
    print("5 x", i,"=", 5*i)

for i in [2,3,4,5,6,7,8,0]:
    if (i%2!=0):
        continue
    print(i)
        