import random
from game import constants, items, hrs_profs


class Enemy(hrs_profs.Creature):

    def __init__(self,
                 name,
                 gender,
                 clan,
                 lvl=1,
                 exp=0,
                 chr_points=0,
                 hp=100,
                 luck=1,
                 strength=3,
                 agility=3,
                 movement=2,
                 intelligence=1,
                 critical_chance=0,
                 bag=[],
                 what_is_on=[],
                 sword_skill=0,
                 knife_skill=0,
                 axe_skill=0,
                 bow_skill=0,
                 fist_skill=0,
                 head=items.naked,
                 torso=items.naked,
                 left_arm=items.naked,
                 right_arm=items.naked,
                 legs=items.naked,
                 feet=items.naked,
                 active_weapon='fist',
                 active_skill=0,
                 cht_type='npc',
                 spec=None):

        super().__init__(name,
                         gender,
                         clan,
                         lvl,
                         exp,
                         chr_points,
                         hp,
                         luck,
                         strength,
                         agility,
                         movement,
                         intelligence,
                         critical_chance,
                         bag,
                         what_is_on,
                         sword_skill,
                         knife_skill,
                         axe_skill,
                         bow_skill,
                         fist_skill,
                         head,
                         torso,
                         left_arm,
                         right_arm,
                         legs,
                         feet,
                         active_weapon,
                         active_skill,
                         cht_type,
                         spec)
        self.apply_default_chr()

    def apply_default_chr(self):
        self.head_armor = self.head.damage
        if self.torso.weapon_type == 'jacket':
            self.torso_armor = self.torso.damage
            self.left_arm_armor = self.torso.damage
            self.right_arm_armor = self.torso.damage
        elif self.torso.weapon_type == 'vest' or 'naked':
            self.torso_armor = self.torso.damage
        self.feet_armor = self.feet.damage
        self.legs_armor = self.legs.damage

    @property
    def skills(self):
        """Returns all skills as a dict"""
        return dict(sword=self.sword_skill, knife=self.knife_skill, axe=self.axe_skill, bow=self.bow_skill,
                    fist=self.fist_skill)

    def calc_dmg(self):
        self.active_skill = self.skills[self.active_weapon.weapon_type]
        modifier = 1 + (self.strength / 100) + (self.agility / 150) + (self.active_skill / 10)
        return int(modifier * random.randint(self.active_weapon.damage[0], self.active_weapon.damage[1]))

    def chance_of_critical_strike(self):
        """Calculates chance for critical damage based on character's self.critical_chance value,
        returns True if chance is within default 5%, players self.critical_chance increases the probability by
        lowering the random range"""
        chance = random.randint(self.critical_chance, 100)
        return True if chance in range(95, 100) else False

    def hit_player(self, player):
        """Calculates the damage from a weapon based on chr charactetistics"""
        hit_choice = ''
        critical = False
        active_armor = ()
        random_where_to_hit = random.randint(1, 5)
        if random_where_to_hit == 1:
            hit_choice = 'head'
            active_armor = player.head_armor
        elif random_where_to_hit == 2:
            hit_choice = 'torso'
            active_armor = player.torso_armor
        elif random_where_to_hit == 3:
            hit_choice = 'left arm'
            active_armor = player.left_arm_armor
        elif random_where_to_hit == 4:
            hit_choice = 'right arm'
            active_armor = player.right_arm_armor
        elif random_where_to_hit == 5:
            hit_choice = 'legs'
            active_armor = int(player.legs_armor[0] + (player.feet_armor[0]) / 7), int(
                player.legs_armor[1] + (player.feet_armor[1] / 7))
        armor_value = int(random.randint(active_armor[0], active_armor[1]))
        if self.chance_of_critical_strike():
            damage = int(self.calc_dmg() * 1.5)
            critical = True
        else:
            damage = self.calc_dmg() - armor_value
        return (0, hit_choice, critical) if damage < 0 else (damage, hit_choice, critical)


