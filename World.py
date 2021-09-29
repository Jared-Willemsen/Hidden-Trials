import json
from Room import *

class World:
    def __init__(self, rooms):
        self.rooms = rooms

    def first_room(self):
        for room in self.rooms:
            if room.first_room == True:
                return room        
    
    def add_room(self, name, connections, item, contains_enemy, first_room, boss_room, unlock_connection):
        self.rooms.append(Room(name, connections, item, contains_enemy, first_room, boss_room, unlock_connection))

    def room_amount(self):
        print(len(self.rooms))
    
    def make_world(self):
        with open("World1.json", "r") as f:
            world = json.load(f)
        for dict in world:
            room = list(dict.values())
            self.add_room(room[0], room[1], room[2], room[3], room[4], room[5], room[6])
        
        #for room1 in self.rooms:
        #    for connection in room1.connections:
        #        for room in self.rooms:
        #            if connection == room.name:
        #                connection = room


