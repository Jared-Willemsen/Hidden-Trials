from World import *
from Player import *
from Enemy import *
from Battle import start_battle

class Controller:
    def __init__(self):
        self.players = [Player("Joshua", "phisical", 30, 10, 0.4, 0.7), 
                        Player("Lillian", "magical", 30, 10, 0.7, 0.4)]
        self.world = World([])
        self.mover = Mover(0)
    
    def play_game(self):
        #load the world
        self.world.make_world()
        #place the mover in the first room
        self.mover.current_room = self.world.get_first_room()
        playing = True
        while playing:
            while True:
                if (action_input := get_action_input()) in ("0", "1"):
                    break
                print("Invalid input")
            if action_input == "0":
                while True:
                    if (room_input := get_room_input(self.world, self.mover)) != False:
                        break     
                    print("Invalid input")                  
                self.mover.goto_room(room_input)
                #start a battle if there are enemies
                if self.mover.current_room.contains_enemy == True:
                    start_battle(self.players, self.mover)
                #search the room
                self.mover.current_room.search_room()
                #transfer items from room to player
                self.mover.current_room.items = self.mover.pick_up_items(self.mover.current_room)
                #add new link if there is one
                self.world.create_new_link(self.mover.current_room.unlock_connection)
            elif action_input == "1":
                if self.mover.check_for_usable_items("world") == True:
                    self.mover.use_item(self.players, "world")
                else:
                    print("You have no usable items")

def get_action_input():
    print("Actions: ")
    print("(0)Move")
    print("(1)Use item")
    action_input = input("Intput: ")
    return action_input

def get_room_input(world, mover):
    # ask user for room input
    print(f"\x1B[3mYou are currently in room {mover.current_room.name} Where do you wish to move.\x1B[0m")
    for room in mover.current_room.connections:
        print(f"Room {world.rooms[room].name}")
    room_input = input("input: Room ")
    
    #validate user input 
    for connection in mover.current_room.connections:
        if room_input == world.rooms[connection].name:
            return world.rooms[connection]
    return False
    
                    

                
            
