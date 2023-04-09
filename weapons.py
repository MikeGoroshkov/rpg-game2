# class fists:
#     base_damage = 3
#     damage_per_sec = base_damage*(1 + strength*0.3)

class decrepit_bow:
    name = 'decrepit_bow'
    min_dexterity = 7
    base_damage = 10
    damage_per_sec = 'base_damage*(1 + dexterity*0.5)'
    # def __init__(self):

class exquisite_bow:
    min_dexterity = 10
    min_intelligence = 8
    base_damage = 9
    damage_per_sec = 'base_damage*(1 + dexterity*0.4 + intelligence*0.2)'
#
class woodcutter_axe:
    name = 'woodcutter_axe'
    min_strength = 7
    base_damage = 10
    damage_per_sec = 'base_damage*(1 + strength*0.5)'

class hammer:
    min_strength = 10
    base_damage = 12
    damage_per_sec = 'base_damage*(1 + strength*0.5)'

class magic_staff:
    name = 'magic_staff'
    min_intelligence = 7
    base_damage = 11
    damage_per_sec = 'base_damage*(1 + intelligence*0.5)'