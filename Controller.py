from typing import Tuple
from World import *
from Player import *
from Enemy import *

class Controller:
    def __init__(self):
        self.world = World([])
        self.Lillian = Player()
        self.Walker = Walker(0)
    
    def play_game(self):
        self.world.make_world()
        self.Walker.current_room = self.world.first_room()
        while True:
            #show player where they can move to 
            print("You are currently in room " + self.Walker.current_room.name + " Where do you wish to move.")
            for room in self.Walker.current_room.connections:
                print("Room " + self.world.rooms[room].name)
            
            #MOVING
            connection_not_found = True
            while connection_not_found:
                #get room input
                user_input = input("input: Room ")
                
                #try to move to room
                for connection in self.Walker.current_room.connections:
                    if user_input == self.world.rooms[connection].name:
                        self.Walker.goto_room(self.world.rooms[connection])
                        if self.Walker.current_room.contains_enemy == True:
                            self.enemy_battle()
                        self.Walker.current_room.search_room()
                        if self.Walker.current_room.unlock_connection != []:
                            self.world.rooms[self.Walker.current_room.unlock_connection[0]].add_connection(self.world.rooms[self.Walker.current_room.unlock_connection[1]], self.Walker.current_room.unlock_connection)
                            self.Walker.current_room.unlock_connection = []
                        connection_not_found = False
                        break
                if connection_not_found == True:   
                    print("Input is not valid")
    
    def enemy_battle(self):
        enemies = []
        


    
