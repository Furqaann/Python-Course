"""
 Author: Furqan Fiaz
 Date: 1-09-2022, 10.50 Pm
 This file will contain the information about Multiple Inheritence in Python
"""

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
class Player:
    def __init__(self,name,players):
        self.name=name
        self.players=players

    def print_gameinfo(self):
        print(f"The name of game played is {self.name} and no of players are {self.players}")

    def subtraction(self,num1,num2):
        if(num1>num2):
            return num1-num2
        else:
            return num2-num1

class Employer_Player(Employer,Player):
    pass
class Player_Employer(Player,Employer):
    pass

if __name__ == '__main__':
    Furqan=Employer_Player("Furqan",22,"CEO")
    Ali=Player_Employer("Football",11)

    # we can use any methods of both Employer and player class
    Furqan.print_Info()
    Ali.print_gameinfo()
    print(Furqan.subtraction(23,33))
    print(Furqan.addition(23,33))

    # As shown above we can use both the methods of both the class inherited
