"""
 Author: Furqan Fiaz
 Date:02-09-2022, 10.04 Pm
 This file will contain the information about Access Specifiers in Python
"""
# Public    Normal definition ( Everyone can use this)
# Protected Use _ for protected variables   (Only Class objects and derived classes can use this variable)
# Private   Use __ for private  (Only base class in which variable is defined can use this variable, inherited classes cannot use it)

class Employee:
    name="Ali"
    _age=88
    __gender="Male"

class company(Employee):
    pass

if __name__ == '__main__':
    obj1=company
    print(obj1.name)
    print(obj1._age)
    # print(obj1.__gender)

    obj2=Employee
    print(obj2.name)
    print(obj2._age)
    print(obj2._Employee__gender)