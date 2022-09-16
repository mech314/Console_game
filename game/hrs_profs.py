import random
from abc import ABC

from game import armor
from game import items
from game import weapon


class Creature(ABC):
    def __init__(self,
                 name,
                 gender,
                 clan,
                 level,
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
                 _what_is_on,
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
        self.level = level  # Level
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
        self._what_is_on = _what_is_on  # List that contains all clothes on a hero. Pop them from bag when you put them
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
                 level=1,
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
                 _what_is_on=[],
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
                 active_skill=0,
                 chr_type='npc',
                 spec=None):

        super().__init__(name,
                         gender,
                         clan,
                         level,
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
                         _what_is_on,
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
                         spec)
        self.apply_specialization()  # Adds specialization bonuses at the character creation
        """This is definitely redundant but I don't know how to make it better yet. This section will define 
        an effective value for the parameters based on what is on the character. This is here because it is handy if you wanna
        start with the character not naked but with clothes and weapon. Not necessary for sure but works so far."""
        self.hp += (self.head.hp + self.torso.hp + self.left_arm.hp +
                    self.right_arm.hp + self.legs.hp + self.feet.hp + self.active_weapon.hp)
        self.luck += (
                self.head.luck + self.torso.luck + self.left_arm.luck + self.right_arm.luck + self.legs.luck +
                self.feet.luck + self.active_weapon.luck)
        self.strength += (
                self.head.strength + self.torso.strength + self.left_arm.strength + self.right_arm.strength +
                self.legs.strength + self.feet.strength + self.active_weapon.strength)
        self.agility += (
                self.head.agility + self.torso.agility + self.left_arm.agility + self.right_arm.agility +
                self.legs.agility + self.feet.agility + self.active_weapon.agility)
        self.movement += (
                self.head.movement + self.torso.movement + self.left_arm.movement + self.right_arm.movement +
                self.legs.movement + self.feet.movement + self.active_weapon.movement)
        self.intelligence += (
                self.head.intelligence + self.torso.intelligence + self.left_arm.intelligence +
                self.right_arm.intelligence + self.legs.intelligence + self.feet.intelligence +
                self.active_weapon.intelligence)
        self.critical_chance += (self.head.critical_chance +
                                 self.torso.critical_chance + self.left_arm.critical_chance + self.right_arm.critical_chance
                                 + self.legs.critical_chance + self.feet.critical_chance + self.active_weapon.critical_chance)
        self.reference_hp = hp
        self.max_hp = self.hp
        self.sword_skill = sword_skill
        self.knife_skill = knife_skill
        self.axe_skill = axe_skill
        self.bow_skill = bow_skill
        self.fist_skill = fist_skill
        self.active_skill = self.skills[self.active_weapon.weapon_type.lower()]
        self.bag = bag

    def apply_specialization(self):
        if self.spec.lower() == 'swordsman':
            self.sword_skill += 3
            self.hp += 30
        elif self.spec.lower() == 'axeman':
            self.axe_skill += 3
            self.critical_chance += 5

    def current_max_hp(self):
        if self.spec.lower() == 'swordsman':
            self.max_hp = self.reference_hp + (30 * self.level) + (self.head.hp + self.torso.hp + self.left_arm.hp +
                                                                   self.right_arm.hp + self.legs.hp + self.feet.hp + self.active_weapon.hp)
        else:
            self.max_hp = self.reference_hp + (self.head.hp + self.torso.hp + self.left_arm.hp +
                                               self.right_arm.hp + self.legs.hp + self.feet.hp + self.active_weapon.hp)

    @property
    def skills(self):
        """Returns all skills as a dict"""
        return {'sword': self.sword_skill, 'knife': self.knife_skill, 'axe': self.axe_skill,
                'bow': self.bow_skill, 'fist': self.fist_skill}

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
                self.current_max_hp
            if self.spec.lower() == 'axeman':
                self.critical_chance += 5
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
                self.strength += 1
                self.chr_points -= 1
                print("Your Base Strength is {}".format(self.strength))
            elif choice.lower() == 'b' and 'agility':
                self.agility += 1
                self.chr_points -= 1
                print("Your Base Agility is {}".format(self.agility))
            elif choice.lower() == 'c' and 'luck':
                self.luck += 1
                self.chr_points -= 1
                print("Your Base Luck is {}".format(self.luck))
            elif choice.lower() == 'd' and 'movement':
                self.movement += 1
                self.chr_points -= 1
                print("Your Base Movement is {}".format(self.movement))
            elif choice.lower() == 'f' and 'intelligence':
                self.intelligence += 1
                self.chr_points -= 1
                print("Your Base Intelligence is {}".format(self.intelligence))
        print("Your character's characteristics are:")
        self.print_chr()

    def add_item_to_thebag(self, loot, specific_item=None):
        if specific_item:
            self.bag.append(specific_item)
            loot.remove(specific_item)
        else:
            self.bag += loot
            loot = []

    def chr_belongings(self):
        """This method prints what's on the character and what is in the bag ignoring "naked" or "fist" objects"""
        print(f'{self.name} bag contents:')
        for item in self.bag:
            print(item.name)
        print(f'{self.name} has on him:')
        for key, value in self.whats_on_dict.items():
            if value.item_type.lower() == 'clothes' and value.armor_type != 'naked':
                print(value.name)
            elif value.item_type.lower() == 'weapon' and value.weapon_type != 'fist':
                print(value.name)

    def loot_drop(self):
        """Function that will make a drop of the loot. Will take all the items from the bag and on the character
        with certain chance it will make only a part of the items to actually drop. Dropped items will be an
        instance of lootbox class."""

        if self.chr_belongings:      # If there is anything to drop
            """Calculating the chance of dropping stuff."""
            chance = random.randint(0, 100)
            n = 0
            if chance < 95:
                if chance < 10:
                    n = len(self.chr_belongings)
                elif chance < 30:
                    n = int(len(self.chr_belongings) / 1.2)
                else:
                    n = 1
                loot_name = str(self.name + ' loot')
                loot_box = random.sample(self.chr_belongings, n)     # Creating random amount loot
                loot = items.LootBoxes(name=loot_name, contents=loot_box)       # Creating a class object of loot
                items.location_loot.append(loot)        # Appending it to the location's items
            else:
                print(f"Nothing has fallen from {self.name}")

    @property
    def bag_content(self):
        return self.bag

    def printbag_cnt(self):
        print("You have following items in the bag:")
        for count, item in enumerate(self.bag):
            print('----------------------------------------')
            """Will print all armor from the armor list in items module"""
            if item.item_type == 'weapon':
                print('Item # ', count, 'Name', ':', item.name.capitalize(),
                      'Condition', item.condition,
                      'Hp: ', item.hp,
                      'Damage: ', item.damage,
                      'Durability:', item.durability,
                      'Luck: ', item.luck,
                      'Strength: ', item.strength,
                      'Agility: ', item.agility,
                      'Movement: ', item.movement,
                      'Intelligence: ', item.intelligence,
                      'Critical chance: ', item.critical_chance,
                      'Level: ', item.level)
            elif item.item_type == 'clothes':
                print('Item # ', count, 'Name', ':', item.name.capitalize(),
                      'Condition', item.condition,
                      'Hp: ', item.hp,
                      'Armor: ', item.armor,
                      'Durability:', item.durability,
                      'Luck: ', item.luck,
                      'Strength: ', item.strength,
                      'Agility: ', item.agility,
                      'Movement: ', item.movement,
                      'Intelligence: ', item.intelligence,
                      'Critical chance: ', item.critical_chance,
                      'Level: ', item.level)
            elif item.item_type == 'potion':
                print('Item # ', count, 'Name', ':', item.name.capitalize(),
                      'Hp: ', item.hp,
                      'Level: ', item.level)
        print('----------------------------------------')

    def health_potion(self):
        potion_counter = 0
        for item in self.bag:  # Yes this is stupid, probably need to learn how to find object in the list using __eq__
            if item.item_type == 'potion':
                potion_counter += 1
        if potion_counter >= 1:
            self.print_potionbag()
            choice = input('Which potion do you want to take? ')
            potion = self.bag.pop(int(choice))
            if self.hp + potion.hp >= self.max_hp:
                self.hp = self.max_hp
                print("You health has been restored to the max level")
            else:
                self.hp += potion.hp
                print(f'You health restored to {self.hp}')
        else:
            print("You have checked your bag and it seems that you don't have any potions buddy...")

    def print_potionbag(self):
        """Will print only the potions in the bag"""
        print("You have following potions in the bag:")
        for count, item in enumerate(self.bag):
            if item.item_type == 'potion':
                print('----------------------------------------')
                print('Item # ', count, 'Name', ':', item.name.capitalize(),
                      'Hp: ', item.hp,
                      'Level: ', item.level)

    def put_on_items(self, choice=None):
        """Puts a piece of armor on you"""
        if choice is None:
            print('PUTTING ON THE ITEMS This is what you have in the bag:')
            self.printbag_cnt()
            input_choice = input('What do you want to put on:')
            if input_choice.isnumeric() and len(self.bag)-1 >= int(input_choice):
                try:
                    choice = int(input_choice)
                except ValueError:
                    print("Input error")
                    self.put_on_items()
            elif str(input_choice) == "no":
                print("You decided not to put on anything")
                return None
            elif input_choice == "q":
                print("Quiting")
                exit()
            else:
                print("Input error")
                self.put_on_items()
        item = self.bag_content[choice]
        if isinstance(item, armor.Armor):
            if item.armor_type == 'jacket':  # Put jacket on body, gives armor for hands and torso
                if self.torso == items.naked:
                    print(f'You put {item.name} on your body')
                    self.torso = self.bag_content[int(choice)]
                    self.left_arm = self.bag_content[int(choice)]
                    self.right_arm = self.bag_content[int(choice)]
                    self.torso_armor = item.armor
                    self.left_arm_armor = item.armor
                    self.right_arm_armor = item.armor
                else:
                    reply_flag = True
                    while reply_flag:
                        user_input = input(f'You have {self.torso.name} on you, do you want to change it? ')
                        if user_input.lower() == 'yes':
                            reply_flag = False
                            old_item = self.torso
                            self.bag.append(old_item)
                            self._what_is_on.remove(old_item)
                            self.torso = self.bag_content[int(choice)]
                            self.left_arm = self.bag_content[int(choice)]
                            self.right_arm = self.bag_content[int(choice)]
                            self.torso_armor = item.armor
                            self.left_arm_armor = item.armor
                            self.right_arm_armor = item.armor
                            print(f'You have changed {old_item.name} for {self.torso.name}')
                        elif user_input.lower() == 'no':
                            reply_flag = False
                            if len(self.bag_content) > 0:
                                more_items_flag = True
                                while more_items_flag:
                                    self.printbag_cnt()
                                    more_items = input('Do you want to put something else? ')
                                    if more_items.isnumeric() and len(self.bag) - 1 >= int(more_items):
                                        more_items_flag = False
                                        self.put_on_items(int(more_items))
                                    elif str(more_items).lower() == "no":
                                        more_items_flag = False
                                        print('Alright')
                                        return None
                                    else:
                                        print('Wrong input')
                            else:
                                print("You have nothing in your bag")
                        else:
                            print("Wrong input")
            elif item.armor_type == 'vest':  # Put vest, naked arms but can put armlets now
                if self.torso == items.naked:
                    print(f'You put {item.name} on your body, you can put armlets as well')
                    self.torso = self.bag_content[int(choice)]
                    self.torso_armor = item.armor
                else:
                    reply_flag = True
                    while reply_flag:
                        user_input = input(f'You have {self.torso.name} on you, do you want to change it? ')
                        if user_input.lower() == 'yes':
                            reply_flag = False
                            old_item = self.torso
                            self.bag.append(old_item)
                            self._what_is_on.remove(old_item)
                            self.torso = self.bag_content[int(choice)]
                            self.torso_armor = item.armor
                            print(f'You have changed {old_item.name} for {self.torso.name}')
                        elif user_input.lower() == 'no':
                            reply_flag = False
                            if len(self.bag_content) > 0:
                                more_items_flag = True
                                while more_items_flag:
                                    self.printbag_cnt()
                                    more_items = input('Do you want to put something else? ')
                                    if more_items.isnumeric() and len(self.bag) - 1 >= int(more_items):
                                        more_items_flag = False
                                        self.put_on_items(int(more_items))
                                    elif str(more_items).lower() == "no":
                                        more_items_flag = False
                                        print('Alright')
                                        return None
                                    else:
                                        print('Wrong input')
                            else:
                                print("You have nothing in your bag")
                        else:
                            print("Wrong input")
            elif item.armor_type == 'armlet':
                armlet_flag = True
                while armlet_flag:
                    if self.torso.armor_type != 'jacket':  # Can put armlets only with vest or naked
                        hand = input('Put on left or right hand?')
                        if hand.lower() == 'left':
                            if self.left_arm == items.naked:
                                print(f'You put {item.name} on your left hand')
                                self.left_arm = self.bag_content[int(choice)]
                                self.left_arm_armor = item.armor
                                armlet_flag = False
                            else:
                                reply_flag = True
                                while reply_flag:
                                    user_input = input(
                                        f'You have {self.left_arm.name} on you, do you want to change it? ')
                                    if user_input.lower() == 'yes':
                                        reply_flag = False
                                        old_item = self.left_arm
                                        self.bag.append(old_item)
                                        self._what_is_on.remove(old_item)
                                        self.left_arm = self.bag_content[int(choice)]
                                        self.left_arm_armor = item.armor
                                        print(f'You have changed {old_item.name} for {self.left_arm.name}')
                                        armlet_flag = False
                                    elif user_input.lower() == 'no':
                                        reply_flag = False
                                        if len(self.bag_content) > 0:
                                            more_items_flag = True
                                            while more_items_flag:
                                                self.printbag_cnt()
                                                more_items = input('Do you want to put something else? ')
                                                if more_items.isnumeric() and len(self.bag) - 1 >= int(more_items):
                                                    more_items_flag = False
                                                    self.put_on_items(int(more_items))
                                                elif str(more_items).lower() == "no":
                                                    more_items_flag = False
                                                    print('Alright')
                                                    return None
                                                else:
                                                    print('Wrong input')
                                        else:
                                            print("You have nothing in your bag")
                                    else:
                                        print("Wrong input")
                        elif hand.lower() == 'right':
                            if self.right_arm == items.naked:
                                print(f'You put {item.name} on your right hand')
                                self.right_arm = self.bag_content[int(choice)]
                                self.right_arm_armor = item.armor
                                armlet_flag = False
                            else:
                                reply_flag = True
                                while reply_flag:
                                    user_input = input(
                                        f'You have {self.right_arm.name} on you, do you want to change it? ')
                                    if user_input.lower() == 'yes':
                                        reply_flag = False
                                        old_item = self.right_arm
                                        self.bag.append(old_item)
                                        self._what_is_on.remove(old_item)
                                        self.right_arm = self.bag_content[int(choice)]
                                        self.right_arm_armor = item.armor
                                        print(f'You have changed {old_item.name} for {self.right_arm.name}')
                                        armlet_flag = False
                                    elif user_input.lower() == 'no':
                                        reply_flag = False
                                        if len(self.bag_content) > 0:
                                            more_items_flag = True
                                            while more_items_flag:
                                                self.printbag_cnt()
                                                more_items = input('Do you want to put something else? ')
                                                if more_items.isnumeric() and len(self.bag) - 1 >= int(more_items):
                                                    more_items_flag = False
                                                    self.put_on_items(int(more_items))
                                                elif str(more_items).lower() == "no":
                                                    more_items_flag = False
                                                    print('Alright')
                                                    return None
                                                else:
                                                    print('Wrong input')
                                        else:
                                            print("You have nothing in your bag")
                                    else:
                                        print("Wrong input")
                        else:
                            print(f'Choose the hand on which you wanna put {item.name}')
                    else:
                        print(f'You cannot put armlets on because you are wearing {self.torso.name}')
            elif item.armor_type == 'trousers':  # Same story with pants
                if self.legs == items.naked:
                    print(f'You put {item.name} on legs')
                    self.legs = self.bag_content[int(choice)]
                    self.legs_armor = item.armor
                else:
                    reply_flag = True
                    while reply_flag:
                        user_input = input(f'You have {self.legs.name} on you, do you want to change it? ')
                        if user_input.lower() == 'yes':
                            reply_flag = False
                            old_item = self.legs
                            self.bag.append(old_item)
                            self._what_is_on.remove(old_item)
                            self.legs = self.bag_content[int(choice)]
                            self.legs_armor = item.armor
                            print(f'You have changed {old_item.name} for {self.legs.name}')
                        elif user_input.lower() == 'no':
                            reply_flag = False
                            if len(self.bag_content) > 0:
                                more_items_flag = True
                                while more_items_flag:
                                    self.printbag_cnt()
                                    more_items = input('Do you want to put something else? ')
                                    if more_items.isnumeric() and len(self.bag) - 1 >= int(more_items):
                                        more_items_flag = False
                                        self.put_on_items(int(more_items))
                                    elif str(more_items).lower() == "no":
                                        more_items_flag = False
                                        print('Alright')
                                        return None
                                    else:
                                        print('Wrong input')
                            else:
                                print("You have nothing in your bag")
                        else:
                            print("Wrong input")
            elif item.armor_type == 'boots':  # Same story with boots
                if self.feet == items.naked:
                    print(f'You put {item.name} on feet')
                    self.feet = self.bag_content[int(choice)]
                    self.feet_armor = item.armor
                else:
                    reply_flag = True
                    while reply_flag:
                        user_input = input(f'You have {self.feet.name} on you, do you want to change it? ')
                        if user_input.lower() == 'yes':
                            reply_flag = False
                            old_item = self.feet
                            self.bag.append(old_item)
                            self._what_is_on.remove(old_item)
                            self.feet = self.bag_content[int(choice)]
                            self.feet_armor = item.armor
                            print(f'You have changed {old_item.name} for {self.feet.name}')
                        elif user_input.lower() == 'no':
                            reply_flag = False
                            if len(self.bag_content) > 0:
                                more_items_flag = True
                                while more_items_flag:
                                    self.printbag_cnt()
                                    more_items = input('Do you want to put something else? ')
                                    if more_items.isnumeric() and len(self.bag) - 1 >= int(more_items):
                                        more_items_flag = False
                                        self.put_on_items(int(more_items))
                                    elif str(more_items).lower() == "no":
                                        more_items_flag = False
                                        print('Alright')
                                        return None
                                    else:
                                        print('Wrong input')
                            else:
                                print("You have nothing in your bag")
                        else:
                            print('Wrong input')
            elif item.armor_type == 'helmet':  # Same story with helmet
                if self.head == items.naked:
                    print(f'You put {item.name} on feet')
                    self.head = self.bag_content[int(choice)]
                    self.head_armor = item.armor
                else:
                    reply_flag = True
                    while reply_flag:
                        user_input = input(f'You have {self.head.name} on you, do you want to change it? ')
                        if user_input.lower() == 'yes':
                            reply_flag = False
                            old_item = self.head
                            self.bag.append(old_item)
                            self._what_is_on.remove(old_item)
                            self.head = self.bag_content[int(choice)]
                            self.head_armor = item.armor
                            print(f'You have changed {old_item.name} for {self.head.name} ')
                        elif user_input.lower() == 'no':
                            reply_flag = False
                            if len(self.bag_content) > 0:
                                more_items_flag = True
                                while more_items_flag:
                                    self.printbag_cnt()
                                    more_items = input('Do you want to put something else? ')
                                    if more_items.isnumeric() and len(self.bag) - 1 >= int(more_items):
                                        more_items_flag = False
                                        self.put_on_items(int(more_items))
                                    elif str(more_items).lower() == "no":
                                        more_items_flag = False
                                        print('Alright')
                                        return None
                                    else:
                                        print('Wrong input')
                            else:
                                print("You have nothing in your bag")
                        else:
                            print('Wrong input')
        elif isinstance(item, weapon.Weapon):
            if self.active_weapon == items.fist:
                print(f'You have {item.name.lower()} in your hands')
                self.active_weapon = self.bag_content[int(choice)]
                self.active_skill = self.skills[self.active_weapon.weapon_type]
            else:
                reply_flag = True
                while reply_flag:
                    user_input = input(f'You have {self.active_weapon.name} on you, do you want to change it? ')
                    if user_input.lower() == 'yes':
                        reply_flag = False
                        old_item = self.active_weapon
                        self.bag.append(old_item)
                        self._what_is_on.remove(old_item)
                        self.active_weapon = self.bag_content[int(choice)]
                        self.active_skill = self.skills[self.active_weapon.weapon_type]
                        print(f'You have changed {old_item.name} for {self.active_weapon.name}')
                    elif user_input.lower() == 'no':
                        reply_flag = False
                        if len(self.bag_content) > 0:
                            more_items_flag = True
                            while more_items_flag:
                                self.printbag_cnt()
                                more_items = input('Do you want to put something else? ')
                                if more_items.isnumeric() and len(self.bag) - 1 >= int(more_items):
                                    more_items_flag = False
                                    self.put_on_items(int(more_items))
                                elif str(more_items).lower() == "no":
                                    more_items_flag = False
                                    print('Alright')
                                    return None
                                else:
                                    print('Wrong input')
                        else:
                            print("You have nothing in your bag")
                    else:
                        print('Wrong input')
        else:
            repeater_flag = True
            print("Wrong item")
            while repeater_flag:
                decision = input("What do you wanna do? Try again? yes or no? ")
                if decision.lower() == 'yes':
                    repeater_flag = False
                    self.put_on_items()
                elif decision.lower() == 'no':
                    return None
                else:
                    print('Wrong input')
            return None
        self._what_is_on.append(self.bag.pop(int(choice)))
        self.hp += item.hp  # Now adds up all characteristics of a cloth to character's chr.
        self.luck += item.luck
        self.strength += item.strength
        self.agility += item.agility
        self.movement += item.movement
        self.intelligence += item.intelligence
        self.critical_chance += item.critical_chance
        self.current_max_hp()
        if len(self.bag_content) > 0:
            more_items_flag = True
            while more_items_flag:
                self.printbag_cnt()
                more_items = input('Do you want to put something else? ')
                if more_items.isnumeric() and len(self.bag)-1 >= int(more_items):
                    more_items_flag = False
                    self.put_on_items(int(more_items))
                elif str(more_items).lower() == "no":
                    more_items_flag = False
                    print('Alright')
                    return None
                else:
                    print('Wrong input')
        else:
            print("You have nothing in your bag")
        return item

    def put_off_items(self, choice=None):
        """Taking items off. Will check your input, if it is correct will put the item on you and remove it from the bag
         and add it to the whats_on list"""
        if choice is None:
            print('TAKING OFF THE ITEMS This is what is on you:')
            self.print_whats_on()
            input_choice = input('What do you want to take off:')
            if input_choice.isnumeric() and len(self._what_is_on)-1 >= int(input_choice):       # Checking input
                try:
                    choice = int(input_choice)
                except ValueError:
                    print("Input error")
                    self.put_off_items()
            elif str(input_choice) == "no":      # Checking input
                print("You decided not to take off anything")
                return None
            elif input_choice == "q":        # Exit
                print("Quiting")
                exit()
            else:       # Restart
                print("Input error")
                self.put_off_items()
        item = self._what_is_on[choice]
        if isinstance(item, armor.Armor):       # If this is an armor will proceed
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
                            self.right_arm = naked
                            self.right_arm_armor = naked.armor
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
        elif isinstance(item, weapon.Weapon):    # If this is an weapon will proceed
            print(f'You put {item.name.lower()} away from your hands')
            self.active_weapon = items.fist
            self.active_skill = self.skills[self.active_weapon.weapon_type]
        self.bag.append(self._what_is_on.pop(int(choice)))
        self.hp -= item.hp  # Now adds up all characteristics of a cloth to character's chr.
        self.luck -= item.luck
        self.strength -= item.strength
        self.agility -= item.agility
        self.movement -= item.movement
        self.intelligence -= item.intelligence
        self.critical_chance -= item.critical_chance
        self.current_max_hp()
        if len(self._what_is_on) > 0:       # Will ask if you wanna take more items off.
            more_items_flag = True
            while more_items_flag:
                self.print_whats_on()
                more_items = input('Do you want to take something else off? ')
                if more_items.isnumeric() and len(self._what_is_on)-1 >= int(more_items):
                    more_items_flag = False
                    self.put_off_items(choice=int(more_items))
                elif str(more_items).lower() == "no":
                    more_items_flag = False
                    print('Alright')
                    return None
                else:
                    print('Wrong input')
        else:
            print('You are naked')
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
        if self.critical_chance >= 100:
            return True
        else:
            chance = random.randint(self.critical_chance, 100)
            return True if chance in range(95, 100) else False

    def player_hit(self, target):
        """Gives a choice to a player to hit an enemy."""
        """To fix later. Wanted to code 'a or head' kind of response but face a bug where uses only first if"""
        flag = True
        while flag:
            where_to_hit = input(
                'Where you want to hit your enemy? a) Head, b) Torso, c) Left hand, d) Right hand, f) Legs, '
                'p) Drink potion, q) quit ')
            if where_to_hit.lower() == 'p':  # Will allow you to drink a potion in the battle
                self.health_potion()
            elif where_to_hit.lower() == "a":
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
            elif where_to_hit.lower() == 'q':
                print('Stopping the battle ')
                exit()
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
