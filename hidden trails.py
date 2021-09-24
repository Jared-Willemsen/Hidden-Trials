from World import *
from Player import *

class Controller:
    def __init__(self):
        self.world = World([])
        self.Walker = Player(0)
    
    def play_game(self):
        self.world.add_room("0", ["1"], "", False, False)
        self.world.add_room("1", ["0", "2", "3"], "", False, False)
        self.world.add_room("2", ["1", "5"], "", False, False)
        self.world.add_room("3", ["1", "4"], "", False, False)
        self.world.add_room("4", ["3", "6"], "", False, False)
        self.world.add_room("5", ["2", "6"], "", False, False)
        self.world.add_room("6", ["5","4","7"], "", False, False)
        self.world.add_room("7", ["6"], "", False, True)



        while True:
            self.world.rooms[self.Walker.room].describeRoom()
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
                                print("You entered room " + room + ".\n")
                                foundRoom = True
                    i += 1
                if foundRoom == False:
                    print("Input is not valid")
                else:
                    if  self.world.rooms[self.Walker.room].finalRoom == True:
                        print("You find ")
                        
                        self.world.rooms[0].addConnection()
                    break



class Room:
    def __init__(self, name, connections, item, containsEnmeny, finalRoom):
        self.name = name
        self.connections = connections
        self.item = item
        self.containsEnmeny = containsEnmeny
        self.finalRoom = finalRoom

    def describeRoom(self):
        print("You enter the room and look around you.")
        print("there are " + str(len(self.connections) - 1) + " new doors.")
        if self.item == "":
            print("You look further and find no items.\n")
        else:
            print("You look further and see an object. You decide to pick it up")
            print("Item found: " + self.item + "\n")

    def addConnection(self, connection):
        print("You hear a rumble coming from the entrance.")
        self.connections.append(connection)

game = Controller()
game.play_game()