import json
from sqlite3 import connect
from Item import *

class Room:
    def __init__(self, name, connections, items, enemies, unlock_connection, first_room, boss_room):
        self.name = name
        self.connections = connections
        self.items = items
        self.enemies = enemies
        self.unlock_connection = unlock_connection
        self.first_room = first_room
        self.boss_room = boss_room

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

    def save_to_JSON(self):
        items_in_JSON = []
        for item in self.items:
            items_in_JSON.append(item.name)

        room_in_JSON = {"name":"", "connections":[], "items":[], "enemies":[], "unlock_connection":[], "first_room":False, "boss_room":False}
        room_in_JSON["name"] = self.name
        room_in_JSON["connections"] = self.connections
        room_in_JSON["items"] = items_in_JSON
        room_in_JSON["enemies"] = self.enemies
        room_in_JSON["unlock_connection"] = self.unlock_connection
        room_in_JSON["first_room"] = self.first_room
        room_in_JSON["boss_room"] = self.boss_room
        return room_in_JSON

    def add_connection(self, room):
        self.connections.append(room)


