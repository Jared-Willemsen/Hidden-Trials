import json
from marshal import load
from time import *
from tkinter import W
from World import *
from Player import *
from Enemy import *
from Item import *
from Battle import start_battle

class Controller:
    def __init__(self):
        self.world = World([])
        self.players = []
        self.mover = Mover(0)
    
    def play_game(self):
        while (new_or_loaded_game := start_game()) not in ("New Game", "Load Game"):
            print("Invalid input")
        #load the world and players depending on if you start a new game or load a game
        self.world.make_world(new_or_loaded_game)
        self.load_players(new_or_loaded_game)

        # this is the only while true since after this the game will continue until you either die or finish the game in both cases the program will quit
        while True:
            #gets an input for the player action: player can move to another room (0), use an item (1) or save the game (2)   
            while (action_input := get_action_input(self.mover.current_room, self.world.get_first_room())) not in ("0", "1", "2"):
                print("Invalid input")
            if action_input == "0":
                #gets an input to move to another room 
                while (next_room := get_room_input(self.world, self.mover)) == False:     
                    print("Invalid input")      
                self.mover.current_room = next_room
                #start a battle if there are enemies
                if self.mover.current_room.enemies != []:
                    start_battle(self.players, self.mover)
                    self.mover.current_room.enemies = []
                    # if the battle was the boss battle it ends the game
                    if self.mover.current_room.boss_room == True:
                        print("Thank you for playing my game :)")
                        exit()
                #search the room
                self.mover.current_room.search_room()
                #transfer items from room to player
                self.mover.current_room.items = self.mover.pick_up_items(self.mover.current_room)
                #add new link if there is one
                self.world.create_new_link(self.mover.current_room.unlock_connection)
                    
            elif action_input == "1":
                #checks if the player has any usable items
                if self.mover.check_for_usable_items("world") == True:
                    self.mover.use_item(self.players, "world") #function for using an item
                else:
                    print("You have no usable items")
            elif action_input == "2":
                #saves the game
                self.world.save_world()
                self.save_players()
                print("Game is saved\n")
    
    def save_players(self):
        # all this is basically changing class abjects into dictionaries so it can be saved in a JSON file
        players1_info = {"health":self.players[0].health, "weapon":self.players[0].weapon.name, "armour":self.players[0].armour.name, "combat_power":self.players[0].combat_power}
        players2_info = {"health":self.players[1].health, "weapon":self.players[1].weapon.name, "armour":self.players[1].armour.name, "combat_power":self.players[1].combat_power}
        player_items = []
        for player_item in self.mover.items:
            player_items.append(player_item.name)
        for i in range(len(self.world.rooms)):
            if self.world.rooms[i].name == self.mover.current_room.name:
                room_pointer = i
        players_info = [players1_info, players2_info, player_items, room_pointer]    
        with open("JSON/SavedPlayers.json", "w") as f:
            json.dump(players_info, f)
        


    def load_players(self, new_or_loaded_game):
        if new_or_loaded_game == "New Game":
            with open("JSON/NewPlayers.json", "r") as f: #this file contains data for the players if the world us new
                players_info = json.load(f)
        else:
            with open("JSON/SavedPlayers.json", "r") as f: # this file contains saved player data
                players_info = json.load(f)
        player1 = players_info[0]
        player2 = players_info[1]
        # this changes player equipment for dictionaries back to item objects
        player1["weapon"] = translate_equipment(player1["weapon"]) 
        player1["armour"] = translate_equipment(player1["armour"])
        player2["weapon"] = translate_equipment(player2["weapon"])
        player2["armour"] = translate_equipment(player2["armour"])
        #makes player abjects with data form JSON file
        self.players.append(Player("Joshua", "physical", 30, player1["health"], player1["weapon"].potency, player1["armour"].potency, player1["armour"].potency, player1["weapon"], player1["armour"], player1["combat_power"], 99))
        self.players.append(Player("Lillian", "magical", 30, player2["health"], player2["weapon"].potency, player2["armour"].potency, player2["armour"].potency - 0.2, player2["weapon"], player2["armour"], player2["combat_power"], 99))
        
        if new_or_loaded_game == "Load Game": #changes rest of items to item objects if world was loaded
            with open("JSON/Items.json", "r") as f:
                item_list = json.load(f)
            for player_item in players_info[2]:
                for item in item_list:
                    if player_item == item["name"]:
                        self.mover.items.append(Item(item["name"], item["usable"], item["description"], item["potency"]))
            self.mover.current_room = self.world.rooms[players_info[3]] # places player in room that was saved
        else:
            self.mover.current_room = self.world.get_first_room() # places player in the first room
        


def translate_equipment(equipment): # changes item dictionaries to item objects
    with open("JSON/Items.json", "r") as f:
        item_list = json.load(f)
    for item in item_list:
        if item["name"] == equipment:
            return Item(item["name"], item["usable"], item["description"], item["potency"])
    print("item not found")
    

# the rest if just for inputs
def get_action_input(current_room, first_room):
    print("Actions: ")
    print("(0)Move")
    print("(1)Use item")
    print("(2)Save")
    action_input = input("Intput: ")
    return action_input

def get_room_input(world, mover):
    # ask user for room input
    print(f"\x1B[3mYou are currently in room {mover.current_room.name} Where do you wish to move.\x1B[0m")
    for room in mover.current_room.connections: 
        print(f"Room {world.rooms[room].name}")
    room_input = input("input: Room ")
    
    #validate user input 
    for connection in mover.current_room.connections:
        if room_input == world.rooms[connection].name:
            return world.rooms[connection] # return room abject of chosen room
    return False

def start_game():
    print("Hidden Trails")
    print("New Game")
    print("Load Game")
    world_input = input("Input: ")
    return world_input

                
            
