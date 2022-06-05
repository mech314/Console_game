import random
import hrs_profs

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
        Enemy = hrs_profs.Axeman(str(name), str(gender), str(clan), hp=hp, luck=luck, strength=strength,
                                 agility=agility,
                                 movement=movement, intelligence=intelligence, critical_chance=critical_chance,
                                 chr_type='npc')
    elif specialization.lower() == "swordsman":
        Enemy = hrs_profs.Swordsman(str(name), str(gender), str(clan), hp=hp, luck=luck, strength=strength,
                                    agility=agility, movement=movement, intelligence=intelligence,
                                    critical_chance=critical_chance, chr_type='npc')
    return Enemy
