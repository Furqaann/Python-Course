"""
 Author: Furqan Fiaz
 Date: 26-08-2022, 4.57 Pm
 This file will contain the information about Decorator function in Python
"""
# A decorator is a function that takes another function and extends
# the behavior of the latter function without explicitly modifying it.
# def sum(num1,num2):
#     return num1+num2
# print(sum(2,44))
#
# def decorator(function):
#     function("This is function function")
# decorator(print)

# Create a function which takes a function as an argument
def execute(print_func):

    def nowexe():
        print("This nowexe function 1st print, before print_func call")
        print_func()
        print("This is after print_func call")
    return nowexe
@execute
def print_func():
    print("This is print_func")


# print_func=execute(print_func)
print_func()
