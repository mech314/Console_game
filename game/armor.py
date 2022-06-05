import math


class Armor:
    """Class for armor"""
    _id = 0

    def __init__(self, name, condition=None, armor=None, durability=0, hp=0, luck=0, strength=0, agility=0,
                 movement=0, intelligence=0, critical_chance=0, level=1, armor_type=None):
        item_modifier = {'broken': 0.5, 'rusty': 0.6, 'simple': 0.8, 'normal': 1, 'excellent': 1.2, 'heroic': 1.3}
        if armor is None:
            armor = [0, 0]
        Armor._id += 1
        self._id = Armor._id  # Need to finish this
        self.name = name  # Name
        self.condition = condition
        self.armor = armor  # Amount of protection
        self.durability = durability
        self.hp = hp
        self.luck = luck
        self.strength = strength
        self.agility = agility
        self.movement = movement
        self.intelligence = intelligence
        self.critical_chance = critical_chance
        self.level = level
        self.armor_type = armor_type  # Important for putting armor on the character body parts

        if condition is None:
            self.armor_type = 'naked'
        else:
            if self.armor_type.lower() == 'helmet':
                self.armor = [(int(1 * (self.level * item_modifier[self.condition]))),
                              (int(3 * (self.level * item_modifier[self.condition])))]
                """you have stopped here, armor modification happen based on level and codition, just using the 
                dictionary, need to think how to make initial values a little bit more flexible, not just rigid 1-3
                Need to finish all clothes, think about how different clothes will add up diff values. Then right a 
                function that will create a bunch of various clothes into a list. 
            
                """
                self.durability = int(25 * (self.level * item_modifier[self.condition]))
                self.hp = -5
                self.luck = -1
                self.strength = 0
                self.agility = -1
                self.movement = -1
                self.intelligence = -1
                self.critical_chance = 0
            elif self.armor_type.lower() == 'Jacket':
                self.armor = [5 * self.level, 7 * self.level]
                self.durability = int(45 * (self.level * 0.8))
                self.hp = 0
                self.luck = 0
                self.strength = 0
                self.agility = 0
                self.movement = 0
                self.intelligence = 0
                self.critical_chance = 0
            elif self.armor_type.lower() == 'Vest':
                self.armor = [3 * self.level, 7 * self.level]
                self.durability = int(45 * (self.level * 0.8))
                self.hp = int(3 * (self.level * 0.8))
                self.luck = 0
                self.strength = 0
                self.agility = 0
                self.movement = 0
                self.intelligence = 0
                self.critical_chance = 0
            elif self.armor_type.lower() == 'Armlet':
                self.armor = [1 * self.level, 3 * self.level]
                self.durability = int(45 * (self.level * 0.8))
                self.hp = int(3 * (self.level * 0.8))
                self.luck = 0
                self.strength = 0
                self.agility = 0
                self.movement = 0
                self.intelligence = 0
                self.critical_chance = 0
            elif self.armor_type.lower() == 'Trousers':
                self.armor = [3 * self.level, 9 * self.level]
                self.durability = int(45 * (self.level * 0.8))
                self.hp = int(3 * (self.level * 0.8))
                self.luck = 0
                self.strength = 0
                self.agility = 0
                self.movement = 0
                self.intelligence = 0
                self.critical_chance = 0
            elif self.armor_type.lower() == 'Boots':
                self.armor = [1 * self.level, 2 * self.level]
                self.durability = int(45 * (self.level * 0.8))
                self.hp = int(3 * (self.level * 0.8))
                self.luck = 0
                self.strength = 0
                self.agility = 0
                self.movement = 0
                self.intelligence = 0
                self.critical_chance = 0


    @property
    def armor_chr(self):
        """Creates the dictionary that has all characteristics of a weapon even if they are equal to 0."""
        arm = dict(name=self.name, level=self.level, armor=self.armor, durability=self.durability,
                   condition=self.condition, hp=self.hp, luck=self.luck, strength=self.strength, agility=self.agility,
                   movement=self.movement, intelligence=self.intelligence, critical_chance=self.critical_chance,
                   armor_type=self.armor_type)
        for k, v in arm.items():
            print(k.capitalize(), ':', v)
        return None

    @property
    def print_arm_chr(self):
        """Creates a dict that has only weapon values NOT equal to Zero, even if they are negative"""
        arm_chr = {key: value for (key, value) in self.armor_chr.items() if value}
        for k, v in arm_chr.items():
            print(k.capitalize(), ':', v)

# class Helmet(Armor):
#     """Everything that will be on your head"""
#
#     def __init__(self, name, armor, durability, hp=0, luck=0, strength=0, agility=0,
#                  movement=0, intelligence=0, critical_chance=0, armor_type=None):
#         super().__init__(name, armor, durability, hp, luck, strength, agility,
#                          movement, intelligence, critical_chance, armor_type)
#         self.armor_type = 'helmet'
#
#
# class Jacket(Armor):
#     """Jacket has sleeves so it protect torso and both hands"""
#
#     def __init__(self, name, armor, durability, hp=0, luck=0, strength=0, agility=0,
#                  movement=0, intelligence=0, critical_chance=0, armor_type=None):
#         super().__init__(name, armor, durability, hp, luck, strength, agility,
#                          movement, intelligence, critical_chance, armor_type)
#         self.armor_type = 'jacket'
#
#
# class Vest(Armor):
#     """Vest has not sleeves, so it will protect only torso"""
#
#     def __init__(self, name, armor, durability, hp=0, luck=0, strength=0, agility=0,
#                  movement=0, intelligence=0, critical_chance=0, armor_type=None):
#         super().__init__(name, armor, durability, hp, luck, strength, agility,
#                          movement, intelligence, critical_chance, armor_type)
#         self.armor_type = 'vest'
#
#
# class Armlet(Armor):
#     """Will be on your arms, can be used only with Vest or without anything on torso, could be used on both hands"""
#
#     def __init__(self, name, armor, durability, hp=0, luck=0, strength=0, agility=0,
#                  movement=0, intelligence=0, critical_chance=0, armor_type=None):
#         super().__init__(name, armor, durability, hp, luck, strength, agility,
#                          movement, intelligence, critical_chance, armor_type)
#         self.armor_type = 'armlet'
#
#
# class Trousers(Armor):
#     """Everything that will be on your legs"""
#
#     def __init__(self, name, armor, durability, hp=0, luck=0, strength=0, agility=0,
#                  movement=0, intelligence=0, critical_chance=0, armor_type=None):
#         super().__init__(name, armor, durability, hp, luck, strength, agility,
#                          movement, intelligence, critical_chance, armor_type)
#         self.armor_type = 'trousers'
#
#
# class Boots(Armor):
#     """Everything that will be on your feet"""
#
#     def __init__(self, name, armor, durability, hp=0, luck=0, strength=0, agility=0,
#                  movement=0, intelligence=0, critical_chance=0, armor_type=None):
#         super().__init__(name, armor, durability, hp, luck, strength, agility,
#                          movement, intelligence, critical_chance, armor_type)
#         self.armor_type = 'boots'
#
#
# class Naked(Armor):
#     """Just naked"""
#
#     def __init__(self, name, condition, armor=None, durability=math.inf, hp=0, luck=0, strength=0, agility=0,
#                  movement=0, intelligence=0, critical_chance=0, armor_type=None):
#         super().__init__(name, condition, armor, durability, hp, luck, strength, agility,
#                          movement, intelligence, critical_chance, armor_type)
#         if armor is None:
#             armor = [0, 0]
#         self.armor_type = 'naked'
