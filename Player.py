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
        # if the player was guarding before the enemy attacks it will reduce the damage by half
        if guarding == True:
            true_damage /= 2
        if attack_sort == "physical": # reduces damage with defence
            damage_received = round(true_damage * self.defence)
        else:
            damage_received = round(true_damage * self.magic_defence)
        self.health -= damage_received
        if self.health  <= 0: # if player health reaches 0 player is dead the user loses and the program is exited  
            print(f"{self.name} took {self.health + damage_received} damage and died")
            print("|-------------------------------------------------------------------|")
            print("|                      GAME            OVER                         |")
            print("|-------------------------------------------------------------------|")
            exit()
        else:
            #increases the combat power by taking damage
            self.combat_power += round(damage_received * 0.8) 
            if self.combat_power > self.max_combat_power:
                self.combat_power = self.max_combat_power
            print(f"{self.name} took {damage_received} damage and has {self.health} health left")
    
    def special_attack(self):
        # gets an input for the special attack and reduces combat power accordingly
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
                
# get input for spocial attack
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
    
    def pick_up_items(self, room): # puts items from the room into this class 
        for item in room.items:
            self.items.append(item)
        return []

    def check_for_usable_items(self, location): # checks if user has any usable items
        for item in self.items:
            for setting in item.usable:
                if setting == location:
                    return True
        return False

    def print_items(self, location): # self explanetory
        print("Backpack: ")
        for item in self.items:
            item.print_item(location)

    def use_item(self, players, location): #uses an item
        while (item := get_item_input(self, location)) == False:
            print("Invalid input")
        if item.name == "Lesser healing potion" or item.name  == "Greater healing potion" or item.name  == "Lesser combat potion" or item.name  == "Greater combat potion":
            while (player := get_player_input(players)) == False:
                print("input is invalid")
            if item.name  == "Lesser healing potion" or item.name  == "Greater healing potion":
                player.increase_health(item.potency)
                
            elif item.name  == "Lesser combat potion" or item.name  == "Greater combat potion":
                player.increase_combat_power(item.potency)

        #checks wich item user chose and takes the required actions    
        elif item.name == "Training sword" or item.name == "Saber" or item.name == "Tachi":
            players[0].attack_power = item.potency
            players[0].weapon = item
            
        elif item.name == "Wooden staff" or item.name == "Ruby staff" or item.name == "Moon staff":
            players[1].attack_power = item.potency
            players[1].weapon = item

        elif item.name == "Leather gear" or item.name == "Knights armour" or item.name == "Dragonscale armour":
            players[0].defence = item.potency
            players[0].magic_defence = item.potency
            players[0].armour == item 
        
        elif item.name == "Leather halfrobe" or item.name == "Mage robe" or item.name == "Aetherial robe":
            players[1].defence = item.potency - 0.2
            players[1].magic_defence = item.potency
            players[1].armour == item
        self.items.remove(item)

# the rest is just asking the user for an input
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
    self.print_items(location)
    print("Which item do you want to use?")
    item_input = input("input: ")

    for item in self.items:
        if item.check_item(item_input, location):
            return item
    return False