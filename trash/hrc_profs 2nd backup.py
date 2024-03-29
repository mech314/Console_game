import random
from abc import ABC

from console_game.game import armor
from console_game.game import items
from console_game.game import weapon


class Creature(ABC):
    def __init__(self,
                 name,
                 gender,
                 clan,
                 level,
                 exp,
                 chr_points,
                 base_hp,
                 base_luck,
                 base_strength,
                 base_agility,
                 base_movement,
                 base_intelligence,
                 base_critical_chance,
                 bag,
                 _what_is_on,
                 base_sword_skill,
                 base_knife_skill,
                 base_axe_skill,
                 base_bow_skill,
                 base_fist_skill,
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
        self.level = level  # Level
        self.exp = exp  # Experience, will be added after battles etc
        self.chr_points = chr_points  # Amount of points received with the level_UP.
        self.base_hp = base_hp  # Amount of hit-points
        self.base_luck = base_luck  # How lucky the bastard is
        self.base_strength = base_strength  # Strong man?
        self.base_agility = base_agility  # Agile
        self.base_movement = base_movement  # will be helping to calculate how far hero can go or how many action can perform
        self.base_intelligence = base_intelligence  # How smart
        self.base_critical_chance = base_critical_chance  # A chance to make a critical hit, strikes ignoring armor + 10% dmg
        self.bag = bag  # A storage for all the shit that Hero has
        self._what_is_on = _what_is_on  # List that contains all clothes on a hero. Pop them from bag when you put them
        self.base_sword_skill = base_sword_skill
        self.base_knife_skill = base_knife_skill
        self.base_axe_skill = base_axe_skill
        self.base_bow_skill = base_bow_skill
        self.base_fist_skill = base_fist_skill
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
                 level=1,
                 exp=0,
                 chr_points=0,
                 base_hp=100,
                 base_luck=1,
                 base_strength=3,
                 base_agility=3,
                 base_movement=2,
                 base_intelligence=1,
                 base_critical_chance=0,
                 bag=[],
                 _what_is_on=[],
                 base_sword_skill=0,
                 base_knife_skill=0,
                 base_axe_skill=0,
                 base_bow_skill=0,
                 base_fist_skill=0,
                 head=items.naked,
                 torso=items.naked,
                 left_arm=items.naked,
                 right_arm=items.naked,
                 legs=items.naked,
                 feet=items.naked,
                 active_weapon=items.fist,
                 active_skill=0,
                 chr_type='npc',
                 spec=None):

        super().__init__(name,
                         gender,
                         clan,
                         level,
                         exp,
                         chr_points,
                         base_hp,
                         base_luck,
                         base_strength,
                         base_agility,
                         base_movement,
                         base_intelligence,
                         base_critical_chance,
                         bag,
                         _what_is_on,
                         base_sword_skill,
                         base_knife_skill,
                         base_axe_skill,
                         base_bow_skill,
                         base_fist_skill,
                         head,
                         torso,
                         left_arm,
                         right_arm,
                         legs,
                         feet,
                         active_weapon,
                         active_skill,
                         chr_type,
                         spec)
        self.apply_specialization()  # Adds specialization bonuses at the character creation
        """This is definitely redundant but I don't know how to make it better yet. This section will define 
        an effective value for the parameters based on what is on the character. This is here because it is handy if you wanna
        start with the character not naked but with clothes and weapon. Not necessary for sure but works so far."""
        self.hp = self.base_hp + (self.head.hp + self.torso.hp + self.left_arm.hp +
                                  self.right_arm.hp + self.legs.hp + self.feet.hp + self.active_weapon.hp)
        self.luck = (
                self.base_luck + self.head.luck + self.torso.luck + self.left_arm.luck + self.right_arm.luck + self.legs.luck +
                self.feet.luck + self.active_weapon.luck)
        self.strength = (
                self.base_strength + self.head.strength + self.torso.strength + self.left_arm.strength + self.right_arm.strength +
                self.legs.strength + self.feet.strength + self.active_weapon.strength)
        self.agility = (
                self.base_agility + self.head.agility + self.torso.agility + self.left_arm.agility + self.right_arm.agility +
                self.legs.agility + self.feet.agility + self.active_weapon.agility)
        self.movement = (
                self.base_movement + self.head.movement + self.torso.movement + self.left_arm.movement + self.right_arm.movement +
                self.legs.movement + self.feet.movement + self.active_weapon.movement)
        self.intelligence = (
                self.base_intelligence + self.head.intelligence + self.torso.intelligence + self.left_arm.intelligence +
                self.right_arm.intelligence + self.legs.intelligence + self.feet.intelligence +
                self.active_weapon.intelligence)
        self.critical_chance = (self.base_critical_chance + self.head.critical_chance +
                                self.torso.critical_chance + self.left_arm.critical_chance + self.right_arm.critical_chance
                                + self.legs.critical_chance + self.feet.critical_chance + self.active_weapon.critical_chance)

        self.max_hp = self.hp
        self.sword_skill = base_sword_skill
        self.knife_skill = base_knife_skill
        self.axe_skill = base_axe_skill
        self.bow_skill = base_bow_skill
        self.fist_skill = base_fist_skill
        self.active_skill = self.skills[self.active_weapon.weapon_type.lower()]

    def base_specs(self):  # Makes a dict with the UNMODIFIED VALUES
        base_specs_dict = {'hp': self.base_hp, 'strength': self.base_strength, 'agility': self.base_agility,
                           'luck': self.base_luck,
                           'movement': self.base_movement, 'intelligence': self.base_intelligence,
                           'critical_chance': self.base_critical_chance,
                           'Sword skill': self.base_sword_skill, 'Axe skill': self.base_axe_skill,
                           'Bow skill': self.base_bow_skill,
                           'Fist skill': self.base_fist_skill, 'Knife skill': self.base_knife_skill}
        return base_specs_dict

    def effective_specs(self):  # Makes a dict with CURRENT VALUES
        effective_specs_dict = {'hp': self.hp, 'strength': self.strength, 'agility': self.agility, 'luck': self.luck,
                                'movement': self.movement, 'intelligence': self.intelligence,
                                'critical_chance': self.critical_chance,
                                'Sword skill': self.sword_skill, 'Axe skill': self.axe_skill,
                                'Bow skill': self.bow_skill,
                                'Fist skill': self.fist_skill, 'Knife skill': self.knife_skill}
        return effective_specs_dict

    def apply_specialization(self):
        if self.spec.lower() == 'swordsman':
            self.base_sword_skill += 3
            self.base_hp += 30
        elif self.spec.lower() == 'axeman':
            self.base_axe_skill += 3
            self.base_critical_chance += 5

    # def hp_difference(self):

    # def set_current_specs(self):
    #     """This is rather redundant but didn't find a better solution yet. It will just set current specs by adding all bonuses"""
    #     if self.spec.lower() == 'swordsman':
    #         bonus = 30 * self.level
    #     else:
    #         bonus = 0
    #
    #     self.max_hp = self.base_hp + (self.head.hp + self.torso.hp + self.left_arm.hp +
    #                                   self.right_arm.hp + self.legs.hp + self.feet.hp + self.active_weapon.hp)
    #
    #     self.hp = self.base_hp + (self.head.hp + self.torso.hp + self.left_arm.hp +
    #                               self.right_arm.hp + self.legs.hp + self.feet.hp + self.active_weapon.hp)
    #
    #     if self.max_hp == self.hp:
    #         self.hp = self.base_hp + (self.head.hp + self.torso.hp + self.left_arm.hp +
    #                                   self.right_arm.hp + self.legs.hp + self.feet.hp + self.active_weapon.hp)
    #         print(self.hp)
    #     elif self.max_hp > self.hp:
    #         hp_difference = self.max_hp - self.hp
    #         self.hp = self.base_hp + (self.head.hp + self.torso.hp + self.left_arm.hp +
    #                                   self.right_arm.hp + self.legs.hp + self.feet.hp + self.active_weapon.hp) - hp_difference
    #
    #     self.luck = (
    #             self.base_luck + self.head.luck + self.torso.luck + self.left_arm.luck + self.right_arm.luck + self.legs.luck +
    #             self.feet.luck + self.active_weapon.luck)
    #     self.strength = (
    #             self.base_strength + self.head.strength + self.torso.strength + self.left_arm.strength + self.right_arm.strength +
    #             self.legs.strength + self.feet.strength + self.active_weapon.strength)
    #     self.agility = (
    #             self.base_agility + self.head.agility + self.torso.agility + self.left_arm.agility + self.right_arm.agility +
    #             self.legs.agility + self.feet.agility + self.active_weapon.agility)
    #     self.movement = (
    #             self.base_movement + self.head.movement + self.torso.movement + self.left_arm.movement + self.right_arm.movement +
    #             self.legs.movement + self.feet.movement + self.active_weapon.movement)
    #     self.intelligence = (
    #             self.base_intelligence + self.head.intelligence + self.torso.intelligence + self.left_arm.intelligence +
    #             self.right_arm.intelligence + self.legs.intelligence + self.feet.intelligence +
    #             self.active_weapon.intelligence)
    #     if self.spec.lower() == 'axeman':  # Apply axeman critical change bonus
    #         self.critical_chance = (10 + self.base_critical_chance + self.head.critical_chance +
    #                                 self.torso.critical_chance + self.left_arm.critical_chance + self.right_arm.critical_chance
    #                                 + self.legs.critical_chance + self.feet.critical_chance + self.active_weapon.critical_chance)
    #     else:
    #         self.critical_chance = (self.base_critical_chance + self.head.critical_chance +
    #                                 self.torso.critical_chance + self.left_arm.critical_chance + self.right_arm.critical_chance
    #                                 + self.legs.critical_chance + self.feet.critical_chance + self.active_weapon.critical_chance)
    #     self.effective_specs()

    @property
    def skills(self):
        """Returns all skills as a dict"""
        return {'sword': self.base_sword_skill, 'knife': self.base_knife_skill, 'axe': self.base_axe_skill,
                'bow': self.base_bow_skill, 'fist': self.base_fist_skill}

    @property
    def current_characteristics(self):
        """Return all EFFECTIVE Hero's characteristics as a dict"""
        return {'name': self.name, 'chr_type': self.chr_type, 'specialization': self.spec, 'level': self.level,
                'hp': self.hp, 'strength': self.strength, 'agility': self.agility, 'luck': self.luck,
                'movement': self.movement, 'intelligence': self.intelligence, 'critical_chance': self.critical_chance,
                'active_skill': self.active_skill, 'Axe skill': self.axe_skill, 'Sword skill': self.sword_skill,
                'Head armor': self.head_armor, 'Body armor': self.torso_armor, 'Left arm armor': self.left_arm_armor,
                'Right arm armor': self.right_arm_armor, 'Legs armor': self.legs_armor, 'Feet armor': self.feet_armor,
                'Weapon damage': self.whats_on_dict['Active weapon'].damage}

    @property
    def whats_on_dict(self):
        """Return all Hero's clothes as a dict"""
        return {'Head': self.head, 'Torso': self.torso, 'Left arm': self.left_arm, 'Right arm': self.right_arm,
                "Legs": self.legs, 'Feet': self.feet, 'Active weapon': self.active_weapon}

    def print_whats_on(self):
        """Prints clothes and weapon on the character """
        print('----------------------------------------')
        for count, item in enumerate(self._what_is_on):
            """Will print all armor from the armor list in items module"""
            if item.item_type == 'weapon':
                print('Item # ', count, '\nName', ':', item.name.capitalize(),
                      '\nCondition', item.condition,
                      '\nHp: ', item.hp,
                      '\nDamage: ', item.damage,
                      '\nDurability:', item.durability,
                      '\nLuck: ', item.luck,
                      '\nStrength: ', item.strength,
                      '\nAgility: ', item.agility,
                      '\nMovement: ', item.movement,
                      '\nIntelligence: ', item.intelligence,
                      '\nCritical chance: ', item.critical_chance,
                      '\nLevel: ', item.level)
            elif item.item_type == 'clothes':
                print('Item # ', count, '\nName', ':', item.name.capitalize(),
                      '\nCondition', item.condition,
                      '\nHp: ', item.hp,
                      '\nArmor: ', item.armor,
                      '\nDurability:', item.durability,
                      '\nLuck: ', item.luck,
                      '\nStrength: ', item.strength,
                      '\nAgility: ', item.agility,
                      '\nMovement: ', item.movement,
                      '\nIntelligence: ', item.intelligence,
                      '\nCritical chance: ', item.critical_chance,
                      '\nLevel: ', item.level)
            print('----------------------------------------')

        on_chr = {key: value for (key, value) in self.whats_on_dict.items() if value}
        return {k.capitalize(): v for k, v in on_chr.items()}

    def print_chr(self):
        """Prints name and all character characteristics"""
        print('---------------------------------------')
        print("{}'s characteristics are: ".format(self.name))
        for k, v in self.current_characteristics.items():
            print(k.capitalize(), ':', v)
        print('---------------------------------------')

    def level_up(self):
        """
        A property that will check for the amount of experience. If it exceeds certain amount will increase Hero's level
        """
        if self.exp >= self.level * 100:
            self.level += 1
            self.chr_points += 5
            if self.spec.lower() == 'swordsman':
                self.hp += 30
            if self.spec.lower() == 'axeman':
                self.base_critical_chance += 5
            print("Congratulations, you have reached {} level, you have {} free "
                  "points to make yourself better".format(self.level, self.chr_points))
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
                self.base_strength += 1
                self.chr_points -= 1
                print("Your Base Strength is {}".format(self.base_strength))
            elif choice.lower() == 'b' and 'agility':
                self.base_agility += 1
                self.chr_points -= 1
                print("Your Base Agility is {}".format(self.base_agility))
            elif choice.lower() == 'c' and 'luck':
                self.base_luck += 1
                self.chr_points -= 1
                print("Your Base Luck is {}".format(self.base_luck))
            elif choice.lower() == 'd' and 'movement':
                self.base_movement += 1
                self.chr_points -= 1
                print("Your Base Movement is {}".format(self.base_movement))
            elif choice.lower() == 'f' and 'intelligence':
                self.base_intelligence += 1
                self.chr_points -= 1
                print("Your Base Intelligence is {}".format(self.base_intelligence))
        print("Your character's characteristics are:")
        self.print_chr()

    def add_item_to_thebag(self, item):
        """Adds item to the bag, if the list was passed - entire list will be picked up"""
        if isinstance(item, list):
            for i in item:
                self.bag.append(i)
        else:
            self.bag.append(item)

    @property
    def bag_content(self):
        return self.bag

    def printbag_cnt(self):
        print("You have following items in the bag:")
        for count, item in enumerate(self.bag):
            print('----------------------------------------')
            """Will print all armor from the armor list in items module"""
            if item.item_type == 'weapon':
                print('Item # ', count, '\nName', ':', item.name.capitalize(),
                      '\nCondition', item.condition,
                      '\nHp: ', item.hp,
                      '\nDamage: ', item.damage,
                      '\nDurability:', item.durability,
                      '\nLuck: ', item.luck,
                      '\nStrength: ', item.strength,
                      '\nAgility: ', item.agility,
                      '\nMovement: ', item.movement,
                      '\nIntelligence: ', item.intelligence,
                      '\nCritical chance: ', item.critical_chance,
                      '\nLevel: ', item.level)
            elif item.item_type == 'clothes':
                print('Item # ', count, '\nName', ':', item.name.capitalize(),
                      '\nCondition', item.condition,
                      '\nHp: ', item.hp,
                      '\nArmor: ', item.armor,
                      '\nDurability:', item.durability,
                      '\nLuck: ', item.luck,
                      '\nStrength: ', item.strength,
                      '\nAgility: ', item.agility,
                      '\nMovement: ', item.movement,
                      '\nIntelligence: ', item.intelligence,
                      '\nCritical chance: ', item.critical_chance,
                      '\nLevel: ', item.level)
        print('----------------------------------------')

    # def choose_weapon(self, choice):
    #     """Selecting the weapon from the bag and adds-up all the characteristic to self.whatever_chr_is"""
    #     item = self.bag_content[choice]
    #     if isinstance(item, weapon.Weapon):
    #         self.active_weapon = self.bag_content[choice]
    #         self.active_skill = self.skills[self.active_weapon.weapon_type]
    #         self.luck += self.active_weapon.luck
    #         self.hp += self.active_weapon.hp
    #         self.strength += self.active_weapon.strength
    #         self.agility += self.active_weapon.agility
    #         self.movement += self.active_weapon.movement
    #         self.intelligence += self.active_weapon.intelligence
    #         self.critical_chance += self.active_weapon.critical_chance
    #         print(f'You have {item.name.lower()} in your hand')
    #         return self.active_skill
    #     else:
    #         print(f'You are trying to fight with {item.name.lower()}, are you too smart?')

    def put_on_items(self, choice=None):
        """Puts a piece of armor on you"""
        if choice:
            print(choice)
        elif choice is None:
            self.printbag_cnt()
            choice = input('PUTTING ON ITEMS What do you want to put on:')
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
        elif isinstance(item, weapon.Weapon):
            print(f'You have {item.name.lower()} in your hands')
            self.active_weapon = self.bag_content[int(choice)]
            self.active_skill = self.skills[self.active_weapon.weapon_type]
        self._what_is_on.append(self.bag.pop(int(choice)))
        self.base_hp += item.hp  # Now adds up all characteristics of a cloth to character's chr.
        self.luck += item.luck
        self.strength += item.strength
        self.agility += item.agility
        self.movement += item.movement
        self.intelligence += item.intelligence
        self.critical_chance += item.critical_chance
        if len(self.bag_content) > 0:
            self.printbag_cnt()
            more_items = input('Do you want to put something else? ')
            if str(more_items).lower() == "no":
                print('Alright')
            else:
                self.put_on_items(choice=int(more_items))
        return item

    def put_off_items(self, choice=None):
        if choice:
            print(choice)
        if choice is None:
            print('TAKING OFF THE ITEMS This is what is on you:')
            self.print_whats_on()
            choice = input('What do you want to take off:')
            if choice == "no":
                return None
        item = self._what_is_on[int(choice)]
        if isinstance(item, armor.Armor):
            if item.armor_type == 'jacket':  # Put jacket on body, gives armor for hands and torso
                print(f'You took off {item.name} from your body')
                naked = items.naked
                self.torso = naked
                self.torso_armor = naked.armor
                self.left_arm_armor = naked.armor
                self.right_arm_armor = naked.armor
            elif item.armor_type == 'vest':  # Put vest, naked arms but can put armlets now
                print(f'You took off {item.name} from your body')
                naked = items.naked
                self.torso = naked
                self.torso_armor = naked.armor
            elif item.armor_type == 'armlet':
                flag = True
                while flag:
                    if self.torso.armor_type != 'jacket':  # Can put armlets only with vest or naked
                        hand = input('Take off from left or right hand? Or say no if you changed your mind.')
                        if hand.lower() == 'left':
                            print(f'You took off {item.name} from your left hand')
                            naked = items.naked
                            self.left_arm = naked
                            self.left_arm_armor = naked.armor
                            flag = False
                        elif hand.lower() == 'right':
                            print(f'You took off {item.name} from your right hand')
                            naked = items.naked
                            self.left_arm = naked
                            self.left_arm_armor = naked.armor
                            flag = False
                        elif hand.lower() == 'no':
                            return None
                        else:
                            print(f'Choose the hand on which you wanna put {item.name}')
                    else:
                        print(f'You cannot put armlets on because you are wearing {self.torso.name}')
            elif item.armor_type == 'trousers':  # Same story with pants
                print(f'You took {item.name} off your legs')
                naked = items.naked
                self.legs = naked
                self.legs_armor = naked.armor
            elif item.armor_type == 'boots':  # Same story with boots
                print(f'You took {item.name} off your feet')
                naked = items.naked
                self.feet = naked
                self.feet_armor = naked.armor
            elif item.armor_type == 'helmet':  # Same story with helmet
                print(f'You took {item.name} off your head')
                naked = items.naked
                self.head = naked
                self.head_armor = naked.armor
        elif isinstance(item, weapon.Weapon):
            print(f'You put {item.name.lower()} away from your hands')
            self.active_weapon = items.fist
            self.active_skill = self.skills[self.active_weapon.weapon_type]
        self.bag.append(self._what_is_on.pop(int(choice)))
        self.base_hp -= item.hp  # Now adds up all characteristics of a cloth to character's chr.
        self.luck -= item.luck
        self.strength -= item.strength
        self.agility -= item.agility
        self.movement -= item.movement
        self.intelligence -= item.intelligence
        self.critical_chance -= item.critical_chance
        if len(self._what_is_on) > 0:
            naked_party = input('Do you want to take something else off? ')
            if str(naked_party).lower() == "no":
                print('Alright')
            else:
                self.put_off_items(choice=int(naked_party))
        return item

    def calc_dmg(self):
        """Calculates damage by the player based on strenght, agility and skill. Takes weapon min and max values
        and multiplies them with the damage modifier."""
        if self.active_weapon.weapon_type == 'fist':
            self.active_skill = self.skills['fist']
        modifier = 1 + (self.strength / 100) + (self.agility / 150) + (self.active_skill / 10)
        return int(modifier * (random.choice(self.active_weapon.damage)))

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
                active_armor = ((int(target.legs_armor[0] + target.feet_armor[0])), int(
                    (target.legs_armor[1] + target.feet_armor[1])))
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
            active_armor = int((target.legs_armor[0] + target.feet_armor[0])), int((target.legs_armor[1] +
                                                                                    target.feet_armor[1]))
        return hit_choice, active_armor

    def hit_enemy(self, target):
        """Calculates the damage from a weapon based on chr characteristics"""
        if target.chr_type == 'npc':
            critical = False
            hit_choice, active_armor = self.player_hit(target)
            armor_value = int(random.choice(active_armor))
            if self.chance_of_critical_strike():
                damage = int(self.calc_dmg() * 1.5)
                critical = True
            else:
                damage = self.calc_dmg() - armor_value
            print(active_armor)
            return (0, hit_choice, critical) if damage < 0 else (damage, hit_choice, critical)
        elif target.chr_type == 'player':
            critical = False
            hit_choice, active_armor = self.npc_hit(target)
            armor_value = int(random.choice(active_armor))
            if self.chance_of_critical_strike():
                damage = int(self.calc_dmg() * 1.5)
                critical = True
            else:
                damage = self.calc_dmg() - armor_value
            print(active_armor)
            return (0, hit_choice, critical) if damage < 0 else (damage, hit_choice, critical)

    # def npc_weapon(self):
    #     """Adds weapon bonuses to NPC"""
    #     self.active_skill = self.skills[self.active_weapon.weapon_type.lower()]
    #     self.luck += self.active_weapon.luck
    #     self.hp += self.active_weapon.hp
    #     self.strength += self.active_weapon.strength
    #     self.agility += self.active_weapon.agility
    #     self.movement += self.active_weapon.movement
    #     self.intelligence += self.active_weapon.intelligence
    #     self.critical_chance += self.active_weapon.critical_chance
    #
    # def npc_clothes(self):
    #     """Adds clothes bonuses to NPC"""
    #     self.hp += (self.head.hp + self.torso.hp + self.left_arm.hp + self.right_arm.hp + self.legs.hp + self.feet.hp)
    #     self.luck += (self.head.luck + self.torso.luck + self.left_arm.luck + self.right_arm.luck + self.legs.luck +
    #                   self.feet.luck)
    #     self.strength += (self.head.strength + self.torso.strength + self.left_arm.strength + self.right_arm.strength +
    #                       self.legs.strength + self.feet.strength)
    #     self.agility += (self.head.agility + self.torso.agility + self.left_arm.agility + self.right_arm.agility +
    #                      self.legs.agility + self.feet.agility)
    #     self.movement += (self.head.movement + self.torso.movement + self.left_arm.movement + self.right_arm.movement +
    #                       self.legs.movement + self.feet.movement)
    #     self.intelligence += (self.head.intelligence + self.torso.intelligence + self.left_arm.intelligence +
    #                           self.right_arm.intelligence + self.legs.intelligence + self.feet.intelligence)
    #     self.critical_chance += (self.head.critical_chance + self.torso.critical_chance + self.left_arm.critical_chance
    #                              + self.right_arm.critical_chance + self.legs.critical_chance + self.feet.critical_chance)

# class Thief(Hero):
#     """
#     A knifesman, inherits from Hero, takes specialization. Sneaky - high agility, smart - high intelect
#     """
#
#     def __init__(self, name, gender, clan, spec):
#         super().__init__(name, gender, clan)
#         self.spec = spec
#
#         if self.spec == "sneaky":  # if sneaky is agile
#             self.agility = 5
#         else:  # if smart is smart
#             self.intelligence = 5
