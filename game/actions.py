import random

from colorama import Fore, Style, Back


#
# base_strenght = 5
# base_agility = 3
# base_intelect = 6
# base_luck = 2
# skill = 3
# wpn_dmg = (4, 14)
# hit_points = 130

def unlucky(player):
    """Chance to harm yourself.
    Based on based_luck calculates the chance of unsucssefull potion application"""
    luck_level = ((20 / player.luck), 250 * (player.luck / 10))
    return random.randint(luck_level[0], luck_level[1])


def health_potion(player):
    """Takes a value from potion dictionary and adds value to healths"""
    if len(potions_in_pocket) != 0:
        luck_level = unlucky(player)
        mod = 1 + (player.intelegence / 100) + (player.luck / 10)  # modifier for potion effect based on your skills
        # and luck
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


def fight(player, enemy):
    """Function that only makes actual hits during the battle"""
    player_dmg, player_hit_choice, player_critical = player.hit_enemy(enemy)
    enemy.hp -= player_dmg
    if enemy.hp < 0:
        enemy.hp = 0
    enemy_dmg, enemy_hit_choice, enemy_critical = enemy.hit_enemy(player)
    player.hp -= enemy_dmg
    if player.hp < 0:
        player.hp = 0
    return player_dmg, player_hit_choice, player_critical, enemy_dmg, enemy_hit_choice, enemy_critical


def calc_exp(enemy):
    """Calculates experience that player will gain after defeating an enemy."""
    return (enemy.level * 10) + (enemy.hp / 2)


def battle(player, enemy):
    """Automatic battle between the Player and the NPC enemy"""
    print(f'Battle between {player.name} (Hp: {player.hp}) and {enemy.name} (Hp: {enemy.hp})')
    exp = ((enemy.level * 10) + (enemy.hp / 2))  # Calculates experience

    def fight_finale():
        """Checks if somebody is dead"""
        nonlocal exp
        if player.hp <= 0 and enemy.hp <= 0:
            print("It has started nicely but everyone died.")
            return None
        elif player.hp <= 0:
            print(f'{player.name} is dead. What a shame')
            return None
        elif enemy.hp <= 0:
            enemy.loot_drop()
            print(f'{enemy.name} is dead. {player.name} has won!')
            player.exp += exp
            print(f'You gained {exp} for defeating {enemy.name}')
            player.level_up()
            return None

    exp = calc_exp(enemy)  # calculating experience from enemy's HP and level before he is dead
    while enemy.hp > 0 and player.hp > 0:
        player_dmg, player_hit_choice, player_critical, enemy_dmg, enemy_hit_choice, enemy_critical = fight(player,
                                                                                                            enemy)
        if player_critical:
            print(
                f'{player.name} punched {enemy.name} in the {player_hit_choice} for {Back.RED}{Fore.BLACK}{player_dmg} '
                f'hp!!!{Style.RESET_ALL}, {enemy.name} has {Fore.GREEN}{enemy.hp}{Style.RESET_ALL} hp')
            if enemy_critical:
                print((f'{enemy.name} punched {player.name} player in the {enemy_hit_choice} for {Back.RED}{Fore.BLACK}'
                       f'{enemy_dmg} hp!!!{Style.RESET_ALL}, {player.name} has {Fore.GREEN}{player.hp}{Style.RESET_ALL} '
                       f'hp'))
            else:
                print(f'{enemy.name} punched {player.name} in the {enemy_hit_choice} for {Fore.RED}{enemy_dmg} '
                      f'hp{Style.RESET_ALL}, {player.name} has {Fore.GREEN}{player.hp}{Style.RESET_ALL} hp')
        else:
            print(f'{player.name} punched {enemy.name} in the {player_hit_choice} for {Fore.RED}{player_dmg}'
                  f'{Style.RESET_ALL} hp, {enemy.name} has {Fore.GREEN}{enemy.hp}{Style.RESET_ALL}')
            if enemy_critical:
                print((f'{enemy.name} punched {player.name} in the {enemy_hit_choice} for {Back.RED}{Fore.BLACK}'
                       f'{enemy_dmg} hp!!!{Style.RESET_ALL}, {player.name} has {Fore.GREEN}{player.hp}{Style.RESET_ALL} '
                       f'hp'))
            else:
                print(f'{enemy.name} punched {player.name} in the {enemy_hit_choice} for {Fore.RED}'
                      f'{enemy_dmg}{Style.RESET_ALL} hp, {player.name} has {Fore.GREEN}{player.hp}{Style.RESET_ALL} hp')
        fight_finale()
