from World import *
from Player import *

class Controller:
    def __init__(self):
        self.world = World([])
        self.Walker = Player(0)
    
    def play_game(self):
        self.world.make_world()
        while True:
            print("You are currently in room " + self.world.rooms[self.Walker.room].name + " Where do you wish to move.")
            for room in self.world.rooms[self.Walker.room].connections:
                print("Room " + room)
            while True:
                user_input = input("input: Room ")
                i = 0
                found_room = False
                for room in self.world.rooms: 
                    if user_input == room.name:
                        for room in self.world.rooms[self.Walker.room].connections:
                            if  user_input == room:
                                self.Walker.room = i
                                print("")
                                print("You entered room " + room + ".\n")
                                found_room = True
                    i += 1
                if found_room == False:
                    print("Input is not valid")
                else:
                    self.world.rooms[self.Walker.room].search_room()
                    
                    if self.world.rooms[self.Walker.room].final_room == True:
                        self.world.rooms[0].add_connection(self.world.rooms[self.Walker.room].unlock_connection)
                    break

game = Controller()
game.play_game()