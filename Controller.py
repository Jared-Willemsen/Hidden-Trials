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
        #load the world
        self.world.make_world(new_or_loaded_game)
        self.load_players(new_or_loaded_game)

        while (playing := True):
            while (action_input := get_action_input(self.mover.current_room, self.world.get_first_room())) not in ("0", "1", "2"):
                print("Invalid input")
            if action_input == "0":
                while (room_input := get_room_input(self.world, self.mover)) == False:     
                    print("Invalid input")      
                self.mover.goto_room(room_input)
                #start a battle if there are enemies
                if self.mover.current_room.enemies != []:
                    start_battle(self.players, self.mover)
                    self.mover.current_room.enemies = []
                    if self.mover.current_room.boss_room == True:
                        print("Thank you for playing my game :)")
                        break
                #search the room
                self.mover.current_room.search_room()
                #transfer items from room to player
                self.mover.current_room.items = self.mover.pick_up_items(self.mover.current_room)
                #add new link if there is one
                self.world.create_new_link(self.mover.current_room.unlock_connection)
                    
            elif action_input == "1":
                if self.mover.check_for_usable_items("world") == True:
                    self.mover.use_item(self.players, "world")
                else:
                    print("You have no usable items")
            elif action_input == "2":
                self.players[0].health == self.players[0].max_health
                self.players[1].health == self.players[1].max_health
                self.world.save_world()
                self.save_players()
    
    def save_players(self):
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
            with open("JSON/NewPlayers.json", "r") as f:
                players_info = json.load(f)
        else:
            with open("JSON/SavedPlayers.json", "r") as f:
                players_info = json.load(f)
        player1 = players_info[0]
        player2 = players_info[1]
        player1["weapon"] = translate_equipment(player1["weapon"])
        player1["armour"] = translate_equipment(player1["armour"])
        player2["weapon"] = translate_equipment(player2["weapon"])
        player2["armour"] = translate_equipment(player2["armour"])

        self.players.append(Player("Joshua", "physical", 30, player1["health"], player1["weapon"].potency, player1["armour"].potency, player1["armour"].potency, player1["weapon"], player1["armour"], player1["combat_power"], 100))
        self.players.append(Player("Lillian", "magical", 30, player2["health"], player2["weapon"].potency, player2["armour"].potency, player2["armour"].potency - 0.2, player2["weapon"], player2["armour"], player2["combat_power"], 100))

        with open("JSON/Items.json", "r") as f:
            item_list = json.load(f)
        if new_or_loaded_game == "Load Game":
            for player_item in players_info[2]:
                for item in item_list:
                    if player_item == item["name"]:
                        self.mover.items.append(Item(item["name"], item["usable"], item["description"], item["potency"]))
            self.mover.current_room = self.world.rooms[players_info[3]]
        else:
            self.mover.current_room = self.world.get_first_room()
        


def translate_equipment(equipment):
    with open("JSON/Items.json", "r") as f:
        item_list = json.load(f)
    for item in item_list:
        if item["name"] == equipment:
            return Item(item["name"], item["usable"], item["description"], item["potency"])
    print("item not found")
    

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
            return world.rooms[connection]
    return False

def start_game():
    print("Hidden Trails")
    print("New Game")
    print("Load Game")
    world_input = input("Input: ")
    return world_input
    


def intro_text():
    print("yay")

                
            
