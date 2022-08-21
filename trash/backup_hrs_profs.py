from game import constants, armor, items, weapon


# class Creature(ABC):
#     def __init__(self, name, gender, clan, lvl=1, exp=0, chr_points=0, hp=100, luck=1, strength=3, agility=3,
#                  movement=2, intelligence=1, critical_chance=0, bag=[], sword_skill=0, knife_skill=0, axe_skill=0,
#                  bow_skill=0, fist_skill=0, head=items.naked, torso=items.naked, left_arm=items.naked,
#                  right_arm=items.naked, legs=items.naked, feet=items.naked, active_weapon=None, active_skill=None):
#         self.name = name  # Name of the character
#         self.gender = gender  # Gender
#         self.clan = clan  # Clan
#         self.lvl = lvl  # Level
#         self.exp = exp  # Experience, will be added after battles etc
#         self.chr_points = chr_points  # Amount of points received with the level_UP.
#         self.hp = hp  # Amount of hit-points
#         self.luck = luck  # How lucky the bastard is
#         self.strength = strength  # Strong man?
#         self.agility = agility  # Agile
#         self.movement = movement  # will be helping to calculate how far hero can go or how many action can perform
#         self.intelligence = intelligence  # How smart
#         self.critical_chance = critical_chance  # A chance to make a critical hit, strikes ignoring armor + 10% dmg
#         self.bag = bag  # A storage for all the shit that Hero has
#         self.sword_skill = sword_skill
#         self.knife_skill = knife_skill
#         self.axe_skill = axe_skill
#         self.bow_skill = bow_skill
#         self.fist_skill = fist_skill
#         self.head = head  # What is on your head
#         self.torso = torso  # What is on your torso
#         self.left_arm = left_arm  # What is on your LEFT ARM
#         self.right_arm = right_arm  # What is on your RIGHT ARM
#         self.legs = legs  # What is on your legs
#         self.feet = feet  # What is on your feet
#         self.active_weapon = active_weapon  # Weapon in hand, if None that use the fist
#         self.active_skill = active_skill  # Skill for the weapon in hand


