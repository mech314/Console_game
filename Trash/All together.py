import random


class Hero:
    """
    Class for a player's hero. Take name, gender, clan, specialization.
    """
    def __init__(self, name, gender, clan, hp=100, luck=1, strength=3, agility=3, movement=2, intelligence=1,
                 bag=None, skills=None):
        if skills is None:
            skills = {'sword_skill': 0, 'knife_skill': 0, 'axe_skill': 0, 'bow_skill': 0}
        if bag is None:
            bag = {"sword": (10, 20)}
        self.name = name
        self.gender = gender
        self.clan = clan
        self.hp = hp
        self.luck = luck
        self.strength = strength
        self.agility = agility
        self.movement = movement
        self.intelligence = intelligence
        self.bag = bag
        self.skills = skills

    def hit_enemy(self, whom_to_hit):
        """Calculates the damage from a weapon based on chr charactetistics and hits the target"""
        modifier = 1 + (self.strength / 100) + (self.agility / 150) + (self.skills['sword_skill'] / 10)
        dmg = modifier * random.randint(self.bag['sword'][0], self.bag['sword'][1])
        whom_to_hit.hp -= dmg
        return whom_to_hit.hp


class Fighter(Hero):
    """
    A swordsman or an axeman, inherits from Hero class. Also takes specialization attribute.
    """

    def __init__(self, name, gender, clan, spec):
        super().__init__(name, gender, clan)
        self.spec = spec

        if self.spec == 'swordsman':            # if a swordsman gets more HP and sword skill
            self.skills['sword_skill'] = 3
            self.hp = 120
        else:                                   # if an axeman gets more strength and axe skill
            self.skills['axe_skill'] = 3
            self.strength = 5


player1 = Fighter('Mech', "Male", 'Boyz', 'swordsman')
enemy = Hero('BadBoy', 'Male', 'Enemy')

print(player1.skills)
print(enemy.skills)
print(enemy.hp)
print(player1.hp)
print(player1.hit_enemy(enemy))
print(enemy.hp)
print(player1.hp)
