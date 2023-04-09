import random
from pers_clases import *
from levels import *
from weapons import *
from enemies import *
from tablo import *
#import keyboard

def main():
    global pers_level
    global max_health
    global health
    global endurance
    global strength
    global dexterity
    global intelligence
    global weapon
    global points
    global class_name
    global inventory
    load = int(input("0 - Запустить игру с начала, 1 - загрузить сохраненную игру: "))
    if load:
            with open('save.txt', 'r') as data:
                s = data.readline().split()
                class_name, pers_level, max_health, health, endurance, strength, dexterity, intelligence, weapon, points, start_stg, x, y = \
                    s[0], int(s[1]), float(s[2]), float(s[3]), int(s[4]), int(s[5]), int(s[6]), int(s[7]), eval(s[8]),  int(s[9]),  int(s[10]),  int(s[11]),  int(s[12])
    else:
        points, start_stg, x, y = 0, 1, 0, 0
        class_name, pers_level, max_health, health, endurance, strength, dexterity, intelligence, weapon = class_choice()
    inventory = ['health_poison']
    write_pers_characteristics()
    print("Описание:\nСлева на карте обозначено: Y - персонаж, (I | - _) - стены,\n * - ловушки, g,t,B - враги,\n = - дверь на другой уровень")
    print("Справа характеристики персонажа: уровень, шкала здоровья, шкала опыта,")
    print("текущее оружие и его урон")
    move(x, y, start_stg)

