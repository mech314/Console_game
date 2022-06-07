"""This file contains various functions for the game to work such as creating the NPCs, items etc"""
import random
from console_game.game import hrs_profs
from console_game.game import armor
from console_game.game import chr_npc
from console_game.game import items
from console_game.game import weapon


def npc_creator(name: str, gender: str, clan: str, specialization: str, level: int,
                list_to_append: list = chr_npc.npc_list):
    """This function will take some arguments and create an NPC the characteristics will depend on the level of the
    NPC you wanna create. Indicate the list where these NPC will be added
    Here are values for level 1 NPC
    """
    npc_counter = 1

    ref_hp = [90, 120]
    ref_luck = [1, 3]
    ref_strength = [2, 5]
    ref_agility = [1, 3]
    ref_movement = [1, 4]
    ref_intelligence = [1, 3]

    """Dictionary containing the multipliers for each level"""

    level_multipliers = {"1": 1,
                         "2": 1.13,
                         "3": 1.2,
                         "4": 1.29,
                         "5": 1.33,
                         "6": 1.45,
                         "7": 1.49,
                         "8": 1.53,
                         "9": 1.55,
                         "10": 1.9}

    hp = int(level_multipliers[str(level)] * random.randint(ref_hp[0], ref_hp[1]))
    luck = int(level_multipliers[str(level)] * random.randint(ref_luck[0], ref_luck[1]))
    strength = int(level_multipliers[str(level)] * random.randint(ref_strength[0], ref_strength[1]))
    agility = int(level_multipliers[str(level)] * random.randint(ref_agility[0], ref_agility[1]))
    movement = int(level_multipliers[str(level)] * random.randint(ref_movement[0], ref_movement[1]))
    intelligence = int(level_multipliers[str(level)] * random.randint(ref_intelligence[0], ref_intelligence[1]))
    critical_chance = int(1.21 * level_multipliers[str(level)])

    if specialization.lower() == "axeman":
        npc = hrs_profs.Axeman(str(name), str(gender), str(clan), hp=hp, luck=luck, strength=strength,
                               agility=agility, level=level, spec=specialization, movement=movement,
                               intelligence=intelligence, critical_chance=critical_chance, chr_type='npc')
    elif specialization.lower() == "swordsman":
        npc = hrs_profs.Swordsman(str(name), str(gender), str(clan), hp=hp, luck=luck, strength=strength,
                                  agility=agility, movement=movement, intelligence=intelligence, level=level,
                                  spec=specialization, critical_chance=critical_chance, chr_type='npc')
    list_to_append.append(npc)
    return None


def create_npcs(requested_name: str = None, requested_gender: str = None, requested_clan: str = None,
                requested_spec: str = None, requested_level=None, number_of_npcs: int = None):
    """This function will make several NPCs and put them into the npc_list list"""
    genders = ['male', 'female', 'ork', 'child']  # all genders
    clans = ['Boyz', 'Strangers']  # all clans
    specializations = ['axeman', 'swordsman']  # all specs
    levels = [1, 10]  # default range of levels
    npc_name_counter = 0
    if number_of_npcs is None:
        number_of_npcs = 1
    else:
        number_of_npcs = number_of_npcs
    for npc in range(1, number_of_npcs + 1):
        if requested_gender is None:
            gender_choice = random.choice(genders)
            gender = gender_choice
        else:
            requested_gender = requested_gender

        if requested_clan is None:
            clan_choice = random.choice(clans)
            clan = clan_choice
        else:
            requested_clan = requested_clan

        if requested_spec is None:
            specialization_choice = random.choice(specializations)
            spec = specialization_choice
        else:
            requested_spec = requested_spec

        if requested_level is None:  # If nothing passed to the level it will use a range from 1 to 10, if list passed
            # use this list to randomly choose level. If int is passed-that will be the level
            level_choice = random.randint(levels[0], levels[1])
            level = level_choice
        elif isinstance(requested_level, list):
            levels = requested_level
            level_choice = random.randint(levels[0], levels[1])
            level = level_choice
        else:
            level = requested_level
        if requested_name is None:
            npc_name_counter += 1
            name_choice = "NPC" + str(npc_name_counter)
            name = name_choice
        else:
            requested_name = requested_name
        """After all parameters were defined function will make a set number of NPCs and put them into list"""
        npc_creator(name, gender, clan, spec, level)

        """Erase previous selections"""
        gender_choice = None
        clan_choice = None
        specialization_choice = None
        level_choice = None
        name_choice = None

    return None


