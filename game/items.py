import random
from console_game.game import weapon
from console_game.game import armor

weapon_list = []

gold_chest = []  # Test list for items to pick up

armor_list = []

"""All weapon is here"""
fist = weapon.Weapon('Fist')
super_sword = weapon.Weapon(name='super sword', condition=100, damage=[20, 27], durability=100, hp=1, luck=5,
                            strength=10, agility=10, movement=5, intelligence=1, critical_chance=15, level=10,
                            item_type='weapon', weapon_type='sword', not_custom=False)
helmet_of_holy_tester = armor.Armor(name='Holy helmet', condition=100, armor=[20, 30], durability=100, hp=2, luck=5,
                                    strength=10, agility=10, movement=5, intelligence=1, critical_chance=15, level=10,
                                    item_type='clothes', armor_type='helmet', not_custom=False)
vest_of_holy_tester = armor.Armor(name='Holy vest', condition=100, armor=[30, 40], durability=100, hp=3, luck=5,
                                  strength=10, agility=10, movement=5, intelligence=1, critical_chance=15, level=10,
                                  item_type='clothes', armor_type='vest', not_custom=False)
armlet_of_holy_tester1 = armor.Armor(name='Holy armlet', condition=100, armor=[20, 30], durability=100, hp=4, luck=5,
                                     strength=10, agility=10, movement=5, intelligence=1, critical_chance=15, level=10,
                                     item_type='clothes', armor_type='armlet', not_custom=False)
armlet_of_holy_tester2 = armor.Armor(name='Holy armlet', condition=100, armor=[20, 30], durability=100, hp=5, luck=5,
                                     strength=10, agility=10, movement=5, intelligence=1, critical_chance=15, level=10,
                                     item_type='clothes', armor_type='armlet', not_custom=False)
trousers_of_holy_tester = armor.Armor(name='Holy trousers', condition=100, armor=[40, 50], durability=100, hp=6,
                                      luck=5,
                                      strength=10, agility=10, movement=5, intelligence=1, critical_chance=15, level=10,
                                      item_type='clothes', armor_type='trousers', not_custom=False)
boots_of_holy_tester = armor.Armor(name='Holy boots', condition=100, armor=[50, 60], durability=100, hp=7, luck=5,
                                   strength=10, agility=10, movement=5, intelligence=1, critical_chance=15, level=10,
                                   item_type='clothes', armor_type='boots', not_custom=False)

good_box = [super_sword, helmet_of_holy_tester, vest_of_holy_tester, trousers_of_holy_tester, boots_of_holy_tester,
            armlet_of_holy_tester1, armlet_of_holy_tester2]

"""All armor is here"""

naked = armor.Armor('Naked', armor=[0, 1])
