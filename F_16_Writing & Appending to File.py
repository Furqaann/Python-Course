"""
 Author: Furqan Fiaz
 Date: 14-08-2022, 5.11 Pm
 This file will contain the information about File writing & appending to a file in Python
"""
# To write only mode
# a=open("F_15_File.txt","w")
# a.write("I am try write in the file")
# a.close()
# To read only mode
# f=open("F_15_File.txt","r")
# content=f.read()
# print(content)
# To read and also write
f=open("F_15_File.txt","r+")
content=f.read()
print(content)
f.write("Hello world! My name is Furqan")

f.close()