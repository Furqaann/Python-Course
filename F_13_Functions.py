"""
 Author: Furqan Fiaz
 Date: 13-08-2022, 5.22 Pm
 This file will contain the information about Functions in Python
"""
a=45
b=45
# Builtin Functions, press control and click sum for more built in functions
#print(sum((a,b)))
# We define functions in python using def keyword
def sumation():# we have defined a function, to perform its functionality we need to call the function
    print("The sum of two integers is:",34+45)

sumation()# This is function call, we can call it as many times we want
"""sumation()
sumation()
sumation()"""
# What if we want to print sum of two different integer values every time.
# We give it parameters
def multiplication(a,b):
    #print("The mutiplicated value is",a*b)
    multi=a*b
    return multi
multiplication(a,b)
g= multiplication(a,b)
print(g)

# Docstring, what is docstring
#The first string written after function declaration
def multiplication2(a,b):
    """ This function will calculate product of two numbers"""
    multipli=a*b
    return multipli
f=multiplication2(a,b)
print(f)