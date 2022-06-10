import random


class Weapon:
    _id = 0

    def __init__(self, name, condition=None, damage=None, durability=0, hp=0, luck=0, strength=0, agility=0,
                 movement=0, intelligence=0, critical_chance=0, level=1, item_type='weapon', weapon_type=None,
                 not_custom=True):
        self.item_modifier = {'broken': 0.5, 'rusty': 0.6, 'simple': 0.8, 'normal': 1, 'excellent': 1.2,
                              'heroic': 1.3}
        if damage is None:
            damage = [0, 0]
        Weapon._id += 1
        self._id = Weapon._id  # Need to finish this
        self.name = name  # Name
        self.condition = condition
        self.damage = damage  # Amount of protection
        self.durability = durability
        self.hp = hp
        self.luck = luck
        self.strength = strength
        self.agility = agility
        self.movement = movement
        self.intelligence = intelligence
        self.critical_chance = critical_chance
        self.level = level
        self.item_type = item_type
        self.weapon_type = weapon_type  # Important for putting armor on the character body parts
        self.not_custom = not_custom

        if self.condition is None:  # If condition is 'fist' armor will be just naked.
            self.damage = [0, 1]
            self.weapon_type = 'fist'
        elif condition:
            self.weapon_maker()

    def weapon_maker(self):
        """This functions only for automatically generated items, Custom items will made by hand."""
        if self.not_custom and self.weapon_type.lower() != 'fist':
            if self.weapon_type.lower() == 'sword':
                self.damage = [(int(random.randint(1, 4) * (self.level * self.item_modifier[self.condition]))),
                               (int(random.randint(3, 5) * (self.level * self.item_modifier[self.condition])))]
                self.durability = int((random.randint(15, 30) * (self.level * self.item_modifier[self.condition])))
                self.hp = int((random.randint(0, 1) * (self.level * self.item_modifier[self.condition])))
                self.luck = int((random.randint(1, 3) * (self.level * self.item_modifier[self.condition])))
                self.strength = int((random.randint(0, 0) * (self.level * self.item_modifier[self.condition])))
                self.agility = int((random.randrange(-3, -1) * (self.level * self.item_modifier[self.condition])))
                self.movement = int((random.randrange(-3, -1) * (self.level * self.item_modifier[self.condition])))
                self.intelligence = int((random.randint(1, 5) * (self.level * self.item_modifier[self.condition])))
                self.critical_chance = int((random.randint(0, 5) * (self.level * self.item_modifier[self.condition])))
            elif self.weapon_type.lower() == 'small sword':
                self.weapon_type = 'sword'
                self.damage = [(int(random.randint(3, 7) * (self.level * self.item_modifier[self.condition]))),
                               (int(random.randint(7, 9) * (self.level * self.item_modifier[self.condition])))]
                self.durability = int((random.randint(25, 45) * (self.level * self.item_modifier[self.condition])))
                self.hp = int((random.randint(0, 1) * (self.level * self.item_modifier[self.condition])))
                self.luck = int((random.randint(1, 3) * (self.level * self.item_modifier[self.condition])))
                self.strength = int((random.randint(1, 4) * (self.level * self.item_modifier[self.condition])))
                self.agility = int((random.randint(0, 0) * (self.level * self.item_modifier[self.condition])))
                self.movement = int((random.randint(1, 3) * (self.level * self.item_modifier[self.condition])))
                self.intelligence = int((random.randint(0, 0) * (self.level * self.item_modifier[self.condition])))
                self.critical_chance = int((random.randint(0, 5) * (self.level * self.item_modifier[self.condition])))
            elif self.weapon_type.lower() == 'heavy sword':
                self.weapon_type = 'sword'
                self.damage = [(int(random.randint(2, 5) * (self.level * self.item_modifier[self.condition]))),
                               (int(random.randint(6, 8) * (self.level * self.item_modifier[self.condition])))]
                self.durability = int((random.randint(15, 30) * (self.level * self.item_modifier[self.condition])))
                self.hp = int((random.randint(0, 1) * (self.level * self.item_modifier[self.condition])))
                self.luck = int((random.randint(0, 0) * (self.level * self.item_modifier[self.condition])))
                self.strength = int((random.randint(2, 5) * (self.level * self.item_modifier[self.condition])))
                self.agility = int((random.randrange(-1, 3) * (self.level * self.item_modifier[self.condition])))
                self.movement = int((random.randint(1, 3) * (self.level * self.item_modifier[self.condition])))
                self.intelligence = int((random.randint(0, 0) * (self.level * self.item_modifier[self.condition])))
                self.critical_chance = int((random.randint(0, 5) * (self.level * self.item_modifier[self.condition])))
            elif self.weapon_type.lower() == 'axe':
                self.weapon_type = 'axe'
                self.damage = [(int(random.randint(1, 3) * (self.level * self.item_modifier[self.condition]))),
                               (int(random.randint(4, 5) * (self.level * self.item_modifier[self.condition])))]
                self.durability = int((random.randint(15, 30) * (self.level * self.item_modifier[self.condition])))
                self.hp = int((random.randint(0, 1) * (self.level * self.item_modifier[self.condition])))
                self.luck = int((random.randint(1, 3) * (self.level * self.item_modifier[self.condition])))
                self.strength = int((random.randint(1, 3) * (self.level * self.item_modifier[self.condition])))
                self.agility = int((random.randrange(-3, -1) * (self.level * self.item_modifier[self.condition])))
                self.movement = int((random.randrange(-2, -1) * (self.level * self.item_modifier[self.condition])))
                self.intelligence = int((random.randint(0, 0) * (self.level * self.item_modifier[self.condition])))
                self.critical_chance = int((random.randint(0, 5) * (self.level * self.item_modifier[self.condition])))
            elif self.weapon_type.lower() == 'small axe':
                self.weapon_type = 'axe'
                self.damage = [(int(random.randint(1, 4) * (self.level * self.item_modifier[self.condition]))),
                               (int(random.randint(3, 5) * (self.level * self.item_modifier[self.condition])))]
                self.durability = int((random.randint(15, 30) * (self.level * self.item_modifier[self.condition])))
                self.hp = int((random.randint(0, 1) * (self.level * self.item_modifier[self.condition])))
                self.luck = int((random.randint(1, 3) * (self.level * self.item_modifier[self.condition])))
                self.strength = int((random.randint(5, 7) * (self.level * self.item_modifier[self.condition])))
                self.agility = int((random.randint(1, 7) * (self.level * self.item_modifier[self.condition])))
                self.movement = int((random.randint(3, 9) * (self.level * self.item_modifier[self.condition])))
                self.intelligence = int((random.randint(0, 0) * (self.level * self.item_modifier[self.condition])))
                self.critical_chance = int((random.randint(0, 5) * (self.level * self.item_modifier[self.condition])))
            elif self.weapon_type.lower() == 'heavy axe':
                self.weapon_type = 'axe'
                self.damage = [(int(random.randint(1, 4) * (self.level * self.item_modifier[self.condition]))),
                              (int(random.randint(3, 5) * (self.level * self.item_modifier[self.condition])))]
                self.durability = int((random.randint(15, 30) * (self.level * self.item_modifier[self.condition])))
                self.hp = int((random.randint(0, 1) * (self.level * self.item_modifier[self.condition])))
                self.luck = int((random.randint(1, 3) * (self.level * self.item_modifier[self.condition])))
                self.strength = int((random.randint(1, 3) * (self.level * self.item_modifier[self.condition])))
                self.agility = int((random.randint(1, 6) * (self.level * self.item_modifier[self.condition])))
                self.movement = int((random.randint(5, 10) * (self.level * self.item_modifier[self.condition])))
                self.intelligence = int((random.randint(0, 0) * (self.level * self.item_modifier[self.condition])))
                self.critical_chance = int((random.randint(0, 5) * (self.level * self.item_modifier[self.condition])))

    @property
    def weapon_chr(self):
        """Creates the dictionary that has all characteristics of a weapon even if they are equal to 0."""
        wpn = dict(name=self.name, level=self.level, damage=self.damage, durability=self.durability,
                   condition=self.condition, luck=self.luck, strength=self.strength, agility=self.agility,
                   movement=self.movement, intelligence=self.intelligence, critical_chance=self.critical_chance,
                   weapon_type=self.weapon_type)
        return {k.capitalize(): v for k, v in wpn.items()}

    @property
    def print_wpn_chr(self):
        """Creates a dict that has only weapon values NOT equal to Zero, even if they are negative"""
        wpn_chr = {key: value for (key, value) in self.weapon_chr.items() if value}
        return {k.capitalize(): v for k, v in wpn_chr.items()}

    # def __str__(self):
    #     return str(self.name) + ' ' + str(self.damage) + ' ' + str(self.durability)
    #
    # def __repr__(self):
    #     return str(self.name) + ' ' + str(self.damage) + ' ' + str(self.durability)