class Hero:
    """
    Class for a player's hero. Take name, gender, clan, specialization.
    """

    def __init__(self, name, gender, clan, lvl=1, exp=0, chr_points=0, hp=100, luck=1, strength=3, agility=3,
                 movement=2, intelligence=1, critical_chance=0, bag=[], sword_skill=0, knife_skill=0, axe_skill=0,
                 bow_skill=0, fist_skill=0, head=items.naked, torso=items.naked, left_arm=items.naked,
                 right_arm=items.naked, legs=items.naked, feet=items.naked, active_weapon=None, active_skill=None):
        self.name = name  # Name of the character
        self.gender = gender  # Gender
        self.clan = clan  # Clan
        self.lvl = lvl  # Level
        self.exp = exp  # Experience, will be added after battles etc
        self.chr_points = chr_points  # Amount of points received with the level_UP.
        self.hp = hp  # Amount of hit-points
        self.luck = luck  # How lucky the bastard is
        self.strength = strength  # Strong man?
        self.agility = agility  # Agile
        self.movement = movement  # will be helping to calculate how far hero can go or how many action can perform
        self.intelligence = intelligence  # How smart
        self.critical_chance = critical_chance  # A chance to make a critical hit, strikes ignoring armor + 10% dmg
        self.bag = bag  # A storage for all the shit that Hero has
        self.sword_skill = sword_skill
        self.knife_skill = knife_skill
        self.axe_skill = axe_skill
        self.bow_skill = bow_skill
        self.fist_skill = fist_skill
        self.head = head  # What is on your head
        self.torso = torso  # What is on your torso
        self.left_arm = left_arm  # What is on your LEFT ARM
        self.right_arm = right_arm  # What is on your RIGHT ARM
        self.legs = legs  # What is on your legs
        self.feet = feet  # What is on your feet
        self.active_weapon = active_weapon  # Weapon in hand, if None that use the fist
        self.active_skill = active_skill  # Skill for the weapon in hand
        self.head_armor = self.head.damage
        self.torso_armor = self.torso.damage
        self.left_arm_armor = self.left_arm.damage
        self.right_arm_armor = self.right_arm.damage
        self.legs_armor = self.legs.damage
        self.feet_armor = self.feet.damage

    @property
    def skills(self):
        """Returns all skills as a dict"""
        return dict(sword=self.sword_skill, knife=self.knife_skill, axe=self.axe_skill, bow=self.bow_skill,
                    fist=self.fist_skill)

    @property
    def characteristics(self):
        """Return all Hero's characteristics as a dict"""
        return dict(hp=self.hp, strength=self.strength, agility=self.agility, luck=self.luck,
                    movement=self.movement, intelligence=self.intelligence, critical_chance=self.critical_chance)

    def print_chr(self):
        """Prints all character characteristics"""
        for k, v in self.characteristics.items():
            print(k.capitalize(), ':', v)

    def level_up(self):
        """
        A property that will check for the amount of experience. If it exceeds certain amount will increase Hero's level
        """
        if self.exp >= self.lvl * 100:
            self.lvl += 1
            self.chr_points += 5
            print("Congratulations, you have reached {} level, you have {} free "
                  "points to make yourself better".format(self.lvl, self.chr_points))
            flag = True
            while flag:
                response = input(str('Do you want to improve your characteristics? Yes or No?'))
                if response.lower() == 'yes':
                    if self.chr_points > 0:
                        self.use_chr_points()
                        flag = False
                    else:
                        print('You have no available improvement points, wait for level up')
                        break
                elif response.lower() == 'no':
                    print('You can do it later, just call self.level_up()')
                    flag = False
                else:
                    print('You should say yes or no, no other words will be recognised by your brain')

    def use_chr_points(self):
        """Supposed to allow user to distribute chr_points to increase characteristics"""
        while self.chr_points:  # While there is something in chr_points
            choice = input(str('What characteristic you want to improve: a) strength, b) agility, c) luck, '
                               'd) movement, f) intelligence'))
            if choice.lower() == 'a' and 'strength':
                self.strength += 1
                self.chr_points -= 1
                print("Your Strength is {}".format(self.strength))
            elif choice.lower() == 'b' and 'agility':
                self.agility += 1
                self.chr_points -= 1
                print("Your Agility is {}".format(self.agility))
            elif choice.lower() == 'c' and 'luck':
                self.luck += 1
                self.chr_points -= 1
                print("Your Luck is {}".format(self.luck))
            elif choice.lower() == 'd' and 'movement':
                self.movement += 1
                self.chr_points -= 1
                print("Your Movement is {}".format(self.movement))
            elif choice.lower() == 'f' and 'intelligence':
                self.intelligence += 1
                self.chr_points -= 1
                print("Your Intelligence is {}".format(self.intelligence))
        print("Your character's characteristics are:")
        self.print_chr()

    def add_item_to_thebag(self, item):
        """Adds item to the bag"""
        self.bag.append(item)

    @property
    def bag_content(self):
        return self.bag

    def printbag_cnt(self):
        for count, item in enumerate(self.bag):
            print(count, item.name)

    def choose_weapon(self, choice):
        """Selecting the weapon from the bag and adds-up all the characteristic to self.whatever_chr_is"""
        item = self.bag_content[choice]
        if isinstance(item, weapon.Weapon):
            self.active_weapon = self.bag_content[choice]
            self.active_skill = self.skills[self.active_weapon.weapon_type]
            self.hp += self.active_weapon.base_hp
            self.luck += self.active_weapon.luck
            self.strength += self.active_weapon.strength
            self.agility += self.active_weapon.agility
            self.movement += self.active_weapon.movement
            self.intelligence += self.active_weapon.intelligence
            self.critical_chance += self.active_weapon.critical_chance
            print(f'You have {item.name.lower()} in your hand')
            return self.active_skill
        else:
            print(f'You are trying to fight with {item.name.lower()}, are you too smart?')

    def put_on_armor(self, choice):
        """Puts your helmet on your head"""
        item = self.bag_content[choice]
        if isinstance(item, armor.Armor):
            if item.weapon_type == 'jacket':  # Put jacket on body, gives armor for hands and torso
                print(f'You put {item.name} on your body')
                self.torso = self.bag_content[choice]
                self.torso_armor = item.damage
                self.left_arm_armor = item.damage
                self.right_arm_armor = item.damage
            elif item.weapon_type == 'vest':  # Put vest, naked arms but can put armlets now
                print(f'You put {item.name} on your body, you can put armlets as well')
                self.torso = self.bag_content[choice]
                self.torso_armor = item.damage
            elif item.weapon_type == 'armlet':
                flag = True
                while flag:
                    if self.torso.weapon_type != 'jacket':  # Can put armlets only with vest or naked
                        hand = input('Put on left or right hand?')
                        if hand.lower() == 'left':
                            print(f'You put {item.name} on your left hand')
                            self.left_arm = self.bag_content[choice]
                            self.left_arm_armor = item.damage
                            flag = False
                        elif hand.lower() == 'right':
                            print(f'You put {item.name} on your right hand')
                            self.right_arm = self.bag_content[choice]
                            self.right_arm_armor = item.damage
                            flag = False
                        else:
                            print(f'Choose the hand on which you wanna put {item.name}')
                    else:
                        print(f'You cannot put armlets on because you are wearing {self.torso.name}')
            elif item.weapon_type == 'trousers':  # Same story with pants
                print(f'You put {item.name} on legs')
                self.legs = self.bag_content[choice]
                self.legs_armor = item.damage
            elif item.weapon_type == 'boots':  # Same story with boots
                print(f'You put {item.name} on your feet')
                self.feet = self.bag_content[choice]
                self.feet_armor = item.damage
            elif item.weapon_type == 'helmet':  # Same story with helmet
                print(f'You put {item.name} on your head')
                self.head = self.bag_content[choice]
                self.head_armor = item.damage
            self.hp += item.base_hp  # Now adds up all characteristics of a cloth to character's chr.
            self.luck += item.luck
            self.strength += item.strength
            self.agility += item.agility
            self.movement += item.movement
            self.intelligence += item.intelligence
            self.critical_chance += item.critical_chance

        else:
            print(f'You are trying to put {item.name.lower()} on your head, think one more time.')

    def calc_dmg(self):
        if not self.active_weapon:
            self.active_weapon = weapon.Fist()
            self.active_skill = self.skills['fist']
        modifier = 1 + (self.strength / 100) + (self.agility / 150) + (self.active_skill / 10)
        return int(modifier * random.randint(self.active_weapon.damage[0], self.active_weapon.damage[1]))

    def chance_of_critical_strike(self):
        """Calculates chance for critical damage based on character's self.critical_chance value,
        returns True if chance is within default 5%, players self.critical_chance increases the probability by
        lowering the random range"""
        chance = random.randint(self.critical_chance, 100)
        return True if chance in range(95, 100) else False

    def hit_enemy(self, target):
        """Calculates the damage from a weapon based on chr characteristics"""
        active_armor = ()
        hit_choice = ''
        critical = False
        flag = True
        while flag:
            where_to_hit = input(
                'Where you want to hit your enemy? a)Head, b)Torso, c)Left hand, d)Right hand, f) legs')
            if where_to_hit.lower() == "a" and 'head':
                hit_choice = 'head'
                active_armor = target.head_armor
                flag = False
            elif where_to_hit.lower() == 'b' and 'torso':
                hit_choice = 'torso'
                active_armor = target.torso_armor
                flag = False
            elif where_to_hit.lower() == 'c' and 'left hand':
                hit_choice = 'left arm'
                active_armor = target.left_arm_armor
                flag = False
            elif where_to_hit.lower() == 'd' and 'right hand':
                hit_choice = 'right arm'
                active_armor = target.right_arm_armor
                flag = False
            elif where_to_hit.lower() == 'f' and 'legs':
                hit_choice = 'legs'
                active_armor = int(target.legs_armor[0] + (target.feet_armor[0] / 7)), int(
                    target.legs_armor[1] + (target.feet_armor[1] / 7))
                flag = False
            else:
                print(
                    "You trying to hit an imaginary part of {}'s body, maybe it is not a good idea".format(enemy.name))
        armor_value = int(random.randint(active_armor[0], active_armor[1]))
        if self.chance_of_critical_strike():
            damage = int(self.calc_dmg() * 1.5)
            critical = True
        else:
            damage = self.calc_dmg() - armor_value
        return (0, hit_choice, critical) if damage < 0 else (damage, hit_choice, critical)


