from console_game.game import hrs_profs
from console_game.game import items


npc_list = []

mech = hrs_profs.Hero(name='Mech', gender="Male", clan='Boyz', spec="Swordsman", chr_type='player', bag=[])

# badboy = hrs_profs.Hero(name="Bob", gender="male", clan="BoyZ", spec="Axeman", level=1)

# badboy = hrs_profs.Axeman('BadBoy', 'Male', 'Enemy', hp=10, head=items.simple_helmet,
#                           torso=items.simple_jacket, legs=items.simple_trousers, feet=items.simple_boots,
#                           active_weapon=items.heavy_axe)
# badboy1 = hrs_profs.Axeman('BadBoy', 'Male', 'Enemy', hp=10, head=items.simple_helmet,
#                            torso=items.simple_jacket, legs=items.simple_trousers, feet=items.simple_boots,
#                            active_weapon=items.heavy_axe)
# badboy2 = hrs_profs.Axeman('BadBoy', 'Male', 'Enemy', hp=10, head=items.simple_helmet,
#                            torso=items.simple_jacket, legs=items.simple_trousers, feet=items.simple_boots,
#                            active_weapon=items.heavy_axe)
# badboy3 = hrs_profs.Axeman('BadBoy', 'Male', 'Enemy', hp=10, head=items.simple_helmet,
#                            torso=items.simple_jacket, legs=items.simple_trousers, feet=items.simple_boots,
#                            active_weapon=items.heavy_axe)
#
# bigboy = hrs_profs.Axeman('BadBoy', 'Male', 'Enemy', hp=400, head=items.simple_helmet,
#                           torso=items.simple_jacket, legs=items.simple_trousers, feet=items.simple_boots,
#                           active_weapon=items.heavy_ass_axe)



# def test_clothes():
#     level = 1
#     helmet = functions.armor_creator(requested_armor_type='helmet', requested_level=[1, level])
#     vest = functions.armor_creator(requested_armor_type='vest', requested_level=[1, level])
#     left_arms = functions.armor_creator(requested_armor_type='armlet', requested_level=[1, level])
#     right_arms = functions.armor_creator(requested_armor_type='armlet', requested_level=[1, level])
#     legs = functions.armor_creator(requested_armor_type='trousers', requested_level=[1, level])
#     feet = functions.armor_creator(requested_armor_type='boots', requested_level=[1, level])
#
#     wpn = functions.weapon_creator(requested_weapon_type='heavy axe', requested_level=[1, level])
#     badboy = hrs_profs.Hero(name="Naked Bob", gender="male", clan="BoyZ", spec="Axeman", level=level, hp=100, strength=100,
#                              luck=100, movement=100, agility=100, intelligence=100, critical_chance=100)
#     badboy1 = hrs_profs.Hero(name="Bob", gender="male", clan="BoyZ", spec="Axeman", level=level,
#                              active_weapon=wpn, head=helmet, torso=vest, left_arm=left_arms, right_arm=right_arms, legs=legs, feet=feet,
#                              hp=100, strength=100, luck=100, movement=100, agility=100,
#                              intelligence=100, critical_chance=100)
#
#     badboy.print_chr()
#     badboy1.print_chr()
#
#     return badboy1
