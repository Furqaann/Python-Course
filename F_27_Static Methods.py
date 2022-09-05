"""
 Author: Furqan Fiaz
 Date: 31-08-2022, 10.01 Pm
 This file will contain the information about Static Methods in Python
"""
class Student:

    def __init__(self,name,section,s_class,age):
        self.name=name
        self.section=section
        self.stu_class=s_class
        self.age=age
    def Stu_data(self):
        print(f"Student information is as follows {self.name}, section is {self.section},stu class is {self.stu_class} & age is {self.age}")

# Static methods are unchangeable, they can used to print data or stuff like that
    @staticmethod
    def stat_method(string):
        print(f"Hello I am {string}")

if __name__ == '__main__':
    Ali=Student("Ali","Red","6th",14)
    Ahmed=Student("Ahmed","Blue","5th",13)
    Ali.stat_method("Ali")

    Ali.Stu_data()
    Ahmed.stat_method("Ahmed")