from World import *
from Player import *
from Enemy import *
from Battle import *
from Battle import start_battle

class Controller:
    def __init__(self):
        self.players = [Player("Joshua", "phisical", 30, 10, 0.4, 0.7), Player("Lillian", "magical", 30, 10, 0.7, 0.4)]
        self.world = World([])
        self.mover = mover(0)
    
    def play_game(self):
        self.world.make_world()
        self.mover.current_room = self.world.first_room()
        while True:
            #show player where they can move to 
            print(f"\x1B[3mYou are currently in room {self.mover.current_room.name} Where do you wish to move.\x1B[0m")
            for room in self.mover.current_room.connections:
                print(f"Room {self.world.rooms[room].name}")
            
            #MOVING
            connection_not_found = True
            while connection_not_found:
                #get room input
                user_input = input("input: Room ")
                
                #try to move to room
                for connection in self.mover.current_room.connections:
                    if user_input == self.world.rooms[connection].name:
                        self.mover.goto_room(self.world.rooms[connection])
                        #start a battle if there are enemies
                        if self.mover.current_room.contains_enemy == True:
                            start_battle(self.players)
                        #search the room and open new connections if they're there
                        self.mover.current_room.search_room()
                        if self.mover.current_room.unlock_connection != []:
                            self.world.rooms[self.mover.current_room.unlock_connection[0]].add_connection(self.world.rooms[self.mover.current_room.unlock_connection[1]], self.mover.current_room.unlock_connection)
                            self.mover.current_room.unlock_connection = []

                        connection_not_found = False
                        break
                if connection_not_found == True:   
                    print("Input is not valid")