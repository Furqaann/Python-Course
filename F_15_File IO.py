"""
 Author: Furqan Fiaz
 Date: 14-08-2022, 4.17 Pm
 This file will contain the information about File Input Output in Python
"""
"""
"r" - Open File for reading               - Default mode
"w" - Open File for writing
"x" - Creates file if not exists
"a" - Add more content to a file
"t" - text mode                           - Default mode
"b" - binary mode
"+" - read and write
"""

#open("F_15_File.txt") # It will not return any value for printing
# f=open("F_15_File.txt") # f is the file pointer
# content=f.read()
# print(content)
# f.close()

# Open in mode
# f=open("F_15_File.txt","rb") # it will read in binary
# content=f.read()
# print(content)
# f.close()

# ReadLine Function
f=open("F_15_File.txt")
# for line in f:
#     print(line)
# To print without line break
for line in f:
    print(line, end="")
