import actions
import items
import chr_npc

# TODO: write correct unittests

box_with_stuff = [items.rusty_sword, items.nice_sword, items.heavy_axe, items.simple_boots, items.simple_helmet,
                  items.simple_jacket, items.simple_trousers, items.simple_vest, items.simple_armlet,
                  items.simple_armlet]


def test():
    actions.take_all_items(chr_npc.mech, box_with_stuff)
    chr_npc.mech.choose_weapon(1)
    chr_npc.mech.put_on_armor()
    chr_npc.mech.print_chr()
    chr_npc.badboy.print_chr()
    actions.battle(chr_npc.mech, chr_npc.badboy)
    actions.battle(chr_npc.mech, chr_npc.badboy1)
    actions.battle(chr_npc.mech, chr_npc.badboy2)
    actions.battle(chr_npc.mech, chr_npc.badboy3)
    actions.battle(chr_npc.mech, chr_npc.bigboy)


if __name__ == '__main__':
    test()
