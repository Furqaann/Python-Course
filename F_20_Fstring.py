"""
 Author: Furqan Fiaz
 Date: 20-08-2022, 11.00 Pm
 This file will contain the information about Fstrings and string formatting in a file in Python
"""
# whenever we write in string and we want to insert a variable value in it we use %s
var1=40
var2=45
var3=50
print("Hello Stranger! I got %s %s and %s in math,physics and chemistry exam respectivly"%(var1,var2,var3))
#we can use f string in python
var4=f"Hello stranger! I got {var1} {var2} {var3} in my Maths, physics and chemistry exam repectivly"
print(var4)