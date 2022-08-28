"""
 Author: Furqan Fiaz
 Date: 06-08-2022, 6.06 Pm
 This file will contain the information about IF Else statements in Python
"""
var1=23
var2=40
# Find the greatest among 2 integers
greatest1 = var1
if (var2 > var1):
    greatest1 = var2
else:
    print(greatest1)

print("The Greatest among 2 integers is:",greatest1)

# To find the greatest among 3 integers
greatest2=var1
print("Please Enter an Integer value")
var3=int(input())
if (var2 > var1 and var2>var3):
    greatest2 = var2
elif(var3>var2 and var3>var1):
    greatest2=var3
else :
    print(greatest2)

print("The Greatest among 3 integers is:",greatest2)

# To find a certain number is present or not present in list
list=[3,7,10]
if 3 in list:
    print("Yes it is in List")
if 4 not in list:
    print("Yes it is not in list")

# Exercise: Prompt age from user and determine whether they can drive or not
print("Please enter your age")
age=int(input())
if(age>=7 and age<=100):
    print("You are eligible for driving")
elif(age==18):
    print("Can't Determine")
else:
    print("Yoo are not eligible to drive")




