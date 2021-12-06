import json
from Item import *

class Room:
    def __init__(self, name, connections, items, contains_enemy, first_room, boss_room, unlock_connection):
        self.name = name
        self.connections = connections
        self.items = items
        self.contains_enemy = contains_enemy
        self.first_room = first_room
        self.boss_room = boss_room
        self.unlock_connection = unlock_connection

    def search_room(self):
        print(f"\nYou enter room {self.name} and look around you.\n")
        if len(self.connections) - 1 == 0:
            print("There are no other entrances\n")
        elif len(self.connections) - 1 == 1:
            print("There is one other entrance\n")
        else:
            print(f"There are {len(self.connections) - 1} other entrances.\n")
        if self.unlock_connection != []:
            print("You find a big lever at the back wall. You walk over to it and flip it")
            print("You hear a rumble coming from the entrance.\n")        
        if self.items == []:
            print("You search around the room but find no items.\n")
        else:
            for item in self.items:
                print("You search around the room and find something. You decide to pick it up")
                print(f"Item found: {item.name}\n")

    def add_connection(self, room):
        self.connections.append(room)


