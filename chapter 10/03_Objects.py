# OBJECTS IN OOPs...

# 01 : An object is an intantiation of a class, memory is allocated only after object instantiation..
# 02 : Objects of a given class can invoke the methods available to it without revealing the implementation details to the user..
''' The syntax for object is :
           obj = ClassName()
           print(obj.x)'''
           
           
class Mygame():
    GameType = "ShootingGame "
    def printdata(self):
        print(f'Game Name is {self.name}')
        print(f'Type of game is {self.type}')
    
Game = Mygame()
Game.name = "Shooting Game"
Game.type = "Shooting and killing"
Game.printdata()