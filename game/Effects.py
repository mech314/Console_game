from dataclasses import dataclass


class Effects:
    def __init__(self,
                 effect_name,
                 hp: int = 0,
                 luck=0,
                 strength=0,
                 agility=0,
                 movement=0,
                 intelligence=0,
                 critical_chance=0,
                 sword_skill=0,
                 knife_skill=0,
                 axe_skill=0,
                 bow_skill=0,
                 fist_skill=0):
        self.effect_name = effect_name
        self.hp = hp  # Amount of hit-points
        self.luck = luck  # How lucky the bastard is
        self.strength = strength  # Strong man?
        self.agility = agility  # Agile
        self.movement = movement  # will be helping to calculate how far hero can go or how many action can perform
        self.intelligence = intelligence  # How smart
        self.critical_chance = critical_chance  # A chance to make a critical hit, strikes ignoring armor + 10% dmg
        self.sword_skill = sword_skill
        self.knife_skill = knife_skill
        self.axe_skill = axe_skill
        self.bow_skill = bow_skill
        self.fist_skill = fist_skill


no_effect = Effects(effect_name="no effect")
city = Effects(effect_name="city", hp=int(-10), luck=10)
desert = Effects(effect_name="desert", hp=1, movement=-10, luck=15)