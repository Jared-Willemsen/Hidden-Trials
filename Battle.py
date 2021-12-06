import json
from random import *
from Player import *
from Enemy import *

# def check_enemies_status(enemies, players):
#     for enemy in enemies:
#         if enemy.status == True:
#             return True
#     print_battle_status(enemies, players)            
#     print(f"All enemies died {players[0].name} and {players[1].name} won the battle.")
#     return False

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
    print("=" * (len(enemies) * 27 - 1))
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
    print("=" * (len(enemies) * 27 - 1))

def get_enemies():
    enemies = []
    with open("Enemies.json", "r") as f:
        enemy_list = json.load(f)
    enemy = enemy_list[randrange(0, 3, 1)]
    enemy = list(enemy.values())
    enemy_amount = randrange(2, 4, 1)
    for i in range(enemy_amount):
        enemies.append(Enemy(enemy[0] + str(i + 1), enemy[1], enemy[2], enemy[3], enemy[4], enemy[5]))
    return enemies

def start_battle(players, mover):
    turn_conter = 0
    enemies = get_enemies() #load enemies
    battle = True
    #BEGIN BATTLE
    while battle:
        turn_conter += 1
        #PLAYER TURN
        for player in players:
            print("hey")
            player.guarding = False
            print_battle_status(enemies, players)
            while True:
                if (action := get_action(player)) in ("1", "2","3"):
                    break
            if action == "1": #basic attack
                target = get_target(enemies)
                damage = player.calculate_damage()
                target.receive_damage(damage, player.attack_sort)
            elif action == "2": #special attack/craft
                craft = player.special_attack()
                if craft != False:
                    if player.name == players[0].name:
                        if craft == "1":
                            for enemy in enemies:
                                damage = player.calculate_damage(0.8)
                                enemy.receive_damage(damage, player.attack_sort)
                        elif craft == "2":
                            target = get_target(enemies)
                            damage = player.calculate_damage(2.0)
                            target.receive_damage(damage, player.attack_sort)
                        elif craft == "3":
                            player.guarding = True    
                        elif craft == "S":
                            damage = player.calculate_damage(3.0)
                            for enemy in enemies:
                                enemy.receive_damage(damage, player.attack_sort)
                    else:
                        if craft == "1":
                            for enemy in enemies:
                                damage = player.calculate_damage(0.8)
                                enemy.receive_damage(damage, player.attack_sort)
                        elif craft == "2":
                            target = get_target(enemies)
                            damage = player.calculate_damage(2.0)
                            target.receive_damage(damage, player.attack_sort)
                        elif craft == "3":
                            target = get_target(players)
                            target.increase_health(30)
                        elif craft == "S":
                            damage = player.calculate_damage(3.0)
                            for enemy in enemies:
                                enemy.receive_damage(damage, player.attack_sort)
                else:
                    print_battle_status(enemies, players)
            elif action == "3":
                if mover.check_for_usable_items("battle") == True:
                    mover.use_item(players, "battle")
                else:
                    print("You have no usable items")
            else:
                print("GAME: That is not a valid input")
            for enemy in enemies:
                if enemy.status == False:
                    enemies.remove(enemy)
                    
            if len(enemies) <= 0:
                battle = False
                break
        if len(enemies) <= 0:
            battle = False
            break        
        
        #ENEMY TURN
        print_battle_status(enemies, players)
        for enemy in enemies:
            if enemy.status == True:
                if players[0].guarding == True:
                    target = players[0]
                    print(f"{enemy.name} attacked {target.name}.")
                    damage = enemy.calculate_damage(0.5)
                else:
                    target = choice(players)
                    print(f"{enemy.name} attacked {target.name}.")
                    damage = enemy.calculate_damage()
                target.receive_damage(damage, enemy.attack_sort)                    

def get_action(player):
    print(f"What will {player.name} do?")
    print("(1)Attack")
    print("(2)Craft") 
    print("(3)Item")
    action = input("input: ")
    return action

def print_enemies(enemies, x):
    for enemy in enemies:
        print(enemy.name)
        print(x)
