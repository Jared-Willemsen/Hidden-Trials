class Room:
    def __init__(self, _name, _connections, _item, _contains_enemy, _first_room, _boss_room, _unlock_connection):
        self.name = _name
        self.connections = _connections
        self.item = _item
        self.contains_enemy = _contains_enemy
        self.first_room = _first_room
        self.boss_room = _boss_room
        self.unlock_connection = _unlock_connection

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
        
        if self.item == "":
            print("You search around the room but find no items.\n")
        else:
            print("You search around the room and find something. You decide to pick it up")
            print(f"Item found: {self.item}\n")

    def add_connection(self, room, rooms):
        room.connections.append(rooms[0])
        self.connections.append(rooms[1])
