import random
from console_game.game import weapon
from console_game.game import armor
from console_game.game import potions

class LootBoxes:

    def __init__(self, name, contents=[]):
        self.name = name
        self.contents = contents

    def print_contents(self):
        if len(self.contents) >= 1:
            for count, item in enumerate(self.contents):
                print('----------------------------------------')
                """Will print all armor from the armor list in items module"""
                if item.item_type == 'weapon':
                    print('Item # ', count, '\nName', ':', item.name.capitalize(),
                          '\nCondition', item.condition,
                          '\nHp: ', item.hp,
                          '\nDamage: ', item.damage,
                          '\nDurability:', item.durability,
                          '\nLuck: ', item.luck,
                          '\nStrength: ', item.strength,
                          '\nAgility: ', item.agility,
                          '\nMovement: ', item.movement,
                          '\nIntelligence: ', item.intelligence,
                          '\nCritical chance: ', item.critical_chance,
                          '\nLevel: ', item.level)
                elif item.item_type == 'clothes':
                    print('Item # ', count, '\nName', ':', item.name.capitalize(),
                          '\nCondition', item.condition,
                          '\nHp: ', item.hp,
                          '\nArmor: ', item.armor,
                          '\nDurability:', item.durability,
                          '\nLuck: ', item.luck,
                          '\nStrength: ', item.strength,
                          '\nAgility: ', item.agility,
                          '\nMovement: ', item.movement,
                          '\nIntelligence: ', item.intelligence,
                          '\nCritical chance: ', item.critical_chance,
                          '\nLevel: ', item.level)
                elif item.item_type == 'potion':
                    print('Item # ', count, '\nName', ':', item.name.capitalize(),
                          '\nHp: ', item.hp,
                          '\nLevel: ', item.level)
            print('----------------------------------------')


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

rusty_sword = weapon.Weapon('Rusty sword', condition=100, damage=[5, 7], durability=100, hp=1, luck=5,
                            strength=10, agility=10, movement=5, intelligence=1, critical_chance=15, level=10,
                            item_type='weapon', weapon_type='sword', not_custom=False)

small_health_potion = potions.Health_Potions(name='Small HP potion', level=1, hp=20)
medium_health_potion = potions.Health_Potions(name='Medium HP potion', level=1, hp=35)
large_health_potion = potions.Health_Potions(name='Large HP potion', level=1, hp=50)

good_box = [super_sword, helmet_of_holy_tester, vest_of_holy_tester, trousers_of_holy_tester, boots_of_holy_tester,
            armlet_of_holy_tester1, armlet_of_holy_tester2, small_health_potion, medium_health_potion, large_health_potion]

potion_box = [small_health_potion, medium_health_potion, large_health_potion]
"""All armor is here"""

naked = armor.Armor('Naked', armor=[0, 1])
