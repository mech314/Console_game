import random


class Armor:
    """Class for armor"""
    _id = 0

    def __init__(self, name, condition=None, armor=None, durability=0, hp=0, luck=0, strength=0, agility=0,
                 movement=0, intelligence=0, critical_chance=0, level=1, item_type='clothes', armor_type=None, isItCustom=True):
        self.item_modifier = {'broken': 0.5, 'rusty': 0.6, 'simple': 0.8, 'normal': 1, 'excellent': 1.2,
                              'heroic': 1.3}
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
        self.item_type = item_type
        self.armor_type = armor_type  # Important for putting armor on the character body parts
        self.isItCustom = isItCustom


        if self.condition is None:  # If condition is 'naked' armor will be just naked.
            self.armor = [0, 1]
            self.armor_type = 'naked'
        elif condition:
            self.armor_maker()

    def armor_maker(self):
        """This functions only for automatically generated items, Custom items will made by hand."""
        if self.isItCustom and self.armor_type.lower() != 'naked':
            if self.armor_type.lower() == 'helmet':
                self.armor = [(int(random.randint(1, 4) * (self.level * self.item_modifier[self.condition]))),
                              (int(random.randint(3, 5) * (self.level * self.item_modifier[self.condition])))]
                self.durability = int((random.randint(15, 30) * (self.level * self.item_modifier[self.condition])))
                self.hp = int((random.randint(0, 1) * (self.level * self.item_modifier[self.condition])))
                self.luck = int((random.randint(1, 3) * (self.level * self.item_modifier[self.condition])))
                self.strength = int((random.randint(0, 0) * (self.level * self.item_modifier[self.condition])))
                self.agility = int((random.randrange(-3, -1) * (self.level * self.item_modifier[self.condition])))
                self.movement = int((random.randrange(-3, -1) * (self.level * self.item_modifier[self.condition])))
                self.intelligence = int((random.randint(1, 5) * (self.level * self.item_modifier[self.condition])))
                self.critical_chance = int((random.randint(0, 5) * (self.level * self.item_modifier[self.condition])))
            elif self.armor_type.lower() == 'jacket':
                self.armor = [(int(random.randint(3, 7) * (self.level * self.item_modifier[self.condition]))),
                              (int(random.randint(7, 9) * (self.level * self.item_modifier[self.condition])))]
                self.durability = int((random.randint(25, 45) * (self.level * self.item_modifier[self.condition])))
                self.hp = int((random.randint(5, 15) * (self.level * self.item_modifier[self.condition])))
                self.luck = int((random.randint(1, 3) * (self.level * self.item_modifier[self.condition])))
                self.strength = int((random.randint(1, 4) * (self.level * self.item_modifier[self.condition])))
                self.agility = int((random.randint(0, 0) * (self.level * self.item_modifier[self.condition])))
                self.movement = int((random.randint(1, 3) * (self.level * self.item_modifier[self.condition])))
                self.intelligence = int((random.randint(0, 0) * (self.level * self.item_modifier[self.condition])))
                self.critical_chance = int((random.randint(0, 5) * (self.level * self.item_modifier[self.condition])))
            elif self.armor_type.lower() == 'vest':
                self.armor = [(int(random.randint(2, 5) * (self.level * self.item_modifier[self.condition]))),
                              (int(random.randint(6, 8) * (self.level * self.item_modifier[self.condition])))]
                self.durability = int((random.randint(15, 30) * (self.level * self.item_modifier[self.condition])))
                self.hp = int((random.randint(5, 10) * (self.level * self.item_modifier[self.condition])))
                self.luck = int((random.randint(0, 0) * (self.level * self.item_modifier[self.condition])))
                self.strength = int((random.randint(2, 5) * (self.level * self.item_modifier[self.condition])))
                self.agility = int((random.randrange(-1, 3) * (self.level * self.item_modifier[self.condition])))
                self.movement = int((random.randint(1, 3) * (self.level * self.item_modifier[self.condition])))
                self.intelligence = int((random.randint(0, 0) * (self.level * self.item_modifier[self.condition])))
                self.critical_chance = int((random.randint(0, 5) * (self.level * self.item_modifier[self.condition])))
            elif self.armor_type.lower() == 'armlet':
                self.armor = [(int(random.randint(1, 3) * (self.level * self.item_modifier[self.condition]))),
                              (int(random.randint(4, 5) * (self.level * self.item_modifier[self.condition])))]
                self.durability = int((random.randint(15, 30) * (self.level * self.item_modifier[self.condition])))
                self.hp = int((random.randint(1, 5) * (self.level * self.item_modifier[self.condition])))
                self.luck = int((random.randint(1, 3) * (self.level * self.item_modifier[self.condition])))
                self.strength = int((random.randint(1, 3) * (self.level * self.item_modifier[self.condition])))
                self.agility = int((random.randrange(-3, -1) * (self.level * self.item_modifier[self.condition])))
                self.movement = int((random.randrange(-2, -1) * (self.level * self.item_modifier[self.condition])))
                self.intelligence = int((random.randint(0, 0) * (self.level * self.item_modifier[self.condition])))
                self.critical_chance = int((random.randint(0, 5) * (self.level * self.item_modifier[self.condition])))
            elif self.armor_type.lower() == 'trousers':
                self.armor = [(int(random.randint(1, 4) * (self.level * self.item_modifier[self.condition]))),
                              (int(random.randint(3, 5) * (self.level * self.item_modifier[self.condition])))]
                self.durability = int((random.randint(15, 30) * (self.level * self.item_modifier[self.condition])))
                self.hp = int((random.randint(1, 5) * (self.level * self.item_modifier[self.condition])))
                self.luck = int((random.randint(1, 3) * (self.level * self.item_modifier[self.condition])))
                self.strength = int((random.randint(5, 7) * (self.level * self.item_modifier[self.condition])))
                self.agility = int((random.randint(1, 7) * (self.level * self.item_modifier[self.condition])))
                self.movement = int((random.randint(3, 9) * (self.level * self.item_modifier[self.condition])))
                self.intelligence = int((random.randint(0, 0) * (self.level * self.item_modifier[self.condition])))
                self.critical_chance = int((random.randint(0, 5) * (self.level * self.item_modifier[self.condition])))
            elif self.armor_type.lower() == 'boots':
                self.armor = [(int(random.randint(1, 4) * (self.level * self.item_modifier[self.condition]))),
                              (int(random.randint(3, 5) * (self.level * self.item_modifier[self.condition])))]
                self.durability = int((random.randint(15, 30) * (self.level * self.item_modifier[self.condition])))
                self.hp = int((random.randint(15, 30) * (self.level * self.item_modifier[self.condition])))
                self.luck = int((random.randint(1, 3) * (self.level * self.item_modifier[self.condition])))
                self.strength = int((random.randint(1, 3) * (self.level * self.item_modifier[self.condition])))
                self.agility = int((random.randint(1, 6) * (self.level * self.item_modifier[self.condition])))
                self.movement = int((random.randint(5, 10) * (self.level * self.item_modifier[self.condition])))
                self.intelligence = int((random.randint(0, 0) * (self.level * self.item_modifier[self.condition])))
                self.critical_chance = int((random.randint(0, 5) * (self.level * self.item_modifier[self.condition])))

    @property
    def armor_chr(self):
        """Creates the dictionary that has all characteristics of a weapon even if they are equal to 0."""
        arm = dict(name=self.name, level=self.level, armor=self.armor, durability=self.durability,
                   condition=self.condition, hp=self.hp, luck=self.luck, strength=self.strength, agility=self.agility,
                   movement=self.movement, intelligence=self.intelligence, critical_chance=self.critical_chance,
                   armor_type=self.armor_type)
        return {k.capitalize(): v for k, v in arm.items()}

    @property
    def print_arm_chr(self):
        """Creates a dict that has only weapon values NOT equal to Zero, even if they are negative"""
        arm_chr = {key: value for (key, value) in self.armor_chr.items() if value}
        return {k.capitalize(): v for k, v in arm_chr.items()}
