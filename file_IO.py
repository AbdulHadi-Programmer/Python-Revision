## File Handling (File IO):
# open a file = open("file_name", "mode")
# Modes to open a file:
# 'r' = for read (default mode)
# 'w' = for write (write  is use to write content on a file ) and it create the file when it doesnot it create the file and it overwrite the file content 
# 'a' = for append()
# 'x' = create the file and gives an error if file already exist
# 'b' = read binary file like images, pdf, etc
# 't' = used to read text file 
# 'rt' = read file in text mode  
# 'rb' = read file in binary mode
## If the file Exist then It run properly but
#  when the file doesnot found it will gives an error 
# f = open("myfile_IO.txt", "rt")
# f = open("myfile_IO.txt", "rb")
# f = open("myfile_IO.txt")
# Read content from a file:
'''
f = open("myfile_IO.txt", "r")
text = f.read()
print(text)
# close the file
f.close()

## Writing a file:
# 'w' mode is used to open a file and it deleted the current content and add new content
# if we want to append text in a file then we use 'a' append mode
# This is 1st method for file handling:
# f = open('myfile2_IO.txt', 'a')
# f.write(" Hello, World! ")
# f.close()
# 2nd Methods
with open('myfile2_IO.txt', 'a') as f:
    f.write("\nHey I am inside with")
'''
#### Read, readline, readlines   Day 50
f = open('myfile2_IO.txt', 'r')
while True:
    line = f.readline()
    if not line:
        break
    print(line.rstrip())