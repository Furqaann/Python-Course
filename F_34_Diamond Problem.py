""""
 Author: Furqan Fiaz
 Date:06-09-2022, 11.10 Pm
 This file will contain the information about Diamond problem in Python
"""
# The problem is which class's method will run, there is lot of confusion
class A:
    def info(self):
        print("This is method of class A")

class B(A):
    def info(self):
        print("This is method of class B")

class C(A):
    def info(self):
        print("This is method of class C")

class D(B,C):
    def info(self):
        print("This is method of class D")


if __name__ == '__main__':
    obj1=A()
    obj2=B()
    obj3=C()
    obj4=D()

    obj4.info()
