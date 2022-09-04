"""
 Author: Furqan Fiaz
 Date: 26-08-2022, 7.03 Pm
 This file will contain the information about Object Oriented Programming in Python
"""
# We create different classes for performing different functionalities.(Class is more like a template, predefined things)
# Objects are instances of that class, e.g we created a class car, now the car has no of tires, colour, engine capacity, engine no etc,
# these things are written only once in class and used again and again by creating different objects
class Car:
    """ To tell interpreter nothing is written"""
    no_tires = 4
    pass
""" Creating objects """

Corolla = Car()
Hilux = Car()
Civic = Car()

"""Assigning values to objects:-"""
Corolla.colour="red"
Corolla.engine="1500cc"
Corolla.seating_capacity=5

Hilux.colour="white"
Hilux.engine="3200cc"
Hilux.seating_capacity=5

Civic.colour="grey"
Civic.engine="1800cc"
Civic.seating_capacity=5

if __name__ == '__main__':
    print(f"The colour of corolla is {Corolla.colour} and no of tires are {Corolla.no_tires}")