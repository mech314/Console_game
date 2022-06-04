class Hero:
    """
    Class for a player's hero. Take name, gender, clan, specialization.
    """
    base_hp = 100
    base_luck = 1
    base_strength = 3
    base_agility = 3
    base_movement = 2
    base_intelect = 1
    weapon = None
    skills = {'sword_skill': 0, 'knife_skill': 0, 'axe_skill': 0, 'bow_skill': 0}

    def __init__(self, name, gender, clan):
        self.name = name
        self.gender = gender
        self.clan = clan


class Fighter:
    """
    A swordsman or an axeman, inherits from Hero class. Also takes specialization attribute.
    """

    def __init__(self, name, gender, clan, spec):
        super().__init__(name, gender, clan)
        self.spec = spec

        if self.spec == 'swordsman':            # if a swordsman gets more HP and sword skill
            Hero.sword_skill = 3
            Hero.base_hp = 120
        else:                                   # if an axeman gets more strength and axe skill
            Hero.axe_skill = 3
            Hero.base_strength = 5

    def hit(self, spec):
        pass


class Thief():
    """
    A knifesman, inherits from Hero, takes specialization. Sneaky - high agility, smart - high intelect
    """
    knife_skill = 3

    def __init__(self, name, gender, clan, spec):
        super().__init__(name, gender, clan)
        self.spec = spec

        if self.spec == "sneaky":                       # if sneaky is agile
            Hero.base_agility = 5
        else:                                           # if smart is smart
            Hero.base_intelect = 5


