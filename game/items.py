import weapon
import armor

weapon_dict = {}
armor_dict = {}

"""All weapon is here"""
fist = weapon.Fist('Fist', (1, 3))
rusty_sword = weapon.Sword('Rusty sword', (10, 20), durability=100, hp=1, luck=1, strength=1, agility=1,
                           movement=1, intelligence=1, critical_chance=10)
nice_sword = weapon.Sword('Nice sword', (19, 30), durability=100, hp=1, luck=1, strength=1, agility=1,
                          movement=1, intelligence=1, critical_chance=10)
heavy_axe = weapon.Axe('Heavy Axe', (5, 24), durability=75, agility=-3, strength=4, intelligence=-3, movement=-1,
                       critical_chance=30)
heavy_ass_axe = weapon.Axe('Heavy Axe', (40, 77), durability=150, agility=-9, strength=9, intelligence=-18, movement=-7,
                           critical_chance=66)

"""All armor is here"""

naked = armor.Naked('Naked', (0, 1))
simple_helmet = armor.Helmet('Simple helmet', (4, 9), durability=30, hp=10, agility=1)
simple_jacket = armor.Jacket('Simple jacket', (7, 11), durability=40, hp=15, strength=1, agility=1)
simple_trousers = armor.Trousers('Simple trousers', (5, 9), durability=35, hp=5, agility=1, critical_chance=5)
simple_boots = armor.Boots('Simple boots', (3, 5), durability=50, movement=1, luck=1, agility=3)
simple_vest = armor.Vest('Simple vest', (5, 7), durability=50, movement=1, hp=10, luck=1, agility=3)
simple_armlet = armor.Armlet('Simple armlet', (3, 7), durability=25, movement=3, hp=5, luck=1, agility=3, strength=2)