def move(x, y, lev):
    b_x = 10
    b_y = 6
    while True:
        part_h = int(health * 10 // max_health)
        h_str = part_h * '█' + (10 - part_h) * '░'
        part_l = int(points * 10 // (50 + pers_level * 30))
        l_str = part_l * '█' + (10 - part_l) * '░'
        if part_h >= 8: face = face_1
        if part_h < 8: face = face_2
        if part_h < 6: face = face_3
        base_damage = weapon.base_damage
        pers_damage = eval(weapon.damage_per_sec)
        if class_name == 'warrior':
            table = [f'|Your level:{pers_level} Stg:{lev}|', \
                       f'|health: {h_str}|', \
                       f'|nxtLvL: {l_str}|', \
                       '|......▀█▄▄▄█▀.....|', \
                       f'|{face}|', \
                       '|....█▄▄▄░░▄▄█.....|', \
                       '|...▄█▀..▀▀..█▄....|', \
                       f'|..{weapon.name + "." * (16 - len(weapon.name))}|', \
                       f'|...damage:{pers_damage}....|', \
                       '|_____██▄__██▄_____|', \
                       ]
        if class_name == 'archer':
            table = [f'|Your level:{pers_level} Stg:{lev}|', \
                       f'|health: {h_str}|', \
                       f'|nxtLvL: {l_str}|', \
                       '|......▄▄███▄▄.....|', \
                       f'|{face}|', \
                       '|.....▄▄▄░░▄▄......|', \
                       '|...▄█...▀▀..█▄....|', \
                       f'|..{weapon.name + "."*(16-len(weapon.name))}|', \
                       f'|...damage:{pers_damage}....|', \
                       '|_____██▄__██▄_____|', \
                       ]
        if class_name == 'wizard':
            table = [f'|Your level:{pers_level} Stg:{lev}|', \
                       f'|health: {h_str}|', \
                       f'|nxtLvL: {l_str}|', \
                       '|........███.......|', \
                       f'|{face}|', \
                       '|...▄▄▄▄▄░░▄▄▄▄....|', \
                       '|...▄█...▀▀..█▄....|', \
                       f'|..{weapon.name + "."*(16-len(weapon.name))}|', \
                       f'|...damage:{pers_damage}....|', \
                       '|_____█▀▄__█▀▄_____|', \
                       ]
        level = eval('level_' + f'{lev}')[:]
        level[y] = level[y][:x] + 'Y' + level[y][x + 1:]
        screen = []
        if lev == 3:
            level[b_y] = level[b_y][:b_x] + 'B' + level[b_y][b_x + 1:]
            if b_x > x and abs(b_x - x) >= abs(b_y - y) and level[b_y][b_x-1] not in 'I-': b_x -= 1
            if b_x < x and abs(b_x - x) >= abs(b_y - y) and level[b_y][b_x+1] not in 'I-': b_x += 1
            if b_y > y and abs(b_x - x) < abs(b_y - y) and level[b_y-1][b_x] not in 'I-': b_y -= 1
            if b_y < y and abs(b_x - x) < abs(b_y - y) and level[b_y+1][b_x] not in 'I-': b_y += 1
        for i in range(len(level)):
            screen.append(level[i] + table[i])
        for s in screen:
            for i, c in enumerate(s):
                if i < 20:
                    print(f'{c} ', end='')
                else:
                    print(c, end='')
            print('')
        pers_move = input("Шагать - (u, d, l, r), сохранить игру - s, инвентарь - i: ")
        if pers_move == 's':
            with open('save.txt', 'w') as data:
                for i in (class_name, pers_level, max_health, health, endurance, strength, dexterity, intelligence, weapon.name, points, lev, x, y):
                    data.write(str(i)+' ')
                print("Игра сохранена")
        if pers_move == 'i':
            print('В вашем инвентаре:')
            for i in inventory: print(i)
        if pers_move == 'r' and x < 19 and level[y][x+1] not in 'I-': x += 1
        if pers_move == 'l' and x > 0 and level[y][x-1] not in 'I-': x -= 1
        if pers_move == 'd' and y < 9 and level[y+1][x] not in 'I-': y += 1
        if pers_move == 'u' and y > 0 and level[y-1][x] not in 'I-': y -= 1
        if x == 0 and y == 0 and pers_move == 'l':
            if lev > 1:
                lev = lev - 1
                x = 19
                y = 9
        if x == 19 and y == 9 and pers_move == 'r':
            if lev < 10:
                lev = lev + 1
                x = 0
                y = 0
        if level[y][x] == '*':
                print("Вы наступили на ловушку")
                change_health(-10)
                print(f'health: {health}')
        if level[y][x] in "gtB":
            if not fight(level[y][x]):
                break
            level_up()
        if level[y][x] in "▣":
            loot_random()

def change_health(h):
    global health
    health += h
    global max_health
    if health > max_health:
        health = max_health

def change_points(p):
    global points
    points += p

def loot_random():
    global inventory
    rand_int = random.randint(1, 3)
    if rand_int == 1: item = exquisite_bow
    if rand_int == 2: item = 'health_poison'
    if rand_int == 3: item = hammer
    inventory.append(item)
    print(f"Вы нашли {item}")

def fight(enemy):
    if enemy == 'g':
        enemy_name = 'goblin'
        print("Вы вступили в бой с гоблином")
    if enemy == 't':
        enemy_name = 'troll'
        print("Вы вступили в бой с троллем")
    if enemy == 'B':
        enemy_name = 'boss'
        print("Вы вступили в бой с боссом")
    base_damage = weapon.base_damage
    pers_damage = eval(weapon.damage_per_sec)
    en_health = eval(enemy_name).health
    en_damage = eval(enemy_name).base_damage
    while en_health > 0:
        print(f"Ваш удар: {pers_damage}")
        en_health -= pers_damage
        print(f"Удар врага: {en_damage}")
        change_health(-en_damage)
        if health <= 0:
            print("Вы мертвы!")
            return 0
    print(f'health: {health}')
    change_points(eval(enemy_name).w_points)
    return 1

def write_pers_characteristics():
    print(f'personage level: {pers_level}')
    print(f'health: {health}')
    print(f'endurance: {endurance}')
    print(f'strength: {strength}')
    print(f'dexterity: {dexterity}')
    print(f'intelligence: {intelligence}')

def level_up():
    global pers_level
    global max_health
    global health
    global endurance
    global strength
    global dexterity
    global intelligence
    global points
    need_points = 50 + pers_level * 30
    if points >= need_points:
        points -= need_points
        char_up = 'a'
        while char_up not in 'hesdi':
            char_up = input("Какую характерстику повысить (h -здоровье, e -выносливость, s -сила, d -ловкость, i -ум): ")
            if char_up == 'h':
                max_health *= 1.05
                health = max_health
            if char_up == 'e': endurance += 1
            if char_up == 's': strength += 1
            if char_up == 'd': dexterity += 1
            if char_up == 'i': intelligence += 1
        pers_level += 1
        write_pers_characteristics()

    
if __name__ == '__main__':
    main()