import random
from hrs_profs import Hero

base_strenght = 5
base_agility = 3
base_intelect = 6
base_luck = 2
skill = 3
wpn_dmg = (4, 14)
hit_points = 130

potions = {"small": (0, 7), 'medium': (5, 12), 'large': (25, 70)}
potions_in_pocket = ['small', 'small', 'large', 'medium']


def damage(strength, agility, skill, wpn_dmg=()):
    """Calculates the damage from a weapon based on chr charactetistics"""
    modifier = 1 + (strength / 100) + (agility / 150) + (skill / 10)
    return modifier * random.randint(wpn_dmg[0], wpn_dmg[1])


def getting_hit(whom_to_hit, dmg):
    """Takes damage from "damage" function and subtracts it from the Hero's health """
    return whom_to_hit.base_hp - dmg


def unlucky(luck):
    """Chance to harm yourself.
    Based on based_luck calculates the chance of unsucssefull potion application"""
    luck_level = ((20 / luck), 250 * (luck / 10))
    return random.randint(luck_level[0], luck_level[1])


def health_potion(health, luck):
    """Takes a value from potion dictionary and adds value to healths"""
    if len(potions_in_pocket) != 0:
        luck_level = unlucky(luck)
        mod = 1 + (base_intelect / 100) + (luck / 10)  # modifier for potion effect based on your skills and luck
        flag = True
        while flag and len(potions_in_pocket) != 0:
            potion = str.lower(input(str("You have {} potions, choose your potion: ".format(potions_in_pocket))))
            if potion in potions_in_pocket:
                potions_in_pocket.remove(potion)
                flag = False
            else:
                print("You do not have this potion, choose from what you have in your pocket: ", potions_in_pocket)
        min_eff, max_eff = potions[potion][0], potions[potion][1]
        potion_effect = int(random.randint(min_eff, max_eff) * mod)

        if 10 < luck_level < 15:
            print("You are unlucky, potion poisoned your for {} hit points".format(potion_effect))
            return health - potion_effect
        else:
            print("Potion will add {} hit points".format(potion_effect))
            return health + potion_effect
    else:
        return "You have no potions, no luck."


# x = 0
# while x < 1:
#     print(health_potion(hit_points, base_luck))
#     x += 1
#


# print(getting_hit(hit_points, damage(base_strenght, base_agility, skill, wpn_dmg)))