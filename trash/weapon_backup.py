class Weapon:
    _id = 0
    """ Weapon class, takes damage, durability, weapon_type, hp=0, luck=0, strength=0, agility=0,
        movement=0, intelligence=0, critical_chance=0.
        Weapon type will be defined in daughter classes and should not be defined elsewhere.
        Other parameters will indicate bonus to a player who is holding this weapon
    """

    def __init__(self, name, damage, level=1, durability=None, hp=0, luck=0, strength=0, agility=0,
                 movement=0, intelligence=0, critical_chance=0, _weapon_type=None):
        Weapon._id += 1
        self._id = Weapon._id
        self.name = name
        self.damage = damage
        self.level = level
        self.durability = durability
        self.hp = hp
        self.luck = luck
        self.strength = strength
        self.agility = agility
        self.movement = movement
        self.intelligence = intelligence
        self.critical_chance = critical_chance
        self._weapon_type = _weapon_type

    @property
    def weapon_chr(self):
        """Creates the dictionary that has all characteristics of a weapon even if they are equal to 0."""
        wpn = dict(name=self.name, damage=self.damage, durability=self.durability, hp=self.hp, luck=self.luck,
                   strength=self.strength, agility=self.agility, movement=self.movement,
                   intelligence=self.intelligence, critical_chance=self.critical_chance)
        return wpn

    @property
    def print_wpn_chr(self):
        """Creates a dict that has only weapon values NOT equal to Zero, even if they are negative"""
        wpn_chr = {key: value for (key, value) in self.weapon_chr.items() if value}
        for k, v in wpn_chr.items():
            print(k.capitalize(), ':', v)

    # def __str__(self):
    #     return str(self.name) + ' ' + str(self.damage) + ' ' + str(self.durability)
    #
    # def __repr__(self):
    #     return str(self.name) + ' ' + str(self.damage) + ' ' + str(self.durability)


class Fist(Weapon):

    def __init__(self, name, damage=None, weapon_type=None):
        super().__init__(damage, name, weapon_type)
        self.name = name
        self.damage = (1, 5)
        self.weapon_type = 'fist'


class Sword(Weapon):

    def __init__(self, name, damage, durability, level=1, hp=0, luck=0, strength=0, agility=0,
                 movement=0, intelligence=0, critical_chance=0, weapon_type=None):
        super().__init__(name, damage, durability, level, hp, luck, strength, agility,
                         movement, intelligence, critical_chance, weapon_type)
        self.weapon_type = 'sword'


class Axe(Weapon):

    def __init__(self, name, damage, durability, level=1, hp=0, luck=0, strength=0, agility=0,
                 movement=0, intelligence=0, critical_chance=0, weapon_type=None):
        super().__init__(name, damage, durability, level, hp, luck, strength, agility,
                         movement, intelligence, critical_chance, weapon_type)
        self.weapon_type = 'axe'


class Knife(Weapon):

    def __init__(self, name, damage, durability, level=1, hp=0, luck=0, strength=0, agility=0,
                 movement=0, intelligence=0, critical_chance=0, weapon_type=None):
        super().__init__(name, damage, durability, level, hp, luck, strength, agility,
                         movement, intelligence, critical_chance, weapon_type)
        self.weapon_type = "knife"


class Bow(Weapon):

    def __init__(self, name, damage, durability, level=1, hp=0, luck=0, strength=0, agility=0,
                 movement=0, intelligence=0, critical_chance=0, weapon_type=None):
        super().__init__(name, damage, durability, level, hp, luck, strength, agility,
                         movement, intelligence, critical_chance, weapon_type)
        self.weapon_type = "bow"


