from random import *

class Enemy:
    def __init__(self, _name, _max_health, _attack_damage, _defence, _magic_defence, _attack_sort, _status = True):
        self.name = _name
        self.max_health = _max_health
        self.health = _max_health
        self.attack_damage = _attack_damage
        self.defence = _defence
        self.magic_defence = _magic_defence
        self.attack_sort = _attack_sort
        self.status = _status

    def calculate_damage(self, multiplier = 1):
        standard_damage = self.attack_damage * multiplier
        print(standard_damage)         
        true_damage = round(standard_damage *  (randrange(8, 12, 1) / 10))
        print(true_damage)
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

