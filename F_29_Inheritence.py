"""
 Author: Furqan Fiaz
 Date: 1-09-2022, 10.31 Pm
 This file will contain the information about Single level Inheritence in Python
"""
# Inheritence is use of previously developed functions without writting them again
# The aim of inheritence is code reusability

class Employer:
    def __init__(self,name,age,role):
        self.name=name
        self.age=age
        self.role=role
    def addition(self,num1,num2):
        return num1+num2

    def print_Info(self):
        print(f"The name is {self.name} age of person is {self.age} and role is {self.role}")
        return

Akbar=Employer("Akbar",34,"CEO")
Akbar.print_Info()

# What if we want to use the function of Employer class and define another class and also use its functions at the same time
# Simple put the name of class to be inherited in brackets (SYNTAX)
class Employee(Employer):
    def __init__(self,name,age,role,earnings):
        self.name=name
        self.age=age
        self.role=role
        self.pay=earnings

    def print_Info(self):
        print(f"The name is {self.name} age of person is {self.age} and role is {self.role} and the last thing is {self.pay}")
        return
Ali=Employee("Ali",23,"Programmer","34000")
Ali.print_Info()
# // Here the addition function is defined in Employer class but we were able to use it
print(Ali.addition(23,34)) 