class Enemy_Fighter(Enemy):
    """
    A swordsman or an axeman, inherits from Hero class. Also takes specialization attribute.
    """

    def __init__(self, name, gender, clan, spec, lvl=1, exp=0, chr_points=0, hp=100, luck=1, strength=3, agility=3,
                 movement=2, intelligence=1, critical_chance=10, bag=[], sword_skill=0, knife_skill=0, axe_skill=0,
                 bow_skill=0, fist_skill=0, head=items.naked, torso=items.naked, left_arm=items.naked,
                 right_arm=items.naked, legs=items.naked, feet=items.naked, active_weapon=items.fist,
                 active_skill=None):
        super().__init__(name, gender, clan, lvl, exp, chr_points, hp, luck, strength, agility, movement, intelligence,
                         critical_chance, bag, sword_skill, knife_skill, axe_skill, bow_skill, fist_skill,
                         head, torso, left_arm, right_arm, legs, feet, active_weapon, active_skill)
        self.spec = spec
        self.active_skill = self.skills[self.active_weapon.weapon_type]
        if self.spec == constants.SWORDSMAN:  # if a swordsman gets more HP and sword skill
            self.sword_skill = 3
            self.hp += 30 * self.lvl
        elif self.spec == constants.AXEMAN:  # if an axeman gets more strength and axe skill
            self.axe_skill = 3
            self.strength = 5
            self.critical_chance = 10


class Axeman(Enemy):
    """
    A swordsman or an axeman, inherits from Enemy class. Also takes specialization attribute.
    """

    def __init__(self,
                 name,
                 gender,
                 clan,
                 lvl=1,
                 exp=0,
                 chr_points=0,
                 hp=100,
                 luck=1,
                 strength=5,
                 agility=3,
                 movement=2,
                 intelligence=1,
                 critical_chance=0,
                 bag=[],
                 what_is_on=[],
                 sword_skill=0,
                 knife_skill=0,
                 axe_skill=0,
                 bow_skill=0,
                 fist_skill=0,
                 head=items.naked,
                 torso=items.naked,
                 left_arm=items.naked,
                 right_arm=items.naked,
                 legs=items.naked,
                 feet=items.naked,
                 active_weapon=items.fist,
                 cht_type='npc',
                 spec=None):
        super().__init__(name,
                         gender,
                         clan,
                         lvl,
                         exp,
                         chr_points,
                         hp,
                         luck,
                         strength,
                         agility,
                         movement,
                         intelligence,
                         critical_chance,
                         bag,
                         what_is_on,
                         sword_skill,
                         knife_skill,
                         axe_skill,
                         bow_skill,
                         fist_skill,
                         head,
                         torso,
                         left_arm,
                         right_arm,
                         legs,
                         feet,
                         active_weapon,
                         cht_type,
                         spec)
        self.spec = spec
        self.axeman_bonuses()
        if self.chr_type == 'npc':
            self.npc_weapon()
            self.npc_clothes()

    def npc_weapon(self):
        self.active_skill = self.skills[self.active_weapon.weapon_type]
        self.hp += self.active_weapon.hp
        self.luck += self.active_weapon.luck
        self.strength += self.active_weapon.strength
        self.agility += self.active_weapon.agility
        self.movement += self.active_weapon.movement
        self.intelligence += self.active_weapon.intelligence
        self.critical_chance += self.active_weapon.critical_chance
        return self.active_skill

    def npc_clothes(self):
        self.hp += (self.head.hp + self.torso.hp + self.left_arm.hp + self.right_arm.hp + self.legs.hp + self.feet.hp)
        self.luck += (self.head.luck + self.torso.luck + self.left_arm.luck + self.right_arm.luck + self.legs.luck +
                      self.feet.luck)
        self.strength += (self.head.strength + self.torso.strength + self.left_arm.strength + self.right_arm.strength +
                          self.legs.strength + self.feet.strength)
        self.agility += (self.head.agility + self.torso.agility + self.left_arm.agility + self.right_arm.agility +
                         self.legs.agility + self.feet.agility)
        self.movement += (self.head.movement + self.torso.movement + self.left_arm.movement + self.right_arm.movement +
                          self.legs.movement + self.feet.movement)
        self.intelligence += (self.head.intelligence + self.torso.intelligence + self.left_arm.intelligence +
                              self.right_arm.intelligence + self.legs.intelligence + self.feet.intelligence)
        self.critical_chance += (self.head.critical_chance + self.torso.critical_chance + self.left_arm.critical_chance
                                 + self.right_arm.critical_chance + self.legs.critical_chance + self.feet.critical_chance)

    def axeman_bonuses(self):
        self.critical_chance += 10
        self.axe_skill = 3
