""""
 Author: Furqan Fiaz
 Date:05-09-2022, 11.40 Pm
 This file will contain the information about Polymorphism , Super & Overriding in Python
"""
# Ability to take various forms
# Two types 1- Compile Time 2-Run Time

# 1.1=Function Overloading
# 1.2=F_12_Operators Overloading

# 2.1 Virtual Functions

class A:

    varA="variable of class A"
    def __init__(self):
        self.instance_varA1="1st variable of instance class A"
        self.instance_varA2="2nd variable of instance class A"


class B(A):
    varB = "variable of class B"
    # By defining a new constructor we have overriden the constructor of base class
    def __init__(self):
        # self.instance_varA1="1st variable of instance class B"

        self.instance_varB1 = "1st variable of instance class B"
        self.instance_varB2 = "2nd variable of instance class B"
        super().__init__()
        # We use super keyword to use constructor of base class
if __name__ == '__main__':
    a=B()
    print(a.varA)
    print(a.instance_varA1)