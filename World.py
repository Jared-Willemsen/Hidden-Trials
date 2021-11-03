import json
from Room import *

class World:
    def __init__(self, _rooms):
        self.rooms = _rooms

    def first_room(self):
        for room in self.rooms:
            if room.first_room == True:
                return room        
    
    def add_room(self, name, connections, item, contains_enemy, first_room, boss_room, unlock_connection):
        self.rooms.append(Room(name, connections, item, contains_enemy, first_room, boss_room, unlock_connection))

    def room_amount(self):
        print(len(self.rooms))
    
    def make_world(self):
        #read world from JSON file 
        with open("World1.json", "r") as f:
            world = json.load(f)
        for dict in world:
            room = list(dict.values())
            self.add_room(room[0], room[1], room[2], room[3], room[4], room[5], room[6])
        
        #change connection and unluck_connection strings to pointers
        for room in self.rooms:
            for connection in range(len(room.connections)):
                for i in range(len(self.rooms)):
                    if self.rooms[i].name == room.connections[connection]:
                        room.connections[connection] = i

            for connection in range(len(room.unlock_connection)):
                for i in range(len(self.rooms)):
                    if self.rooms[i].name == room.unlock_connection[connection]:
                        room.unlock_connection[connection] = i


