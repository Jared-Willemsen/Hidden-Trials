class Room:
    def __init__(self, name, connections, item, contains_enmeny, final_room, unlock_connection):
        self.name = name
        self.connections = connections
        self.item = item
        self.contains_enmeny = contains_enmeny
        self.final_room = final_room
        self.unclock_connection = unlock_connection

    def search_room(self):
        print("You enter the room and look around you.\n")
        
        if len(self.connections) - 1 == 0:
            print("there are no other entrances\n")
        elif len(self.connections) - 1 == 1:
            print("There is one other entrance\n")
        else:
            print("there are " + str(len(self.connections) - 1) + " other entrances.\n")

        if self.final_room == True:
            print("You find a big lever at the back wall. You walk over to it and flip it")
            print("You hear a rumble coming from the entrance.\n")
        
        if self.item == "":
            print("You search around the room but find no items.\n")
        else:
            print("You search around the room and find something. You decide to pick it up")
            print("Item found: " + self.item + "\n")

    def add_connection(self, connection):
        self.connections.append(connection)