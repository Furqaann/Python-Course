"""
 Author: Furqan Fiaz
 Date: 06-08-2022, 6.06 Pm
 This code will contain the information about variables, datatypes and types casting
"""
# This file contains the string slicing and Functions
var1="Furqan is a good boy"
#print(var1[2]) For printing a single character
print(var1[0:6])
print(len(var1))                            # to print the length of the string

""" 
Advance Slicing
What if we want to get characters from a string by skipping 1 character , 2 character and so on each time
"""
print(var1[0:6:2])
print(var1[0:6:3])

#Negative Indexes
"""
In my string the opposite end characters are treated as negative indexes, such as in var1 y is equal to -1, o=-2, b=-3 and so on"""
print(var1[-1:-4]) # Not printing in my case but it is possible

# To invert the string
print(var1[ : :-1])

""" 
String Functions
1. Return true and false whether the string is alpha numeric
2. Count how many times a character occured in the string
3. Print Length
4. Search in the string
"""
print(var1.isalnum())
print(var1.count("o"))
print(var1.__len__())
print(var1.find("a"))