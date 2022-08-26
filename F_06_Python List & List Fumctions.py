"""
 Author: Furqan Fiaz
 Date: 07-08-2022, 5.32 Pm
 This code will contain the information about Lists, List Functions, Tuples etc
"""
# In Other programming languages Arrays are known as Python Lists in Python

# List is denoted by[] brackets

Class10A=["Ali","Ahmed","Abdullah","Furqan"]
print(Class10A)

Class10A_Result=[10,3,49,11]
Class10A_Result1=[10,3,49,11,20,22,40,22]
print(Class10A_Result)
# To print 4th Value in Both Lists
print(Class10A[3],Class10A_Result[3])
#To sort Numbers
Class10A_Result1.sort()
print(Class10A_Result1)

"""
List Slicing
"""
print(Class10A_Result[0:5])
print(Class10A_Result[::2])
print("Printing The length of Class 10A result",Class10A_Result.__len__())
print("Printing The length of Class 10A result 1:",Class10A_Result1.__len__())

"""
Tuples are a form of List which doesnot changes the value from the list.
tuples are defined using () brackets
Mutable & Immutable
"""
Tuple1=(1,2,40,20)
print(Tuple1)
print("How many times did 2 came in Tuple 1:",Tuple1.count(2))

# You can search for Tuple & List Functions from Internet Easily





