from console_game.game import actions
from console_game.game import items
from console_game.game import chr_npc
from console_game.game import functions
from console_game.game import hrs_profs

# TODO: write correct unittests

# box_with_stuff = [items.rusty_sword, items.nice_sword, items.heavy_axe, items.simple_boots, items.simple_helmet,
#                   items.simple_jacket, items.simple_trousers, items.simple_vest, items.simple_armlet,
#                   items.simple_armlet]
from console_game.game.chr_npc import npc_list


def test():
    # actions.take_all_items(chr_npc.mech, box_with_stuff)
    # chr_npc.mech.choose_weapon(1)
    # chr_npc.mech.put_on_armor()
    # chr_npc.mech.print_chr()
    # chr_npc.badboy.print_chr()
    # actions.battle(chr_npc.mech, chr_npc.badboy)
    # functions.weapon_creator(number_of_weapon=1)
    # functions.create_npcs(number_of_npcs=5)
    # print(chr_npc.npc_list)
    # functions.npc_list_print(chr_npc.npc_list)
    # chr_npc.npc_list[0].print_whats_on()
    # functions.armor_creator(number_of_armor=1)
    # functions.take_item(items.weapon_list, chr_npc.mech)
    # functions.take_item(items.armor_list, chr_npc.mech)
    """This doesn't work. Need to be able to print the stuff in the bag regardless armor or weapon it is."""
    # functions.weapon_creator(number_of_weapon=5, list_to_append=chr_npc.mech.bag)
    # functions.armor_creator(number_of_armor=10, list_to_append=chr_npc.mech.bag)
    # functions.weapon_list_print(weapon_list=chr_npc.mech.bag)

    # chr_npc.mech.print_bag_cnt()
    # chr_npc.mech.choose_weapon(0)


if __name__ == '__main__':
    test()
    # test_clothes()
