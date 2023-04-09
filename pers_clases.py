from weapons import *

def class_choice():
    pers_class = input("Выбери класс персонажа (w - воин, a - лучник, z - маг): ")
    pers_level = 1
    if pers_class == 'w':
        class_name = 'warrior'
    if pers_class == 'a':
        class_name = 'archer'
    if pers_class == 'z':
        class_name = 'wizard'
    weapon = eval(class_name).start_weapon
    max_health = eval(class_name).health
    health = max_health
    endurance = eval(class_name).endurance
    strength = eval(class_name).strength
    dexterity = eval(class_name).dexterity
    intelligence = eval(class_name).intelligence
    return class_name, pers_level, max_health, health, endurance, strength, dexterity, intelligence, weapon


class warrior:
    health = 120
    endurance = 5
    strength = 7
    dexterity = 5
    intelligence = 5
    start_weapon = woodcutter_axe

class archer:
    health = 100
    endurance = 5
    strength = 5
    dexterity = 7
    intelligence = 5
    start_weapon = decrepit_bow

class wizard:
    health = 100
    endurance = 5
    strength = 5
    dexterity = 5
    intelligence = 7
    start_weapon = magic_staff

