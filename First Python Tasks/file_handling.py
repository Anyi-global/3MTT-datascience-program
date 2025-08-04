'''
File_Mode	Description
r	Open for reading (default)
w	Open for writing, truncating existing content
x	Create a new file and open for writing, fail if exists
a	Open for appending, create new file if it doesn't exist
r+	Open for reading and writing, existing content can be modified
w+	Open for reading and writing, existing content is deleted
a+	Open for reading and appending, existing content is preserved
b	Open in binary mode (combine with other modes like 'rb' or 'wb')
'''

# f = open("MyData.txt", "r") # Open a file in read mode for manipulation

# for l in f.readlines(): # Reads multiple lines from a file and outputs to the console
#     print(l)

# f = open("MyData.txt", "r+") # It opens a file for reading and writing and the existing content can be modified

# f.write("Just appended a new data to this file using 'r+' mode\n")

# f.close()

# f = open("MyData.txt", "w")

# lines = ['line1', 'line2', 'line3']

# f.writelines(lines) # writelines takes a sequence of line statements and add to the file
# f.close()

# print(f.name) # returns the name of the file
# print(f.mode) # returns the file mode
# print("is file readable? ", f.readable) # checks if file readable or not, returns true if readable and false if it is not
# print(f.writable) # checks if file writable or not, returns true if writable and false if it is not
# print(f.close)

# f.close()

# print("Closed now? ", f.close)

# f1 = open('new_file', 'w') # Open a file in write mode for writing contents into it

#copy contents of MyData file into another file
# for data in f:
#     f1.write(data)

# f1.close()

# f = open("MyData", "a") # Add more texts into the file using the append mode

# f.write("\nThis is newly Appended")
# print(f.read()) # Reads the entire file and print to the console
# print(f.readline()) # Reads the first line in the file
# print(f.readline()) # Reads the second line in the file, and so on...
# print(f.readline(5)) # Reads only the first five characters in the file
# f.write("My name is Ifeanyi\n") # Writes a new line to the file
# f.write("I am a Python programmer\n") # "" "" "" "" "" "" "" ""
# f.write("I am learning file handling\n") # "" "" "" "" "" "" "" ""
# f.write("3MTT Data Science program with Darey.io is the best\n") # "" "" "" "" "" "" "" ""

# f.close()

# f2 = open("Myself.jpg", "rb") # Opens the image in a read-byte mode

# print(f2.read()) # Reads byte data. Reads the image as a byte

# f2.close()

# f3 = open("copied_img.jpg", "wb") # Opens a new image file 

# for loop that copies the contents of Myself.jpg into copied_img.jpg
# for i in f2:
#     f3.write(i)

# f3.close()

# using 'with()' statement to open file. It provides a concise and safe way to handle file opening, closing any potential exceptions in the file handling
# with open('MyData.txt', 'a') as f:
#     lines = ['First line', 'Second line', 'Third line']
#     f.writelines(lines)

# f.close()

'''
Using seek() and tell()
Used to mainpulate the file pointer's position within a file object.

seek(offset, whence=0)
Used to move the file pointer to a new position within the file. It takes two arguments:

offset: an integer specifying the number of bytes to move the file pointer. It can be +ve(to move forward), -ve(backward) or 0.
whence(optional): an integer value that defines the reference point from which the offset is to be applied.
It defaults to 0 (referencing the beginning of the file) Some common values for whence include:

0: move to beginning of the file (SEEK_SET)
1: move from the current position of the file pointer (SEEK_CUR)
2: move to the end of the file (SEEK_END)

tell()
This method returns the current position of the file pointer within the file as an integer number of bytes.
It simply tells you where the file pointer is currently located.
'''

# with open('MyData.txt', 'r+') as f:
#     data = f.read(5) # Reads the first five bytes
#     print(data)

#     # Moving the pointer 10 bytes forward from the current position
#     f.seek(7,0)

#     # Reading the next 10 bytes
#     data = f.read(10)
#     print(data)

# Using the tell() function
# with open('MyData.txt', 'r+') as f:
#     print('Current pointer position: ', f.tell())
#     text = f.read()

#     print('Current pointer position: ', f.tell())
#     f.seek(2)

#     f.write("The End!")

#     print('Current pointer position: ', f.tell())


'''
Renaming and deleting files,
Splitting lines
'''

# Renaming and Deleting files
# import os

# os.rename('MyData.txt', 'SampleData.txt')

# Splitting lines
with open('SampleData.txt', 'r') as f:
    lines = f.readlines()

    for l in lines:
        words = l.split()
        print(words)