# class Enemy(Creature):
#     def __init__(self, name, gender, clan, lvl=1, exp=0, chr_points=0, hp=100, luck=1, strength=3, agility=3,
#                  movement=2, intelligence=1, critical_chance=0, bag=[], sword_skill=0, knife_skill=0, axe_skill=0,
#                  bow_skill=0, fist_skill=0, head=items.naked, torso=items.naked, left_arm=items.naked,
#                  right_arm=items.naked, legs=items.naked, feet=items.naked, active_weapon=None, active_skill=None):
#         super().__init__(name, gender, clan, lvl, exp, chr_points, hp, luck, strength, agility, movement, intelligence,
# #                          critical_chance, bag, sword_skill, knife_skill, axe_skill, bow_skill, fist_skill, head, torso,
# #                          left_arm, right_arm, legs, feet, active_weapon, active_skill)
# #         self.apply_default_chr()
# #
# #     def apply_default_chr(self):
# #         # self.head_armor = self.head.armor
# #         if self.torso.armor_type == 'jacket':
# #             self.torso_armor = self.torso.armor
# #             self.left_arm_armor = self.torso.armor
# #             self.right_arm_armor = self.torso.armor
# #         elif self.torso.armor_type == 'vest' or 'naked':
# #             self.torso_armor = self.torso.armor
# #         self.feet_armor = self.feet.armor
# #         self.legs_armor = self.legs.armor
#
#
#
#     @property
#     def skills(self):
#         """Returns all skills as a dict"""
#         return dict(sword=self.sword_skill, knife=self.knife_skill, axe=self.axe_skill, bow=self.bow_skill,
#                     fist=self.fist_skill)
#
#     def calc_dmg(self):
#         self.active_skill = self.skills[self.active_weapon.weapon_type]
#         print(self.active_skill)
#         modifier = 1 + (self.strength / 100) + (self.agility / 150) + (self.active_skill / 10)
#         return int(modifier * random.randint(self.active_weapon.damage[0], self.active_weapon.damage[1]))
#
#     def chance_of_critical_strike(self):
#         """Calculates chance for critical damage based on character's self.critical_chance value,
#         returns True if chance is within default 5%, players self.critical_chance increases the probability by
#         lowering the random range"""
#         chance = random.randint(self.critical_chance, 100)
#         return True if chance in range(95, 100) else False
#
#     def hit_player(self, player):
#         """Calculates the damage from a weapon based on chr charactetistics"""
#         hit_choice = ''
#         critical = False
#         active_armor = ()
#         random_where_to_hit = random.randint(1, 5)
#         if random_where_to_hit == 1:
#             hit_choice = 'head'
#             active_armor = player.head_armor
#         elif random_where_to_hit == 2:
#             hit_choice = 'torso'
#             active_armor = player.torso_armor
#         elif random_where_to_hit == 3:
#             hit_choice = 'left arm'
#             active_armor = player.left_arm_armor
#         elif random_where_to_hit == 4:
#             hit_choice = 'right arm'
#             active_armor = player.right_arm_armor
#         elif random_where_to_hit == 5:
#             hit_choice = 'legs'
#             active_armor = int(player.leg_armor[0] + (player.feet_armor[0]) / 7), int(
#                 player.leg_armor[1] + (player.feet_armor[1] / 7))
#         armor_value = int(random.randint(active_armor[0], active_armor[1]))
#         if self.chance_of_critical_strike():
#             damage = int(self.calc_dmg() * 1.5)
#             critical = True
#         else:
#             damage = self.calc_dmg() - armor_value
#         return (0, hit_choice, critical) if damage < 0 else (damage, hit_choice, critical)


