import armor
import potions
import weapon


class LootBoxes:
    """Class for everything that gonna fall from the NPC or elsewhere"""

    def __init__(self, name, contents=None):
        if contents is None:
            contents = []
        self.name = name
        self.contents = contents

    def print_contents(self):
        if len(self.contents) >= 1:
            print(f"You found {self.name}'s on the floor:")
            for count, item in enumerate(self.contents):
                """Will print all armor from the armor list in items module"""
                if item.item_type == 'weapon':
                    print('Item # ', count, 'Name', ':', item.name.capitalize(),
                          'Condition', item.condition,
                          'Hp: ', item.hp,
                          'Damage: ', item.damage,
                          'Durability:', item.durability,
                          'Luck: ', item.luck,
                          'Strength: ', item.strength,
                          'Agility: ', item.agility,
                          'Movement: ', item.movement,
                          'Intelligence: ', item.intelligence,
                          'Critical chance: ', item.critical_chance,
                          'Level: ', item.level)
                elif item.item_type == 'clothes':
                    print('Item # ', count, 'Name', ':', item.name.capitalize(),
                          'Condition', item.condition,
                          'Hp: ', item.hp,
                          'Armor: ', item.armor,
                          'Durability:', item.durability,
                          'Luck: ', item.luck,
                          'Strength: ', item.strength,
                          'Agility: ', item.agility,
                          'Movement: ', item.movement,
                          'Intelligence: ', item.intelligence,
                          'Critical chance: ', item.critical_chance,
                          'Level: ', item.level)
                elif item.item_type == 'potion':
                    print('Item # ', count, 'Name', ':', item.name.capitalize(),
                          'Hp: ', item.hp,
                          'Level: ', item.level)
            print('----------------------------------------')


weapon_list = []

location_loot = []

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
armlet_of_holy_tester1 = armor.Armor(name='Holy armlet1', condition=100, armor=[20, 30], durability=100, hp=4, luck=5,
                                     strength=10, agility=10, movement=5, intelligence=1, critical_chance=15, level=10,
                                     item_type='clothes', armor_type='armlet', not_custom=False)
armlet_of_holy_tester2 = armor.Armor(name='Holy armlet2', condition=100, armor=[20, 30], durability=100, hp=5, luck=5,
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
                            strength=10, agility=10, movement=5, intelligence=1, critical_chance=6, level=10,
                            item_type='weapon', weapon_type='sword', not_custom=False)

helmet1 = armor.Armor(name='helmet1', condition=1, armor=[2, 5], durability=1, hp=1, luck=1,
                      strength=10, agility=10, movement=5, intelligence=1, critical_chance=15, level=10,
                      item_type='clothes', armor_type='helmet', not_custom=False)

helmet2 = armor.Armor(name='Holy helmet2', condition=2, armor=[20, 30], durability=2, hp=2, luck=2,
                      strength=10, agility=10, movement=5, intelligence=1, critical_chance=15, level=10,
                      item_type='clothes', armor_type='helmet', not_custom=False)

boot1 = armor.Armor(name='boots1', condition=1, armor=[2, 6], durability=1, hp=1, luck=1,
                    strength=10, agility=10, movement=5, intelligence=1, critical_chance=7, level=10,
                    item_type='clothes', armor_type='boots', not_custom=False)

boot2 = armor.Armor(name='Holy boots2', condition=2, armor=[50, 60], durability=2, hp=2, luck=2,
                    strength=10, agility=10, movement=5, intelligence=1, critical_chance=15, level=10,
                    item_type='clothes', armor_type='boots', not_custom=False)

simple_trousers = armor.Armor(name='trousers', condition=100, armor=[3, 4], durability=100, hp=6,
                              luck=5,
                              strength=10, agility=10, movement=5, intelligence=1, critical_chance=4, level=10,
                              item_type='clothes', armor_type='trousers', not_custom=False)

simple_vest = armor.Armor(name='vest', condition=100, armor=[3, 7], durability=100, hp=3, luck=5,
                          strength=10, agility=10, movement=5, intelligence=1, critical_chance=4, level=10,
                          item_type='clothes', armor_type='vest', not_custom=False)

simple_armlet1 = armor.Armor(name='armlet1', condition=100, armor=[2, 3], durability=100, hp=4, luck=5,
                             strength=10, agility=10, movement=5, intelligence=1, critical_chance=2, level=10,
                             item_type='clothes', armor_type='armlet', not_custom=False)
simple_armlet2 = armor.Armor(name='armlet2', condition=100, armor=[2, 3], durability=100, hp=5, luck=5,
                             strength=10, agility=10, movement=5, intelligence=1, critical_chance=2, level=10,
                             item_type='clothes', armor_type='armlet', not_custom=False)

small_health_potion = potions.Health_Potions(name='Small HP potion', level=1, hp=20)
medium_health_potion = potions.Health_Potions(name='Medium HP potion', level=1, hp=35)
large_health_potion = potions.Health_Potions(name='Large HP potion', level=1, hp=50)

good_box = [super_sword, helmet_of_holy_tester, vest_of_holy_tester, trousers_of_holy_tester, boots_of_holy_tester,
            armlet_of_holy_tester1, armlet_of_holy_tester2, small_health_potion, medium_health_potion,
            large_health_potion]

simple_box = [rusty_sword, helmet1, boot1, simple_trousers, simple_vest, simple_armlet1, simple_armlet2]


check_box = [helmet1, super_sword, medium_health_potion]

potion_box = [small_health_potion, medium_health_potion, large_health_potion]
"""All armor is here"""

naked = armor.Armor('Naked', armor=[0, 1])
