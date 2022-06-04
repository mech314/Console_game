import math


class Armor:
    """Class for armor"""
    _id = 0
    def __init__(self, name, armor, durability, hp=0, luck=0, strength=0, agility=0,
                 movement=0, intelligence=0, critical_chance=0, armor_type=None):
        Armor._id += 1
        self._id = Armor._id
        self.name = name
        self.armor = armor
        self.durability = durability
        self.hp = hp
        self.luck = luck
        self.strength = strength
        self.agility = agility
        self.movement = movement
        self.intelligence = intelligence
        self.critical_chance = critical_chance
        self.armor_type = armor_type

    @property
    def armor_chr(self):
        """Creates the dictionary that has all characteristics of a weapon even if they are equal to 0."""
        arm = dict(name=self.name, armor=self.armor, durability=self.durability, hp=self.hp, luck=self.luck,
                   strength=self.strength, agility=self.agility, movement=self.movement,
                   intelligence=self.intelligence, critical_chance=self.critical_chance)
        return arm

    @property
    def print_arm_chr(self):
        """Creates a dict that has only weapon values NOT equal to Zero, even if they are negative"""
        arm_chr = {key: value for (key, value) in self.armor_chr.items() if value}
        for k, v in arm_chr.items():
            print(k.capitalize(), ':', v)


class Helmet(Armor):
    """Everything that will be on your head"""

    def __init__(self, name, armor, durability, hp=0, luck=0, strength=0, agility=0,
                 movement=0, intelligence=0, critical_chance=0, armor_type=None):
        super().__init__(name, armor, durability, hp, luck, strength, agility,
                         movement, intelligence, critical_chance, armor_type)
        self.armor_type = 'helmet'


class Jacket(Armor):
    """Jacket has sleeves so it protect torso and both hands"""

    def __init__(self, name, armor, durability, hp=0, luck=0, strength=0, agility=0,
                 movement=0, intelligence=0, critical_chance=0, armor_type=None):
        super().__init__(name, armor, durability, hp, luck, strength, agility,
                         movement, intelligence, critical_chance, armor_type)
        self.armor_type = 'jacket'


class Vest(Armor):
    """Vest has not sleeves, so it will protect only torso"""

    def __init__(self, name, armor, durability, hp=0, luck=0, strength=0, agility=0,
                 movement=0, intelligence=0, critical_chance=0, armor_type=None):
        super().__init__(name, armor, durability, hp, luck, strength, agility,
                         movement, intelligence, critical_chance, armor_type)
        self.armor_type = 'vest'


class Armlet(Armor):
    """Will be on your arms, can be used only with Vest or without anything on torso, could be used on both hands"""

    def __init__(self, name, armor, durability, hp=0, luck=0, strength=0, agility=0,
                 movement=0, intelligence=0, critical_chance=0, armor_type=None):
        super().__init__(name, armor, durability, hp, luck, strength, agility,
                         movement, intelligence, critical_chance, armor_type)
        self.armor_type = 'armlet'


class Trousers(Armor):
    """Everything that will be on your legs"""

    def __init__(self, name, armor, durability, hp=0, luck=0, strength=0, agility=0,
                 movement=0, intelligence=0, critical_chance=0, armor_type=None):
        super().__init__(name, armor, durability, hp, luck, strength, agility,
                         movement, intelligence, critical_chance, armor_type)
        self.armor_type = 'trousers'


class Boots(Armor):
    """Everything that will be on your feet"""

    def __init__(self, name, armor, durability, hp=0, luck=0, strength=0, agility=0,
                 movement=0, intelligence=0, critical_chance=0, armor_type=None):
        super().__init__(name, armor, durability, hp, luck, strength, agility,
                         movement, intelligence, critical_chance, armor_type)
        self.armor_type = 'boots'


class Naked(Armor):
    """Just naked"""

    def __init__(self, name, armor, durability=math.inf, hp=0, luck=0, strength=0, agility=0,
                 movement=0, intelligence=0, critical_chance=0, armor_type=None):
        super().__init__(name, armor, durability, hp, luck, strength, agility,
                         movement, intelligence, critical_chance, armor_type)
        self.armor_type = 'naked'
