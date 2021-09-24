from World import *
from Player import *

class Controller:
    def __init__(self):
        self.world = World([])
        self.Walker = Player(0)
    
    def play_game(self):
        self.world.fill_world()
        while True:
            print("You are currently in room " + self.world.rooms[self.Walker.room].name + " Where do you wish to move.")
            for room in self.world.rooms[self.Walker.room].connections:
                print("Room " + room)
            while True:
                userInput = input("input: Room ")
                i = 0
                foundRoom = False
                for room in self.world.rooms: 
                    if userInput == room.name:
                        for room in self.world.rooms[self.Walker.room].connections:
                            if  userInput == room:
                                self.Walker.room = i
                                print("")
                                print("You entered room " + room + ".\n")
                                foundRoom = True
                    i += 1
                if foundRoom == False:
                    print("Input is not valid")
                else:
                    if  self.world.rooms[self.Walker.room].finalRoom == True:
                        print("You find ")
                        
                        self.world.rooms[0].addConnection()
                    else:
                        self.world.rooms[self.Walker.room].describeRoom()
                        break

game = Controller()
game.play_game()