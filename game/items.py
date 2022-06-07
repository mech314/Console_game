import random
from console_game.game import weapon
from console_game.game import armor


weapon_list = []

armor_list = []


"""All weapon is here"""
fist = weapon.Weapon('Fist')
# rusty_sword = weapon.Sword('Rusty sword', (10, 20), durability=100, hp=1, luck=1, strength=1, agility=1,
#                            movement=1, intelligence=1, critical_chance=10)
# nice_sword = weapon.Sword('Nice sword', (19, 30), durability=100, hp=1, luck=1, strength=1, agility=1,
#                           movement=1, intelligence=1, critical_chance=10)
# heavy_axe = weapon.Axe('Heavy Axe', (5, 24), durability=75, agility=-3, strength=4, intelligence=-3, movement=-1,
#                        critical_chance=30)
# heavy_ass_axe = weapon.Axe('Heavy Axe', (40, 77), durability=150, agility=-9, strength=9, intelligence=-18, movement=-7,
#                            critical_chance=66)

"""All armor is here"""

naked = armor.Armor('Naked', armor=[0, 1])
