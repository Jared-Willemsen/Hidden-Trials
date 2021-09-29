from World import *
from Player import *

class Controller:
    def __init__(self):
        self.world = World([])
        self.Walker = Player(0)
    
    def play_game(self):
        self.world.make_world()
        self.Walker.current_room = self.world.first_room()
        while True:
            print("You are currently in room " + self.Walker.current_room.name + " Where do you wish to move.")
            for room in self.Walker.current_room.connections:
                print("Room " + room)
            connection_not_found = True
            while connection_not_found:
                user_input = input("input: Room ")
                for room in self.world.rooms:
                    if user_input == room.name:
                        if self.Walker.goto_room(room, user_input) == True:
                            connection_not_found = False
                            break

    
