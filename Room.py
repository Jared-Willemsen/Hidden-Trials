class Room:
    def __init__(self, name, connections, item, containsEnmeny, finalRoom):
        self.name = name
        self.connections = connections
        self.item = item
        self.containsEnmeny = containsEnmeny
        self.finalRoom = finalRoom

    def describeRoom(self):
        print("You enter the room and look around you.")
        if len(self.connections) - 1 == 1:
            print("There is one new door")
        else:
            print("there are " + str(len(self.connections) - 1) + " new doors.")
        if self.item == "":
            print("You look further and find no items.\n")
        else:
            print("You look further and see an object. You decide to pick it up")
            print("Item found: " + self.item + "\n")

    def addConnection(self, connection):
        print("You hear a rumble coming from the entrance.")
        self.connections.append(connection)