class Fighter(Hero):
    """
    A swordsman or an axeman, inherits from Hero class. Also takes specialization attribute.
    """

    def __init__(self, name, gender, clan, lvl=1, exp=0, chr_points=0, hp=100, luck=1, strength=3, agility=3,
                 movement=2, intelligence=1, critical_chance=0, bag=[], sword_skill=0, knife_skill=0, axe_skill=0,
                 bow_skill=0, fist_skill=0, head=items.naked, torso=items.naked, left_arm=items.naked,
                 right_arm=items.naked, legs=items.naked, feet=items.naked, active_weapon=None, spec=None):
        super().__init__(name, gender, clan, lvl, exp, chr_points, hp, luck, strength, agility, movement, intelligence,
                         critical_chance, bag, sword_skill, knife_skill, axe_skill, bow_skill, fist_skill, head, torso,
                         left_arm, right_arm, legs, feet, active_weapon, spec)
        self.spec = spec
        if self.spec == constants.SWORDSMAN:  # if a swordsman gets more HP and sword skill
            self.sword_skill = 3
            self.hp += 30 * self.lvl
        elif self.spec == constants.AXEMAN:  # if an axeman gets more strength and axe skill
            self.axe_skill = 3
            self.strength = 5
            self.critical_chance = 10


class Thief(Hero):
    """
    A knifesman, inherits from Hero, takes specialization. Sneaky - high agility, smart - high intelect
    """

    def __init__(self, name, gender, clan, spec):
        super().__init__(name, gender, clan)
        self.spec = spec

        if self.spec == "sneaky":  # if sneaky is agile
            self.agility = 5
        else:  # if smart is smart
            self.intelligence = 5


