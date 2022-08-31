"""
 Author: Furqan Fiaz
 Date: 18-08-2022, 5.21 Pm
 This file will contain the information about Seek(), tell(), opening file using with block in a file in Python
"""

# a=open("F_17_seek.txt","r+")
# a.write("Hello Stranger!")
# a.write("You're Awesome")
# a.close()
#
# f=open("F_17_seek.txt","r+")
# f.write("Yes you're Right")
# print(f.readline())
# print(f.readline())
# f.close()

a=open("F_17_seek.txt","r+")
# Sometimes we dont know where we at in the file so we use tell function to know that
print(a.tell())
print(a.readline())
print(a.tell())
# If we want to begin grom a certain point in the file we use seek function
a.seek(2)
print(a.readline())
a.seek(17)
print(a.tell())
print(a.readline())
a.close()

print("Printing With Block:-")
# If we want to open file using with block
with open("F_17_seek.txt") as f:
    print(f.read())
