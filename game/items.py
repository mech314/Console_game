import random
from console_game.game import weapon
from console_game.game import armor


weapon_list = []

gold_chest = []     # Test list for items to pick up

armor_list = []


"""All weapon is here"""
fist = weapon.Weapon('Fist')

"""All armor is here"""

naked = armor.Armor('Naked', armor=[0, 1])
