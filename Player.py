from Room import *
from random import *

class Player():
    def __init__(self, _name, _attack_sort, _max_health, _attack_damage, _defence, _magic_defence, _guarding = False, _combat_power = 0, _max_combat_power = 99):
        self.name = _name
        self.attack_sort = _attack_sort
        self.max_health = _max_health
        self.health = _max_health
        self.attack_damage = _attack_damage
        self.defence = _defence
        self.magic_defence = _magic_defence
        self.guariding = _guarding
        self.combat_power = _combat_power
        self.max_combat_power = _max_combat_power
    
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
                print("(1)Blitz Assault     - attack all enemies at increadible speed: 20cp")
                print("(2)Heavy Impact      - attack one enemy with an powerful strike: 30cp")
                print("(3)Guard             - protect ally and reduce incoming damage: 10cp")
                print("(S)Termination Slash - slash all enmies with extreme power and focus: 99cp")
            else:
                print("Crafts:")
                print("(1)Crystal Volley - summon a wave of crystals shards to attack all enemies: 20cp")
                print("(2)Stone Bullet   - create a sharp stone and launch it at an enemy with great speed: 30cp")
                print("(3)Heal           - heal an ally: 10cp")
                print("(S)Dark Matter    - summon a dark orb that puts imense pressure on all enemies: 99cp")
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

class mover():
    def __init__(self, _current_room):
        self.current_room = _current_room
    
    def goto_room(self, room):
        #change player room and describe it
        self.current_room = room
    