import json
from random import *
from typing import Tuple
from Player import *
from Enemy import *

def get_target(targets):
    while True:
        print("---------------------------------")
        print("Pick a target:")
        for target in targets:
            print(f"{target.name}")
        print("---------------------------------")                        
        target_choice = input(f"input: ")
        for target in targets:
            if target_choice == target.name:
                return target
        print("invalid input")

def print_battle_status(enemies, players):
    name_line = ""
    health_line = ""
    combat_power_line = ""
    if len(enemies) >= 2:
        borderline = "=" * (len(enemies) * 27 - 1)
    else:
        borderline = "=" * (54 - 1)
    print(borderline)
    for enemy in enemies:
        if enemy.status == True:
            healthbar = round(enemy.health/enemy.max_health * 20)
            name_line += enemy.name + " " * (27 - len(enemy.name))
            health_line += str(enemy.health).zfill(2) + "/" + str(enemy.max_health) + " " + "|" * healthbar +"-" * (20 - healthbar) + " "
    print(name_line)
    print(health_line)
    print("\n" * 2)

    name_line = ""
    health_line = ""
    for player in players:
        healthbar = round(player.health/player.max_health * 20)
        health_line += str(player.health).zfill(2) + "/" + str(player.max_health) + " " + "|" * (healthbar) + "-" * (20 - healthbar) + " "
        name_line += player.name + " " * (27 - len(player.name))
        combat_power_bar = round(player.combat_power/player.max_combat_power * 20)
        combat_power_line += str(player.combat_power).zfill(2) + "/" + str(player.max_combat_power) + " " + "|" * (combat_power_bar) + "-" * (20 - combat_power_bar) + " "
    print(name_line)
    print(health_line)
    print(combat_power_line)
    print(borderline)

def get_enemies(room):
    battle_enemies = []
    i = 0
    with open("JSON/Enemies.json", "r") as f:
        enemy_list = json.load(f)
    for room_enemy in room.enemies:
        i += 1
        for list_enemy in enemy_list:
            if list_enemy["name"] == room_enemy:
                if room_enemy ==  "Firewing Wyvern":
                    battle_enemies.append(Boss(list_enemy["name"] + str(i), list_enemy["max_health"], list_enemy["attack_damage"], list_enemy["defence"], list_enemy["magic_defence"], list_enemy["attack_sort"]))    
                else:
                    battle_enemies.append(Enemy(list_enemy["name"] + str(i), list_enemy["max_health"], list_enemy["attack_damage"], list_enemy["defence"], list_enemy["magic_defence"], list_enemy["attack_sort"]))
    return battle_enemies

def start_battle(players, mover):
    turn_conter = 0
    enemies = get_enemies(mover.current_room) #load enemies
    battle = True
    #BEGIN BATTLE
    while battle:
        turn_conter += 1
        guarding = False
        #PLAYER TURN
        for player in players:
            print_battle_status(enemies, players)
            if player.combat_power < 10:
                while (action := get_action(player)) not in ("1", "3"):
                    if action == "2":
                        print("Not enough combat power")
                    else:
                        print("Invalid input")    
            else:
                while (action := get_action(player)) not in ("1", "2", "3"):
                    print("Invalid input") 
            if action == "1": #basic attack
                target = get_target(enemies)
                damage = player.calculate_damage()
                target.receive_damage(damage, player.attack_sort)
            elif action == "2": #special attack/craft
                craft = player.special_attack()
                if craft == "1":
                    for enemy in enemies:
                        damage = player.calculate_damage(0.8)
                        enemy.receive_damage(damage, player.attack_sort)
                elif craft == "2":
                    target = get_target(enemies)
                    damage = player.calculate_damage(2.0)
                    target.receive_damage(damage, player.attack_sort)
                elif craft == "3":
                    if player.name == players[0].name:
                        guarding = True
                    else:
                        target = get_target(players)
                        target.increase_health(15)  
                elif craft == "S":
                    damage = player.calculate_damage(3.0)
                    for enemy in enemies:
                        enemy.receive_damage(damage, player.attack_sort)
            elif action == "3":
                if mover.check_for_usable_items("battle") == True:
                    mover.use_item(players, "battle")
                else:
                    print("You have no usable items")
            else:
                print("GAME: That is not a valid input")

            enemies = remove_dead_enemies(enemies)
            if len(enemies) == 0:
                battle = False
                return
        
        
        #ENEMY TURN
        print_battle_status(enemies, players)
        for enemy in enemies:
            if enemy.name == "Firewing wyvern":
                boss_turn(enemies[0], players)
            elif enemy.status == True:
                target = choice(players)
                print(f"{enemy.name} attacked {target.name}.")
                damage = enemy.calculate_damage()
                target.receive_damage(damage, enemy.attack_sort, guarding)                    

def get_action(player):
    print(f"What will {player.name} do?")
    print("(1)Attack")
    print("(2)Craft") 
    print("(3)Item")
    action = input("input: ")
    return action

def boss_turn(boss, players):
    if boss.charging_attack == True:
        for player in players:
            print(f"{boss.name} attacked {player.name}.")
            damage = boss.calculate_damage(1.8)
            player.receive_damage(damage,boss.attack_sort)
        boss.charging_attack = False
    boss_action = choice(boss.actions)
    print(boss_action)
    if boss_action == "singel_attack":
        target = choice(players)
        damage = boss.calculate_damage()
        print(f"{boss.name} attacked {target.name}.")
        target.receive_damage(damage, boss.attack_sort)
    elif boss_action == "multi_attack":
        for player in players:
            print(f"{boss.name} attacked {player.name}.")
            damage = boss.calculate_damage(0.75)
            player.receive_damage(damage, boss.attack_sort)
    elif boss_action == "change_attack_sort":
        if boss.attack_sort == "physical":
            boss.attack_sort = "magical"
        else:
            boss.attack_sort = "physical"
        boss_turn(boss, players)
    elif boss_action == "change_resistance":
        storage = boss.defence
        boss.defence = boss.magic_defence
        boss.magic_defence = storage
        boss_turn(boss, players)
    elif boss_action == "charge_attack":
        boss.charging_attack = True
    
def remove_dead_enemies(enemies):
    new_enemy_list = []
    for enemy in enemies:
        if enemy.status == True:
            new_enemy_list.append(enemy)
    return new_enemy_list