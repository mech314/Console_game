import chr_npc
import functions
import items

#mech = hrs_profs.Hero(name='Mech', gender="Male", clan='Boyz', spec="swordsman", chr_type='player', head=items.helmet1)
#test_obj = hrs_profs.Hero(name='testman', gender="gender", clan='testers', spec="keybordman", chr_type='npc', head=items.helmet2)

good_box = [items.super_sword, items.helmet_of_holy_tester, items.vest_of_holy_tester, items.trousers_of_holy_tester, items.boots_of_holy_tester,
            items.armlet_of_holy_tester1, items.armlet_of_holy_tester2, items.small_health_potion, items.medium_health_potion,
            items.large_health_potion]

# TODO: write correct unittests


def test():
    # actions.take_all_items(chr_npc.mech, box_with_stuff)
    # chr_npc.mech.choose_weapon(1)
    # chr_npc.mech.put_on_armor()
    # chr_npc.mech.print_chr()
    # chr_npc.badboy.print_chr()
    # actions.battle(chr_npc.mech, chr_npc.badboy)
    # functions.weapon_creator(number_of_weapon=1)
    functions.create_npcs(number_of_npcs=1, requested_level=1)
    print(chr_npc.npc_list[0].name)
    print(chr_npc.npc_list[0].gender)
    print(chr_npc.npc_list[0].active_weapon.name)
    print(chr_npc.npc_list[0].active_weapon.weapon_type)
    print(chr_npc.npc_list[0].spec)
    print(chr_npc.npc_list[0].active_skill)
    print(chr_npc.npc_list[0].sword_skill)
    print(chr_npc.npc_list[0].axe_skill)
    #mech.add_item_to_thebag(good_box)
    # print(chr_npc.npc_list[0])
    # =====
    #mech.torso = items.vest_of_holy_tester
    #test_obj.chr_belongings()
    print('==========')
    #mech.chr_belongings()
    # =====
    # mech.print_chr()
    # test_obj.print_chr()
    # print(chr_npc.npc_list)
    # functions.npc_list_print(chr_npc.npc_list)
    # chr_npc.npc_list[0].print_whats_on()
    # functions.armor_creator(number_of_armor=1)
    # functions.take_item(items.weapon_list, chr_npc.mech)
    # functions.take_item(items.armor_list, chr_npc.mech)
    # functions.weapon_creator(number_of_weapon=1, list_to_append=items.gold_chest)
    # functions.armor_creator(number_of_armor=10, list_to_append=items.gold_chest)
    # functions.item_list_print(weapon_list=items.gold_chest)
    # chr_npc.mech.add_item_to_thebag(items.gold_chest)
    # chr_npc.mech.printbag_cnt()
    # chr_npc.mech.print_chr()
    # chr_npc.mech.put_on_items()
    # chr_npc.mech.print_chr()

    # for enemy in chr_npc.npc_list:
    #     enemy.chr_belongings()
    # print("Current hp", chr_npc.mech.hp)
    # print("Max recorded hp", chr_npc.mech.max_hp)
    # chr_npc.mech.put_on_items()
    #
    # for item in items.location_loot:
    #     item.print_contents()
    # chr_npc.mech.put_off_items()
    # print("Current hp", chr_npc.mech.hp)
    # print("Max recorded hp", chr_npc.mech.max_hp)
    # chr_npc.mech.put_off_items()
    # chr_npc.mech.print_chr()
    # print("Current hp", chr_npc.mech.hp)
    # print("Max recorded hp", chr_npc.mech.max_hp)
    # chr_npc.mech.put_on_items()
    # chr_npc.mech.printbag_cnt()
    # chr_npc.npc_list[0].printbag_cnt()
    # functions.weapon_list_print(weapon_list=chr_npc.mech.bag)
    # chr_npc.mech.printbag_cnt()
    # chr_npc.mech.choose_weapon(0)


if __name__ == '__main__':
    test()
