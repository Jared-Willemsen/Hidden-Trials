from random import *

class Enemy:
    def __init__(self, name, max_health, attack_damage, defence, magic_defence, attack_sort, status = True):
        self.name = name
        self.max_health = max_health
        self.health = max_health
        self.attack_damage = attack_damage
        self.defence = defence
        self.magic_defence = magic_defence
        self.attack_sort = attack_sort
        self.status = status

    def calculate_damage(self, multiplier = 1):
        standard_damage = self.attack_damage * multiplier         
        true_damage = round(standard_damage *  (randrange(8, 12, 1) / 10))
        return true_damage

    def receive_damage(self, true_damage, attack_sort):
        if attack_sort == "phisical":
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