# class Fist(Weapon):
#
#     def __init__(self, name, damage=None, weapon_type=None):
#         super().__init__(damage, name, weapon_type)
#         self.name = name
#         self.damage = (1, 5)
#         self.weapon_type = 'fist'
#
#
# class Sword(Weapon):
#
#     def __init__(self, name, damage, durability, level=1, hp=0, luck=0, strength=0, agility=0,
#                  movement=0, intelligence=0, critical_chance=0, weapon_type=None):
#         super().__init__(name, damage, durability, level, hp, luck, strength, agility,
#                          movement, intelligence, critical_chance, weapon_type)
#         self.weapon_type = 'sword'
#
#
# class Axe(Weapon):
#
#     def __init__(self, name, damage, durability, level=1, hp=0, luck=0, strength=0, agility=0,
#                  movement=0, intelligence=0, critical_chance=0, weapon_type=None):
#         super().__init__(name, damage, durability, level, hp, luck, strength, agility,
#                          movement, intelligence, critical_chance, weapon_type)
#         self.weapon_type = 'axe'
#
#
# class Knife(Weapon):
#
#     def __init__(self, name, damage, durability, level=1, hp=0, luck=0, strength=0, agility=0,
#                  movement=0, intelligence=0, critical_chance=0, weapon_type=None):
#         super().__init__(name, damage, durability, level, hp, luck, strength, agility,
#                          movement, intelligence, critical_chance, weapon_type)
#         self.weapon_type = "knife"
#
#
# class Bow(Weapon):
#
#     def __init__(self, name, damage, durability, level=1, hp=0, luck=0, strength=0, agility=0,
#                  movement=0, intelligence=0, critical_chance=0, weapon_type=None):
#         super().__init__(name, damage, durability, level, hp, luck, strength, agility,
#                          movement, intelligence, critical_chance, weapon_type)
#         self.weapon_type = "bow"


