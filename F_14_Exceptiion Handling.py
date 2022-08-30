"""
 Author: Furqan Fiaz
 Date: 13-08-2022, 5.48 Pm
 This file will contain the information about Functions in Python
"""
# In C/C++ we have try and catch
# In Python we have try and except
# Exception handling is used to capture errors if they occur, They can occur or they cannot occur
"""
# This code will run perfectly fine 
print("Enter Num 1:")
numb1=int(input())
print("Enter Num 2:")
numb2=int(input())
print("Sum of two numbers is:",numb1+numb2)"""

# using exception handling
print("Enter Num 1:")
numb1=input()
print("Enter Num 2:")
numb2=input()
try:
    print("Sum of two numbers is:", int(numb1) + int(numb2))
except Exception as e:
    print(e)# Error will be printed as a string

print("maybe try again later")

