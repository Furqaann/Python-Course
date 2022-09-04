"""
 Author: Furqan Fiaz
 Date: 28-08-2022, 4.15 Pm
 This file will contain the information about Self and init() in Python
"""
# defining class
class Computer:
    display=14
# The self is a nickname given to instance/object, we access it in method using self
    def print_details(self,no):
        return f"The name of {no} laptop is {self.name}, ram is {self.ram}, generation is {self.gen} " \
               f"display is: {self.display} inch and operating system running is {self.OS}"

dell=Computer()
hp=Computer()

dell.ram="4Gb"
dell.name="Dell inspiron"
dell.gen="4th"
dell.OS="Windows"


hp.ram="8Gb"
hp.name="HP Elitebook"
hp.gen="8th"
hp.OS="Linux"

# I have defined instances of class and assigned attributes to instances

# Now what is a constructor?
class Motorbike:
    cc=125
    """constructor"""
    def __init__(self,m_name,m_colour,m_rim):
        self.name=m_name
        self.colour=m_colour
        self.rim=m_rim

# The self is a nickname given to instance/object, we access it in method using self
    def print_details(self,no):
        return f"The name of {no} motorbike is {self.name}, colour is {self.colour}, rim is {self.rim} & no of cc is {self.cc}"

yamaha=Motorbike("Yamaha YBR G","Dark Grey","Alloy")
Honda=Motorbike("CG 125","Red","spokes")
if __name__ == '__main__':

    print(dell.print_details(1))
    print(hp.print_details(2))

    print(yamaha.print_details(1))
    print(Honda.print_details(2))

# Both the ways we can assign values to objects, using constructor and normally