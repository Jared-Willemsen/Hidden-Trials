from Room import *

class World:
    def __init__(self, rooms):
        self.rooms = rooms

    def first_room(self):
        self.rooms.append(Room("0", ["1"], [0], False, False))
    
    def add_room(self, name, connections, item, contains_enemy, final_room, unlock_connection):
        self.rooms.append(Room(name, connections, item, contains_enemy, final_room, unlock_connection))

    def room_amount(self):
        print(len(self.rooms))
    
    def make_world(self):
        self.add_room("0", ["1"], "", False, False, "")
        self.add_room("1", ["0", "2", "3"], "", False, False, "")
        self.add_room("2", ["1", "5"], "", False, False, "")
        self.add_room("3", ["1", "4"], "", False, False, "")
        self.add_room("4", ["3", "6"], "", False, False, "")
        self.add_room("5", ["2", "6"], "", False, False, "")
        self.add_room("6", ["5","4","7"], "", False, False, "")
        self.add_room("7", ["6"], "", False, True, "8")

        self.add_room("8", ["0"], "", False, False, "")

