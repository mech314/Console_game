############################################
# Utils.py
# Utility functions
# This file contains various functions for the game to work such as creating the NPCs, items etc
############################################


# Imports
import random
from colorama import Fore
import armor
import chr_npc
import global_vars
import hrs_profs
import weapon


def npc_creator(name: str, gender: str, clan: str, specialization: str, level: int, armored: bool = True,
                bag_contents: bool = True, list_to_append: list = chr_npc.npc_list):
    """This function will take some arguments and create an NPC the characteristics will depend on the level of the
    NPC you wanna create. Indicate the list where these NPC will be added
    Here are values for level 1 NPC
    """

    def bag_contents_chance():
        """Will calculate the chance and the amount of items to put into the bag"""
        items_to_add = False
        if random.randint(0, 100) < 15:
            if random.randint(0, 100) < 10:
                items_to_add = 3
            elif random.randint(0, 100) < 30:
                items_to_add = 2
            elif random.randint(0, 100) < 100:
                items_to_add = 1
        return items_to_add

    npc_counter = 1  # Not used now

    hp = int(global_vars.level_multipliers[str(level)] * random.randint(*global_vars.ref_stats['hp']))
    luck = int(global_vars.level_multipliers[str(level)] * random.randint(*global_vars.ref_stats['luck']))
    strength = int(global_vars.level_multipliers[str(level)] * random.randint(*global_vars.ref_stats['strength']))
    agility = int(global_vars.level_multipliers[str(level)] * random.randint(*global_vars.ref_stats['agility']))
    movement = int(global_vars.level_multipliers[str(level)] * random.randint(*global_vars.ref_stats['movement']))
    intelligence = int(
        global_vars.level_multipliers[str(level)] * random.randint(*global_vars.ref_stats['intelligence']))
    critical_chance = int(1.21 * global_vars.level_multipliers[str(level)])

    if specialization.lower() == 'swordsman':  # Choosing weapon types to be generated based on the specialization of NPC
        weapon_type = ['sword', 'small sword', 'heavy sword']
    elif specialization.lower() == 'axeman':
        weapon_type = ['axe', 'heavy axe', 'small axe']

    if armored:
        "IF Armored functions creates and puts random armor on NPC based on NPC level+1"
        npc = hrs_profs.Hero(str(name), str(gender), str(clan), hp=hp, luck=luck, strength=strength,
                             agility=agility, movement=movement, intelligence=intelligence, level=level,
                             spec=specialization, critical_chance=critical_chance, chr_type='npc',
                             head=armor_creator(requested_armor_type='helmet', requested_level=[1, level]),
                             torso=armor_creator(requested_armor_type='vest', requested_level=[1, level]),
                             left_arm=armor_creator(requested_armor_type='armlet', requested_level=[1, level]),
                             right_arm=armor_creator(requested_armor_type='armlet', requested_level=[1, level]),
                             legs=armor_creator(requested_armor_type='trousers', requested_level=[1, level]),
                             feet=armor_creator(requested_armor_type='boots', requested_level=[1, level]),
                             active_weapon=weapon_creator(requested_weapon_type=random.choice(weapon_type),
                                                          requested_level=[1, level]))

    """ If NPC to have something in the bag, bg_contents_chance() will calculate a chance of adding something to the bag
    typically 15%. It will return the number of items to add. Example: if number_of_items it will add 2 weapons and 2 armors.
    Levels are random from 1 to NPC+1 level"""
    if bag_contents:
        number_of_items = bag_contents_chance()
        if number_of_items:
            weapon_creator(number_of_weapon=number_of_items, requested_level=[1, level + 1], add_tobag=True,
                           character=npc)
            armor_creator(number_of_armor=number_of_items, requested_level=[1, level + 1], add_tobag=True,
                          character=npc)

    list_to_append.append(npc)
    return None


def create_npcs(requested_name: str = None, requested_gender: str = None, requested_clan: str = None,
                requested_spec: str = None, requested_level=None, number_of_npcs: int = None):
    """This function will make several NPCs and put them into the npc_list list"""
    levels = [1, 10]  # default range of levels
    npc_name_counter = 0
    if number_of_npcs is None:
        number_of_npcs = 1
    else:
        number_of_npcs = number_of_npcs
    for npc in range(1, number_of_npcs + 1):
        if requested_gender is None:
            gender_choice = random.choice(global_vars.genders)
            gender = gender_choice
        else:
            requested_gender = requested_gender

        if requested_clan is None:
            clan_choice = random.choice(global_vars.clans)
            clan = clan_choice
        else:
            requested_clan = requested_clan

        if requested_spec is None:
            specialization_choice = random.choice(global_vars.specializations)
            spec = specialization_choice
        else:
            spec = requested_spec

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


def armor_creator(requested_armor_type: str = None, requested_condition: str = None, requested_level=None,
                  number_of_armor: int = None, list_to_append=None, add_tobag=False, character=None):
    """This function will create a list of random armor objects based on requested armor type and level
    if armor type is not specified it will make random items. If the level is not specified it will make random levels.
    Indicate the list where these NPC will be added"""
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
            armor_type_choice = random.choice(global_vars.armor_types)
            armor_type = armor_type_choice
        else:
            armor_type = requested_armor_type
        """Determining items condition here"""
        if requested_condition is None:
            condition_choice = random.choice(global_vars.condition_list)
            condition = condition_choice
        else:
            condition = requested_condition
        name = str(condition) + " " + str(armor_type)
        armor_item = armor.Armor(name=name, condition=condition, level=level, armor_type=armor_type)
        """Erase all previous selections"""
        level = None
        armor_type = None
        condition = None
        if add_tobag:
            loot_list = [armor_item]
            character.add_item_to_thebag(loot_list)
    if list_to_append is None:  # Is used when we use this function with NPC creation and put weapon\clothes on the NPC
        return armor_item
    else:
        return None


