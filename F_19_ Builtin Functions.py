"""
 Author: Furqan Fiaz
 Date: 20-08-2022, 10.37 Pm
 This file will contain the information about Builtin Functions and modules in a file in Python
"""
# Import built in modules, we can use functions of that module
# Example random
import random
import keyword
import fractions

# randint will return random number between specified 2 numbers
number=random.randint(0,5)
print(number)
str1=keyword.iskeyword("if")
str2=keyword.iskeyword("elif")
print(str1,str2)
number2=fractions.Fraction
print(number2)

