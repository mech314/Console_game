"""This file contains various functions for the game to work such as creating the NPCs, items etc"""
import random
from console_game.game import hrs_profs
from console_game.game import armor


def npc_creator(name, gender, clan, specialization, level):
    """This function will take some arguments and create an NPC
    the characteristics will depend on the level of the NPC you wanna create
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
                         "6": 1.45}

    hp = int(level_multipliers[str(level)] * random.randint(ref_hp[0], ref_hp[1]))
    luck = int(level_multipliers[str(level)] * random.randint(ref_luck[0], ref_luck[1]))
    strength = int(level_multipliers[str(level)] * random.randint(ref_strength[0], ref_strength[1]))
    agility = int(level_multipliers[str(level)] * random.randint(ref_agility[0], ref_agility[1]))
    movement = int(level_multipliers[str(level)] * random.randint(ref_movement[0], ref_movement[1]))
    intelligence = int(level_multipliers[str(level)] * random.randint(ref_intelligence[0], ref_intelligence[1]))
    critical_chance = int(1.21 * level_multipliers[str(level)])

    if specialization.lower() == "axeman":
        return hrs_profs.Axeman(str(name), str(gender), str(clan), hp=hp, luck=luck, strength=strength,
                                agility=agility,
                                movement=movement, intelligence=intelligence, critical_chance=critical_chance,
                                chr_type='npc')
    elif specialization.lower() == "swordsman":
        return hrs_profs.Swordsman(str(name), str(gender), str(clan), hp=hp, luck=luck, strength=strength,
                                   agility=agility, movement=movement, intelligence=intelligence,
                                   critical_chance=critical_chance, chr_type='npc')


def armor_creator(requested_armor_type: str = None, requested_condition: str = None, requested_level: int = None):
    """This function will create a list of random armor objects based on requested armor type and level
    if armor type is not specified it will make random items. If the level is not specified it will make random levels"""

    if requested_level is None:
        requested_level = [1, 10]
    armor_types = ['helmet', 'vest', 'jacket', 'armlet', 'trousers', 'boots']  # All types of armor
    """Determining items type here"""
    if requested_armor_type is None:
        armor_type = random.choice(armor_types)

    """Determining items level here"""
    if isinstance(requested_level, list):
        level = random.randint(requested_level[0], requested_level[1])  # Randomly chooses the item level
    else:
        level = requested_level

    condition_list = ['broken', 'rusty', 'simple', 'normal', 'excellent', 'heroic']  # choosing the condition
    """Determining items condition here"""
    if requested_condition is None:
        condition = random.choice(condition_list)
    else:
        condition = requested_condition

    name = str(condition) + " " + str(armor_type)
    return armor.Armor(name=name, condition=condition, level=level, armor_type=armor_type)

# if __name__ == '__main__':
#     x = armor_creator()