def weapon_creator(requested_weapon_type=None, requested_condition: str = None, requested_level=None,
                   number_of_weapon: int = None, list_to_append=None, add_tobag=False, character=None):
    """This function will create a list of random weapons objects based on requested weapon type and level
        if weapon type is not specified it will make random items. If the level is not specified it will
        make random levels. Indicate the list where these NPC will be added"""

    if number_of_weapon is None:
        number_of_weapon = 1
    for weapon_iter in range(1, number_of_weapon + 1):
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
            weapon_type_choice = random.choice(global_vars.weapon_types)
            weapon_type = weapon_type_choice
        elif isinstance(requested_weapon_type, list):
            weapon_type = random.choice(requested_weapon_type)
        else:
            weapon_type = requested_weapon_type
        """Determining items condition here"""
        if requested_condition is None:
            condition_choice = random.choice(global_vars.condition_list)
            condition = condition_choice
        else:
            condition = requested_condition
        name = str(condition) + " " + str(weapon_type)
        weapon_item = weapon.Weapon(name=name, condition=condition, level=level, weapon_type=weapon_type)
        """Erase all previous selections"""
        level = None
        weapon_type = None
        condition = None
        if add_tobag:
            loot_list = [weapon_item]
            character.add_item_to_thebag(loot_list)
    if list_to_append is None:  # Is used when we use this function with NPC creation and put weapon\clothes on the NPC
        return weapon_item
    else:
        return None


def npc_list_print(npc_list):
    """Will print all NPC from the NPC list in chr_npc module"""
    if isinstance(npc_list, list):
        for npc in npc_list:
            npc_dict = npc.characteristics
            print("\n")
            for key, value in npc_dict.items():
                print(key, ":", value)
    else:
        npc_dict = npc_list.characteristics
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


def item_list_print(weapon_list: list):
    """Will print all armor from the armor list in items module"""
    for weapon_item in weapon_list:
        print("\n")
        if weapon_item.item_type == 'weapon':
            print('\nName', ':', weapon_item.name.capitalize(),
                  '\nCondition', weapon_item.condition,
                  '\nHp: ', weapon_item.hp,
                  '\nDamage: ', weapon_item.damage,
                  '\nDurability:', weapon_item.durability,
                  '\nLuck: ', weapon_item.luck,
                  '\nStrength: ', weapon_item.strength,
                  '\nAgility: ', weapon_item.agility,
                  '\nMovement: ', weapon_item.movement,
                  '\nIntelligence: ', weapon_item.intelligence,
                  '\nCritical chance: ', weapon_item.critical_chance,
                  '\nLevel: ', weapon_item.level)
        elif weapon_item.item_type == 'clothes':
            print('\nName', ':', weapon_item.name.capitalize(),
                  '\nCondition', weapon_item.condition,
                  '\nHp: ', weapon_item.hp,
                  '\nArmor: ', weapon_item.armor,
                  '\nDurability:', weapon_item.durability,
                  '\nLuck: ', weapon_item.luck,
                  '\nStrength: ', weapon_item.strength,
                  '\nAgility: ', weapon_item.agility,
                  '\nMovement: ', weapon_item.movement,
                  '\nIntelligence: ', weapon_item.intelligence,
                  '\nCritical chance: ', weapon_item.critical_chance,
                  '\nLevel: ', weapon_item.level)


# getUserChoice()
# Displays a list of options, prompts for an option, and returns it
# Pass it a list of lists in format [["Letter","Display Text"]]
# Example: [["A","Option A"],["B","Option B"],["C","Option C"]]
# Returns selected letter
def getUserChoice(options):
    # Create a variable to hold valid inputs
    validInputs = ""
    # Loop through the options
    for opt in options:
        # Add this one to the valid letters list
        validInputs += opt[0]
        # And display it
        print(Fore.YELLOW + opt[0], "-", Fore.YELLOW + opt[1])
    # Create the prompt
    prompt = "What do you want to do? [" + validInputs + "]: "
    # Initialize variables
    choice = ""
    done = False
    # Main loop
    while not done:
        # Get a single upper case character
        choice = input(prompt).strip().upper()
        # If the user entered more than 1 character
        if len(choice) > 1:
            # Just use the first
            choice = choice[0]
        # Do we have 1 valid input?
        if len(choice) == 1 and choice in validInputs:
            # We do, outa here!
            done = True
    # Return the selected option
    return choice


# inputNumber()
# Numeric input function
def inputNumber(prompt):
    # Input variable
    inp = ""
    # Loop until variable is a valid number
    while not inp.isnumeric():
        # Prompt for input
        inp = input(prompt).strip()
    # Return the number
    return int(inp)


# inputYesNo()
# User picks Yes or No, return True or False
def inputYesNo(text):
    # Loop until
    while True:
        # Display prompt
        x = input(text + " [Y/N]").upper()
        # Check response
        if x in ["Y", "YES"]:
            return True
        elif x in ["N", "NO"]:
            return False

def gameOver():
    print("GameOver")