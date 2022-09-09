"""
 Author: Furqan Fiaz
 Date:02-09-2022, 10.04 Pm
 This file will contain the information about MultiLevel Inheritence & Overriding in Python
"""
class Dad:
    name="Ahmed"
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def Personal_info(self):
        return f"HELLO! I am {self.name}, and my age is {self.age}"

class Son(Dad):
    # name="Akbar"
    def __init__(self, earning, phone):
        self.earning = earning
        self.phone = phone

    def Personal_info(self):
        return f"HELLO! My earning is {self.earning}, and my phone no is {self.phone}"
# This method is already defined in dad class from where it is inherited, then we defined it again in son class it is overriden
# when called instead of DAD Personal info func, Son personal info would be called
class Grandson(Son):
    pass

if __name__ == '__main__':
    Ahmed=Dad("Ahmed",60)
    Akbar=Son(45000,4444)
    Ali=Grandson(34000,23)

    # print(Ahmed.Personal_info())
    # print(Akbar.Personal_info())
    # print(Ali.Personal_info())
    print(Ali.name)
# In th eabove example Ali.name, we have define variable in 3 different classes. when called compiler will look first in Grandson
# if not found then will look in Son class and if not found would look in Dad class.

# QUIZ:
class Electronic_Device:
    name="Trimmer"
    voltage="12v"
    charging=True

    def Info(self):
        return f"Device Name is {self.name} & voltage is {self.voltage} and is charging possible? {self.charging}"

class Pocket_gadget(Electronic_Device):
    name = "Taser"
    voltage = "12v"
    charging = False

    def Info(self):
        return f"Device Name is {self.name} & voltage is {self.voltage} and is charging possible? {self.charging}"

class Phone(Pocket_gadget):
    # name = "Samsung"
    # voltage = "12v"
    # charging = True
    def Info(self):
        return f"Device Name is {self.name} & voltage is {self.voltage} and is charging possible? {self.charging}"

electronic=Electronic_Device()
print(electronic.Info())
Pocket=Pocket_gadget()
print(Pocket.Info())
phone=Phone()
print(phone.Info())