def armor_creator(requested_armor_type: str = None, requested_condition: str = None, requested_level: int = None,
                  number_of_armor: int = None, list_to_append=items.armor_list):
    """This function will create a list of random armor objects based on requested armor type and level
    if armor type is not specified it will make random items. If the level is not specified it will make random levels.
    Indicate the list where these NPC will be added"""
    armor_types = ['helmet', 'vest', 'jacket', 'armlet', 'trousers', 'boots']  # All types of armor
    condition_list = ['broken', 'rusty', 'simple', 'normal', 'excellent', 'heroic']  # choosing the condition
    if number_of_armor is None:
        number_of_armor = 1
    for armor_iter in range(1, number_of_armor + 1):
        """Determining items level here"""
        if requested_level is None:  # If nothing passed to the level it will use a range from 1 to 10, if list passed
            # use this list to randomly choose level. If int is passed-that will be the level
            levels_to_choose = [1, 10]
            level = random.randint(levels_to_choose[0], levels_to_choose[1])
        elif isinstance(requested_level, list):
            level = random.randint(requested_level[0], requested_level[1])
        else:
            level = requested_level
        """Determining items type here"""
        if requested_armor_type is None:
            armor_type_choise = random.choice(armor_types)
            armor_type = armor_type_choise
        else:
            armor_type = requested_armor_type
        """Determining items condition here"""
        if requested_condition is None:
            condition_choice = random.choice(condition_list)
            condition = condition_choice
        else:
            condition = requested_condition
        name = str(condition) + " " + str(armor_type)
        armor_item = armor.Armor(name=name, condition=condition, level=level, armor_type=armor_type)
        list_to_append.append(armor_item)
        """Erase all previous selections"""
        level = None
        armor_type = None
        condition = None
    return None


def weapon_creator(requested_weapon_type: str = None, requested_condition: str = None, requested_level: int = None,
                  number_of_weapon: int = None, list_to_append=items.weapon_list):
    """This function will create a list of random weapons objects based on requested weapon type and level
        if weapon type is not specified it will make random items. If the level is not specified it will
        make random levels. Indicate the list where these NPC will be added"""
    weapon_types = ['sword', 'small sword', 'heavy sword', 'axe', 'heavy axe', 'small axe']  # All types of armor
    condition_list = ['broken', 'rusty', 'simple', 'normal', 'excellent', 'heroic']  # choosing the condition
    if number_of_weapon is None:
        number_of_armor = 1
    for armor_iter in range(1, number_of_weapon + 1):
        """Determining items level here"""
        if requested_level is None:  # If nothing passed to the level it will use a range from 1 to 10, if list passed
            # use this list to randomly choose level. If int is passed-that will be the level
            levels_to_choose = [1, 10]
            level = random.randint(levels_to_choose[0], levels_to_choose[1])
        elif isinstance(requested_level, list):
            level = random.randint(requested_level[0], requested_level[1])
        else:
            level = requested_level
        """Determining items type here"""
        if requested_weapon_type is None:
            weapon_type_choice = random.choice(weapon_types)
            weapon_type = weapon_type_choice
        else:
            weapon_type = requested_weapon_type
        """Determining items condition here"""
        if requested_condition is None:
            condition_choice = random.choice(condition_list)
            condition = condition_choice
        else:
            condition = requested_condition
        name = str(condition) + " " + str(weapon_type)
        armor_item = weapon.Weapon(name=name, condition=condition, level=level, weapon_type=weapon_type)
        list_to_append.append(armor_item)
        """Erase all previous selections"""
        level = None
        weapon_type = None
        condition = None
    return None


def npc_list_print(npc_list: list):
    """Will print all NPC from the NPC list in chr_npc module"""
    for npc in npc_list:
        npc_dict = npc.characteristics
        print("\n")
        for key, value in npc_dict.items():
            print(key, ":", value)


def armor_list_print(armor_list: list):
    """Will print all armor from the armor list in items module"""
    for armor_item in armor_list:
        item_dict = armor_item.armor_chr
        print("\n")
        for key, value in item_dict.items():
            print(key, ":", value)


def weapon_list_print(weapon_list: list):
    """Will print all armor from the armor list in items module"""
    for weapon_item in weapon_list:
        item_dict = weapon_item.weapon_chr
        print("\n")
        for key, value in item_dict.items():
            print(key, ":", value)


def take_item(item_list, player):
    for item in item_list:
        player.add_item_to_the_bag(item)