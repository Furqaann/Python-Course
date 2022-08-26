"""
 Author: Furqan Fiaz
 Date: 06-08-2022, 5.37 Pm
 This code will contain the information about variables, datatypes and types casting
"""
var1="Hello World!\n"       # This is String variable
var2=30                             #This is integer
var3=36.45                          #This is float
var4="23"
var5="50"

print(type(var1))                   #By using type in print function we can print the type of the data inserted
print(type(var2))
print(type(var3))

print(" The Addition of var2 and var3 is: ",var2+var3,"\n")

"""
How we can convert a string into an integer automatically?
we can so by Type casting
"""
print("Since both the variables are string but they are converted in int and added ",int(var4) + int(var5),"\n")
print(100 * int(var4)+int(var5))
print(10 * var1 )
"""
str()
int()
float() 
"""
# User Input
print("Enter  2 Numbers to get their product")
num1=input()
num2=input()

num3=int(num1)*int(num2)
print("The Product of ",num1," and ",num2," is: ",num3)