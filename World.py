import json
from Item import *
from Room import *

class World:
    def __init__(self, rooms):
        self.rooms = rooms

    def get_first_room(self):
        for room in self.rooms:
            if room.first_room == True:
                return room        
    
    def add_room(self, name, connections, item, enemies, unlock_connection, first_room, boss_room):
        self.rooms.append(Room(name, connections, item, enemies, unlock_connection, first_room, boss_room))

    def room_amount(self):
        print(len(self.rooms))
    
    def create_new_link(self, new_connections):
        for room_1 in new_connections:
            for room_2 in new_connections:
                if room_1 != room_2:
                    self.rooms[room_1].add_connection(room_2)

    
    def make_world(self, world_input):
        #read from JSON
        if world_input == "New Game":
            file = "JSON/NewWorld.json" 
        else:
            file = "JSON/SavedWorld.json"
        with open(file, "r") as f:
            world = json.load(f)

        for room in world:
            #room = list(dict.values())
            self.add_room(room["name"], room["connections"], room["items"], room["enemies"], room["unlock_connection"], room["first_room"], room["boss_room"])
        with open("JSON/Items.json", "r") as f:
            item_list = json.load(f)
        #change connection and unluck_connection strings to pointers
        for room in self.rooms:
            #change item names to objects
            for i in range(len(room.items)):
                for possible_item in item_list:
                    if possible_item["name"] == room.items[i]:
                        room.items[i] = Item(possible_item["name"], possible_item["usable"], possible_item["description"], possible_item["potency"])
            if world_input == "New Game": # it's not necessary to do the next two actions if the world was loaded since the world was saved like that
                #change room names to pointers
                for connection in range(len(room.connections)):
                    for i in range(len(self.rooms)):
                        if self.rooms[i].name == room.connections[connection]:
                            room.connections[connection] = i
                #change unluck_connections to pointers
                for connection in range(len(room.unlock_connection)):
                    for i in range(len(self.rooms)):
                        if self.rooms[i].name == room.unlock_connection[connection]:
                            room.unlock_connection[connection] = i
            
        

                    
    def save_world(self):
        world_in_JSON = []
        for room in self.rooms:
            world_in_JSON.append(room.save_to_JSON())
        with open("JSON/SavedWorld.json", "w") as f:
            json.dump(world_in_JSON, f)


