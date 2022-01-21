from random import *

class Enemy:
    def __init__(self, name, max_health, attack_power, defence, magic_defence, attack_sort):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.attack_power = attack_power
        self.defence = defence
        self.magic_defence = magic_defence
        self.attack_sort = attack_sort
        self.status = True

    def calculate_damage(self, multiplier = 1):
        standard_damage = self.attack_power * multiplier         
        true_damage = round(standard_damage *  (randrange(8, 12, 1) / 10))
        return true_damage

    def receive_damage(self, true_damage, attack_sort):
        if attack_sort == "physical":
            damage_received = round(true_damage * self.defence)
        else:
            damage_received = round(true_damage * self.magic_defence)
        self.health -= damage_received
        if self.health <= 0:
            print(f"{self.name} took {self.health + damage_received} damage and died.")
            self.status = False
        else:
            print(f"{self.name} took {damage_received} damage and has {self.health} health left.")
        return damage_received

class Boss(Enemy):
    def __init__(self, name, max_health, attack_power, defence, magic_defence, attack_sort):
        super().__init__(name, max_health, attack_power, defence, magic_defence, attack_sort)
        self.charging_attack = False
        self.actions = ["singel_attack", "multi_attack", "change_attack_sort", "change_resistance", "charge_attack"]
    
    def change_attack_sort(self):
        if self.attack_sort == "Physical":
            self.attack_sort == "Magical"
        else:
            self.attack_sort == "Physical"
        
    

    

