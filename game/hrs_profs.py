from abc import ABC
import random
from console_game.game import weapon
from console_game.game import armor
from console_game.game import items


class Creature(ABC):
    def __init__(self,
                 name,
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
                 chr_type,
                 spec):
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
        self._bag = bag  # A storage for all the shit that Hero has
        self._what_is_on = what_is_on  # List that contains all clothes on a hero. Pop them from _bag when you put them
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
        self.active_weapon = active_weapon  # Weapon in hand, if None than use the fist
        self.active_skill = active_skill  # Skill for the weapon in hand
        self.head_armor = self.head.armor
        self.torso_armor = self.torso.armor
        self.left_arm_armor = self.left_arm.armor
        self.right_arm_armor = self.right_arm.armor
        self.legs_armor = self.legs.armor
        self.feet_armor = self.feet.armor
        self.chr_type = chr_type  # NPC of Player
        self.spec = spec  # specialization


class Hero(Creature):
    """
    Class for a player's hero. Take name, gender, clan, specialization.
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
        """Prints name and all character characteristics"""
        print("{}'s characteristics are: ".format(self.name))
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

    def add_item_to_the_bag(self, item):
        """Adds item to the bag"""
        self._bag.append(item)

    @property
    def bag_content(self):
        return self._bag

    def print_bag_cnt(self):
        for count, item in enumerate(self._bag):
            print(count, item.name)

    def choose_weapon(self, choice):
        """Selecting the weapon from the bag and adds-up all the characteristic to self.whatever_chr_is"""
        item = self.bag_content[choice]
        if isinstance(item, weapon.Weapon):
            self.active_weapon = self.bag_content[choice]
            self.active_skill = self.skills[self.active_weapon.weapon_type]
            self.hp += self.active_weapon.hp
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

    def put_on_armor(self, choice=None):
        """Puts a piece of armor on you"""
        print(choice)
        if choice is None:
            print("This is what you have in your bag: ")
            self.print_bag_cnt()
            choice = input('What do you want to put on:')
            if choice == "no":
                return None
        item = self.bag_content[int(choice)]
        if isinstance(item, armor.Armor):
            if item.armor_type == 'jacket':  # Put jacket on body, gives armor for hands and torso
                print(f'You put {item.name} on your body')
                self.torso = self.bag_content[int(choice)]
                self.torso_armor = item.armor
                self.left_arm_armor = item.armor
                self.right_arm_armor = item.armor
            elif item.armor_type == 'vest':  # Put vest, naked arms but can put armlets now
                print(f'You put {item.name} on your body, you can put armlets as well')
                self.torso = self.bag_content[int(choice)]
                self.torso_armor = item.armor
            elif item.armor_type == 'armlet':
                flag = True
                while flag:
                    if self.torso.armor_type != 'jacket':  # Can put armlets only with vest or naked
                        hand = input('Put on left or right hand?')
                        if hand.lower() == 'left':
                            print(f'You put {item.name} on your left hand')
                            self.left_arm = self.bag_content[int(choice)]
                            self.left_arm_armor = item.armor
                            flag = False
                        elif hand.lower() == 'right':
                            print(f'You put {item.name} on your right hand')
                            self.right_arm = self.bag_content[int(choice)]
                            self.right_arm_armor = item.armor
                            flag = False
                        else:
                            print(f'Choose the hand on which you wanna put {item.name}')
                    else:
                        print(f'You cannot put armlets on because you are wearing {self.torso.name}')
            elif item.armor_type == 'trousers':  # Same story with pants
                print(f'You put {item.name} on legs')
                self.legs = self.bag_content[int(choice)]
                self.legs_armor = item.armor
            elif item.armor_type == 'boots':  # Same story with boots
                print(f'You put {item.name} on your feet')
                self.feet = self.bag_content[int(choice)]
                self.feet_armor = item.armor
            elif item.armor_type == 'helmet':  # Same story with helmet
                print(f'You put {item.name} on your head')
                self.head = self.bag_content[int(choice)]
                self.head_armor = item.armor
            self.hp += item.hp  # Now adds up all characteristics of a cloth to character's chr.
            self.luck += item.luck
            self.strength += item.strength
            self.agility += item.agility
            self.movement += item.movement
            self.intelligence += item.intelligence
            self.critical_chance += item.critical_chance
            self._what_is_on.append(self._bag.pop(int(choice)))

        else:
            print(f'You are trying to put {item.name.lower()} on your head, think one more time.')
        print("Bag contents: ")
        self.print_bag_cnt()
        more_clothes = input('Do you want to put something else? ')
        if str(more_clothes).lower() == "no":
            print('Alright')
        else:
            self.put_on_armor(choice=int(more_clothes))

    # def put_off_armor(self, choice):

    def calc_dmg(self):
        """Calculates damage by the player based on strenght, agility and skill. Takes weapon min and max values
        and multiplies them with the damage modifier."""
        if self.active_weapon.weapon_type == 'fist':
            self.active_skill = self.skills['fist']
        modifier = 1 + (self.strength / 100) + (self.agility / 150) + (self.active_skill / 10)
        return int(modifier * random.randint(self.active_weapon.damage[0], self.active_weapon.damage[1]))

    def chance_of_critical_strike(self):
        """Calculates chance for critical damage based on character's self.critical_chance value,
        returns True if chance is within default 5%, players self.critical_chance increases the probability by
        lowering the random range"""
        chance = random.randint(self.critical_chance, 100)
        return True if chance in range(95, 100) else False

    @staticmethod
    def player_hit(target):
        """Gives a choice to a player to hit an enemy."""
        """To fix later. Wanted to code 'a or head' kind of response but face a bug where uses only first if"""
        flag = True
        while flag:
            where_to_hit = input(
                'Where you want to hit your enemy? a) Head, b) Torso, c) Left hand, d) Right hand, f) Legs ')
            if where_to_hit.lower() == "a":
                hit_choice = 'head'
                active_armor = target.head_armor
                flag = False
            elif where_to_hit.lower() == 'b':
                hit_choice = 'torso'
                active_armor = target.torso_armor
                flag = False
            elif where_to_hit.lower() == 'c':
                hit_choice = 'left arm'
                active_armor = target.left_arm_armor
                flag = False
            elif where_to_hit.lower() == 'd':
                hit_choice = 'right arm'
                active_armor = target.right_arm_armor
                flag = False
            elif where_to_hit.lower() == 'f':
                hit_choice = 'legs'
                active_armor = (int(target.legs_armor[0] + (target.feet_armor[0] / 1)), int(
                    target.legs_armor[1] + (target.feet_armor[1] / 7)))
                flag = False
            else:
                print(
                    "You trying to hit an imaginary part of {}'s body, maybe it is not a good idea".format(target.name))
        return hit_choice, active_armor

    @staticmethod
    def npc_hit(target):
        """Uses random to choose where to hit a plyaer."""
        hit_choice = ''
        active_armor = None
        random_where_to_hit = random.randint(1, 5)
        if random_where_to_hit == 1:
            hit_choice = 'head'
            active_armor = target.head_armor
        elif random_where_to_hit == 2:
            hit_choice = 'torso'
            active_armor = target.torso_armor
        elif random_where_to_hit == 3:
            hit_choice = 'left arm'
            active_armor = target.left_arm_armor
        elif random_where_to_hit == 4:
            hit_choice = 'right arm'
            active_armor = target.right_arm_armor
        elif random_where_to_hit == 5:
            hit_choice = 'legs'
            active_armor = int(target.legs_armor[0] + (target.feet_armor[0]) / 7), int(target.legs_armor[1] +
                                                                                       (target.feet_armor[1] / 7))
        return hit_choice, active_armor

    def hit_enemy(self, target):
        """Calculates the damage from a weapon based on chr characteristics"""
        if target.chr_type == 'npc':
            critical = False
            hit_choice, active_armor = self.player_hit(target)
            armor_value = int(random.randint(active_armor[0], active_armor[1]))
            if self.chance_of_critical_strike():
                damage = int(self.calc_dmg() * 1.5)
                critical = True
            else:
                damage = self.calc_dmg() - armor_value
            return (0, hit_choice, critical) if damage < 0 else (damage, hit_choice, critical)
        elif target.chr_type == 'player':
            critical = False
            hit_choice, active_armor = self.npc_hit(target)
            armor_value = int(random.randint(active_armor[0], active_armor[1]))
            if self.chance_of_critical_strike():
                damage = int(self.calc_dmg() * 1.5)
                critical = True
            else:
                damage = self.calc_dmg() - armor_value
            return (0, hit_choice, critical) if damage < 0 else (damage, hit_choice, critical)


class Swordsman(Hero):
    """
    A swordsman or an axeman, inherits from Hero class. Also takes specialization attribute.
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
                 active_weapon=items.fist,
                 spec=None,
                 chr_type='npc'):
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
                         spec,
                         chr_type)
        self.spec = spec
        self.swordsman_bonuses()
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

    def swordsman_bonuses(self):
        self.hp += 30 * self.lvl
        self.sword_skill = 3


class Axeman(Hero):
    """
    A swordsman or an axeman, inherits from Hero class. Also takes specialization attribute.
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
                 spec=None,
                 chr_type='npc'):
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
                         spec,
                         chr_type)
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
