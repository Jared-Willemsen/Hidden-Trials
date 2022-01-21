from math import *
from random import *

class Player():
    def __init__(self, name, attack_sort, max_health, health, attack_power, defence, magic_defence, weapon,  armour, combat_power, max_combat_power):
        self.name = name
        self.attack_sort = attack_sort
        self.max_health = max_health
        self.health = health
        self.attack_power = attack_power
        self.defence = defence
        self.magic_defence = magic_defence
        self.weapon = weapon
        self.armour = armour
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
        standard_damage = self.attack_power * multiplier         
        true_damage = round(standard_damage * (randrange(8, 12, 1) / 10)) 
        self.combat_power += round(true_damage * 0.8)
        if self.combat_power > self.max_combat_power:
            self.combat_power = self.max_combat_power
        print(true_damage)
        return true_damage
    
    def receive_damage(self, true_damage, attack_sort, guarding):
        if guarding == True:
            true_damage /= 2
        if attack_sort == "physical":
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
        while (craft := get_special_attack_input(self)) == False:
            print("invalid input")
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
                
def get_special_attack_input(player):
    print("Cp: " + str(player.combat_power) + "/" + str(player.max_combat_power))
    if player.name == "Joshua":
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
    craft = input("Input: ")

    if craft == "1" and player.combat_power < 20 or craft == "2" and player.combat_power < 30 or craft == "S" and player.combat_power < 99:
        return False
    return craft

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
        for item in self.items:
            item.print_item(location)
 
    def goto_room(self, room):
        #change player room
        self.current_room = room

    def use_item(self, players, location):
        while True:
            self.print_items(location)
            if(item := get_item_input(self, location)) != False:
                break
            print("Invalid input")
        if item.name == "Lesser healing potion" or item.name  == "Greater healing potion" or item.name  == "Lesser combat potion" or item.name  == "Greater combat potion":
            while True:
                if(player := get_player_input(players)) != False:
                    break
                print("input is invalid")
            if item.name  == "Lesser healing potion" or item.name  == "Greater healing potion":
                player.increase_health(item.potency)
                
            elif item.name  == "Lesser combat potion" or item.name  == "Greater combat potion":
                player.increase_combat_power(item.potency)
            
        elif item.name == "Training sword" or item.name == "Saber" or item.name == "Tachi":
            players[0].attack_power = item.potency
            self.items.append(players[0].weapon)
            players[0].weapon = item
            
        elif item.name == "Wooden staff" or item.name == "Ruby staff" or item.name == "Moon staff":
            players[1].attack_power = item.potency
            self.items.append(players[1].weapon)
            players[1].weapon = item

        elif item.name == "Leather gear" or item.name == "Knights armour" or item.name == "Dragonscale armour":
            players[0].defence = item.potency
            players[0].magic_defence = item.potency
            self.items.append(players[0].armour)
            players[0].armour == item 
        
        elif item.name == "Leather halfrobe" or item.name == "Mage robe" or item.name == "Aetherial robe":
            players[1].defence = item.potency - 0.2
            players[1].magic_defence = item.potency
            self.items.append(players[1].armour) 
            players[1].armour == item

        self.items.remove(item)
        
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
    item_input = input("input: ")

    for item in self.items:
        if item.check_item(item_input, location):
            return item
    return False