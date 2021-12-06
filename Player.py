from math import fabs
from random import *

class Player():
    def __init__(self, name, attack_sort, max_health, attack_damage, defence, magic_defence, guarding = False, combat_power = 99, max_combat_power = 99):
        self.name = name
        self.attack_sort = attack_sort
        self.max_health = max_health
        self.health = max_health
        self.attack_damage = attack_damage
        self.defence = defence
        self.magic_defence = magic_defence
        self.guariding = guarding
        self.combat_power = combat_power
        self.max_combat_power = max_combat_power

    def increase_health(self, healing_points):
        self.health += healing_points
        if self.health > self.max_health:
            self.health = self.max_health

    def increase_combat_power(self, combat_points):
        self.combat_power += combat_points
        if self.combat_power > self.max_combat_power:
            self.combat_power = self.max_combat_power

    def calculate_damage(self, multiplier = 1):
        standard_damage = self.attack_damage * multiplier         
        true_damage = round(standard_damage * (randrange(8, 12, 1) / 10)) 
        self.combat_power += round(true_damage * 0.8)
        if self.combat_power > self.max_combat_power:
            self.combat_power = self.max_combat_power
        return true_damage
    
    def receive_damage(self, true_damage, attack_sort):
        if attack_sort == "phisical":
            damage_received = round(true_damage * self.defence)
        else:
            damage_received = round(true_damage * self.magic_defence)
        self.health -= damage_received
        if self.health  <= 0:
            print(f"{self.name} took {self.health + damage_received} damage and died")
            print("|-------------------------------------------------------------------|")
            print("|                      GAME            OVER                         |")
            print("|-------------------------------------------------------------------|")
            exit()
        else:
            self.combat_power += round(damage_received * 0.8)
            if self.combat_power > self.max_combat_power:
                self.combat_power = self.max_combat_power
            print(f"{self.name} took {damage_received} damage and has {self.health} health left")
    
    def special_attack(self):
        while True:
            print("Cp: " + str(self.combat_power) + "/" + str(self.max_combat_power))
            if self.combat_power < 10:
                print("You don't have enough combat power to do a craft.")
                return False
            if self.name == "Joshua":
                print("Crafts:")
                print("(1)Blitz Assault     - attack all enemies at increadible speed       | 20cp")
                print("(2)Heavy Impact      - attack one enemy with an powerful strike      | 30cp")
                print("(3)Guard             - protect ally and reduce incoming damage       | 10cp")
                print("(S)Termination Slash - slash all enmies with extreme power and focus | 99cp")
            else:
                print("Crafts:")
                print("(1)Crystal Volley - summon a wave of crystals shards to attack all enemies          | 20cp")
                print("(2)Stone Bullet   - create a sharp stone and launch it at an enemy with great speed | 30cp")
                print("(3)Heal           - heal an ally for 15 health                                      | 10cp")
                print("(S)Dark Matter    - summon a dark orb that puts imense pressure on all enemies      | 99cp")
            craft = input("Input(Q to cancel): ")

            if craft == "1" and self.combat_power < 20 or craft == "2" and self.combat_power < 30 or craft == "S" and self.combat_power < 99:
                print("You do not have enough compat power for that craft.\n")
            elif craft == "Q":
                return False
            else:
                if craft == "1":
                    self.combat_power -= 20
                    return craft
                elif craft == "2":
                    self.combat_power -= 30
                    return craft
                elif craft == "3":
                    self.combat_power -= 10
                    return craft
                elif craft == "S": 
                    self.combat_power -= 99
                    return craft
                else:
                    print("That is not a valid input")

class Mover():
    def __init__(self, current_room, items = []):
        self.current_room = current_room
        self.items = items
    
    def pick_up_items(self, room):
        for item in room.items:
            self.items.append(item)
        return []

    def check_for_usable_items(self, location):
        for item in self.items:
            for setting in item.usable:
                if setting == location:
                    return True
        return False

    def print_items(self, location):
        print("Backpack: ")
        if location == "battle":
            for item in self.items:
                for setting in item.usable:
                    if setting == "battle":
                        print(f"{item.name} - {item.description}")
        else:           
            for item in self.items:
                for setting in item.usable:
                    if setting == "world":
                        print(f"{item.name} - {item.description}")
 
    def goto_room(self, room):
        #change player room
        self.current_room = room

    def use_item(self, players, location):
        while True:
            self.print_items(location)
            if(item := get_item_input(self, location)) != False:
                break
            print("Invalid input")
        if item.name == "lesser healing potion" or item.name  == "greater healing potion" or item.name  == "lesser combat potion" or item.name  == "greater combat potion":
            while True:
                if(player := get_player_input(players)) != False:
                    break
                print("input is invalid")
            if item.name  == "lesser healing potion":
                player.increase_health(15)

            elif item.name  == "greater healing potion":
                player.increase_health(25)

            elif item.name  == "lesser combat potion":
                player.increase_combat_power(40)
                
            else:
                player.increase_combat_power(80)
            self.items.remove(item)
        #self.remove_item(item)
            print("test")
    
    # def remove_item(self, item):
    #     for player_item in self.items:
    #         if player_item.name == item:
                

        # elif item.name == "flash stone":
        
def get_player_input(players):
    print("Who do you want to use this item on")
    for player in players:
        print(f"{player.name} - {player.health}/{player.max_health}HP - {player.combat_power}/{player.max_combat_power}CP")
    target = input("input: ")

    for player in players:
        if player.name == target:
            return player
    return False

def get_item_input(self, location):
    print("Which item do you want to use?")
    item = input("input: ")

    for player_item in self.items:
        for setting in player_item.usable:
            if player_item.name == item and setting == location:
                return player_item
    return False