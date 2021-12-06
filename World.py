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
    
    def add_room(self, name, connections, item, contains_enemy, first_room, boss_room, unlock_connection):
        self.rooms.append(Room(name, connections, item, contains_enemy, first_room, boss_room, unlock_connection))

    def room_amount(self):
        print(len(self.rooms))
    
    def create_new_link(self, rooms):
        for room in rooms:
            for room1 in rooms:
                if room != room1:
                    room.add_connection(room1)

    
    def make_world(self):
        #read world from JSON file 
        with open("World1.json", "r") as f:
            world = json.load(f)
        for room in world:
            #room = list(dict.values())
            self.add_room(room["name"], room["connections"], room["items"], room["contains_enemy"], room["first_room"], room["boss_room"], room["unlock_connection"])
        with open("Items.json", "r") as f:
            item_list = json.load(f)
        #change connection and unluck_connection strings to pointers
        for room in self.rooms:
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
            #change itme names to objects
            for i in range(len(room.items)):
                for possible_item in item_list:
                    if possible_item["name"] == room.items[i]:
                        room.items[i] = Item(possible_item["name"], possible_item["usable"], possible_item["description"])


