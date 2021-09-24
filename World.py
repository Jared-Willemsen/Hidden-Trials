class World:
    def __init__(self, rooms):
        self.rooms = rooms

    def first_room(self):
        self.rooms.append(Room("0", ["1"], [0], False, False))
    
    def add_room(self, name, connections, item, containsEnemy, finalRoom):
        self.rooms.append(Room(name, connections, item, containsEnemy, finalRoom))

    def room_amount(self):
        print(len(self.rooms))