from Room import *

class Player:
    def __init__(self, current_room):
        self.current_room = current_room
    
    def goto_room(self, room, user_input):
        for connection in self.current_room.connections:
            print(connection)
            if  user_input == connection:
                self.current_room = room
                print(self.current_room.name)
                print("")
                print("You entered room " + connection + ".\n")
                self.current_room.search_room()
                return True
        print("Input is not valid")
        return False

                    
                    #if self.Walker.room.unlock_connection != []:
                    #    self.world.rooms[0].add_connection(self.Walker.room)
    