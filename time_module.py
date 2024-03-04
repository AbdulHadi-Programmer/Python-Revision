# Time Module:
import time
# time.time() = give the current time mean total time from 1970 to today current year 
# time.sleep() = sleep for int() second 
# def usingWhile():
#     i = 0
#     while (i<50000):
#         i += 1
#         print(i)
        
# def usingFor():
#     for i in range(50000):
#         print(i)

# init = time.time()
# usingFor()
# print(f'The Time to calculate 50000 using for loop {time.time() - init}')
# time.sleep(6)
# t1 = time.time() - init
# # print(time.time()- init)
# usingWhile()

# # print(time.time()- init)
# print(f'The Time to calculate 50000 using While loop {time.time()- init}')
# print(f'The Time to calculate 50000 using for loop {t1}')
# print(time.time())
# print(4)
# time.sleep(3)
# print("This is printed by 3 seconds")

t = time.localtime()
formatted_time = time.strftime("%Y-%m-%d, %H : %M : %S")
print(formatted_time)