""""
 Author: Furqan Fiaz
 Date:09-09-2022, 12.16 Am
 This file will contain the information about Abstract Class in Python
"""
from abc import ABCMeta,abstractmethod

# abstractmethod() is a decorator

# Sometimes we need a base class which defines some rules that all the derived classes must contain a specific method
# Abstract classes are used to define this rule
class A(metaclass=ABCMeta):
    @abstractmethod
    def Info(self):
        return 0
# Using abstract class we have defined that every derived class of class A must have a Info method in them, otherwise it will throw error


class B(A):
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def Info(self):
        return(self.name,self.age)

if __name__ == '__main__':
    obj1=B("Ali",23)
    # When an object/instance is created if a method is not created in derived class error will be thrown

    print(obj1.Info())

# IMPORTANT: You cannot create instances of abstract base class