import random


class Enemy():
    def __init__(self, name, gender, clan, lvl=1, exp=0, chr_points=0, hp=100, luck=1, strength=3, agility=3,
                 movement=2, intelligence=1, critical_chance=0, bag=[], sword_skill=0, knife_skill=0, axe_skill=0,
                 bow_skill=0, fist_skill=0, head=items.naked, torso=items.naked, left_arm=items.naked,
                 right_arm=items.naked, legs=items.naked, feet=items.naked, active_weapon=None, active_skill=None):
        self.name = name  # Name of the character
        self.gender = gender  # Gender
        self.clan = clan  # Clan
        self.lvl = lvl  # Level
        self.exp = exp  # Experience, will be added after battles etc
        self.chr_points = chr_points  # Amount of points received with the level_UP.
        self.hp = hp  # Amount of hit-points
        self.luck = luck  # How lucky the bastard is
        self.strength = strength  # Strong man?
        self.agility = agility  # Agile
        self.movement = movement  # will be helping to calculate how far hero can go or how many action can perform
        self.intelligence = intelligence  # How smart
        self.critical_chance = critical_chance  # A chance to make a critical hit, strikes ignoring armor + 10% dmg
        self.bag = bag  # A storage for all the shit that Hero has
        self.sword_skill = sword_skill
        self.knife_skill = knife_skill
        self.axe_skill = axe_skill
        self.bow_skill = bow_skill
        self.fist_skill = fist_skill
        self.head = head  # What is on your head
        self.torso = torso  # What is on your torso
        self.left_arm = left_arm  # What is on your LEFT ARM
        self.right_arm = right_arm  # What is on your RIGHT ARM
        self.legs = legs  # What is on your legs
        self.feet = feet  # What is on your feet
        self.active_weapon = active_weapon  # Weapon in hand, if None that use the fist
        self.active_skill = active_skill  # Skill for the weapon in hand
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
            active_armor = int(player.legs_armor[0] + (player.feet_armor[0]) / 7), int(player.legs_armor[1] + (player.feet_armor[1] / 7))
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
                 right_arm=items.naked, legs=items.naked, feet=items.naked, active_weapon=None, active_skill=None, ):
        super().__init__(name, gender, clan, lvl, exp, chr_points, hp, luck, strength, agility, movement, intelligence,
                         critical_chance, bag, sword_skill, knife_skill, axe_skill, bow_skill, fist_skill,
                         head, torso, left_arm, right_arm, legs, feet, active_weapon, active_skill)
        self.spec = spec
        if self.spec == constants.SWORDSMAN:  # if a swordsman gets more HP and sword skill
            self.sword_skill = 3
            self.hp += 30 * self.lvl
        elif self.spec == constants.AXEMAN:  # if an axeman gets more strength and axe skill
            self.axe_skill = 3
            self.strength = 5
            self.critical_chance = 10
