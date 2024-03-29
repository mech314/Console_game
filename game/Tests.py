import chr_npc
import Utils
import items
import hrs_profs
import Locations
import pygame
import sys
import Pygame_tests
import os



# Test character
traveler = hrs_profs.Hero(name='Mech', gender="Male", clan='Boyz', spec="swordsman", chr_type='player',
                          head=items.helmet1)


def locationTester(player):
    # Pygame setup
    # Initialize Pygame
    pygame.init()
    running = True

    # Build game path
    GAME_ROOT_FOLDER = os.path.dirname(__file__)
    IMAGE_FOLDER = os.path.join(GAME_ROOT_FOLDER, "Images")

    # Set frame rate
    clock = pygame.time.Clock()
    clock.tick(60)

    # Constants
    WHITE = [255, 255, 255]
    GRAY = [80, 80, 80]

    # Load images
    BACKGROUND = pygame.image.load(os.path.join(IMAGE_FOLDER, "Background.png"))
    TILE = pygame.image.load(os.path.join(IMAGE_FOLDER, "New_white_tile.png"))

    # Initialize game screen
    screen = pygame.display.set_mode(BACKGROUND.get_size())
    for tile in Locations.tile_h:
        print(tile.horiz, tile.vert, tile.adr[0], tile.adr[1])
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            mouseX, mouseY = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            for item in traveler.nearLocations():
                item.hoveredOVer(event)
                item.isPressed(event)

        # Place background
        screen.blit(BACKGROUND, (0, 0))
        for item in Locations.tile_h:
            item.draw(screen)
        traveler.draw(screen)

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()


# Create dictionary with tiles
tile_h = Pygame_tests.tileCreator()


def testLocationChange(player, new_location):
    """Test the location movement and movement restrictions"""
    print("__________________________")
    print(player.location.locationInfo)
    player.changeLocation(player.location, new_location)
    print(player.location.locationInfo)
    print(player.hp)


def testWhatIsOn():
    mech = hrs_profs.Hero(name='Mech', gender="Male", clan='Boyz', spec="swordsman", chr_type='player',
                          head=items.helmet1)
    test_obj = hrs_profs.Hero(name='testman', gender="gender", clan='testers', spec="keyboarder",
                              chr_type='npc', head=items.holy_helmet2, active_weapon=items.super_sword)
    print("______________________________\n"
          "Players stuff:")
    mech.print_whats_on()
    print("______________________________\n"
          "NPC stuff:")
    test_obj.print_whats_on()


def testPickLootPrintChrBelongings():
    """Creates the character with the items in the bag and adds more items, prints the result."""
    mech = hrs_profs.Hero(name='Mech', gender="Male", clan='Boyz', spec="swordsman", chr_type='player',
                          head=items.helmet1, bag=items.check_box)
    print(len(items.good_box))
    mech.add_item_to_thebag(items.good_box)
    mech.chr_belongings()
    print(len(items.good_box))


def test():
    # actions.take_all_items(chr_npc.mech, box_with_stuff)
    # chr_npc.mech.choose_weapon(1)
    # chr_npc.mech.put_on_armor()
    # chr_npc.mech.print_chr()
    # chr_npc.badboy.print_chr()
    # actions.battle(chr_npc.mech, chr_npc.badboy)
    # functions.weapon_creator(number_of_weapon=1)
    Utils.create_npcs(number_of_npcs=1, requested_level=1)
    print(chr_npc.npc_list[0].name)
    print(chr_npc.npc_list[0].gender)
    print(chr_npc.npc_list[0].active_weapon.name)
    print(chr_npc.npc_list[0].active_weapon.weapon_type)
    print(chr_npc.npc_list[0].spec)
    print(chr_npc.npc_list[0].active_skill)
    print(chr_npc.npc_list[0].sword_skill)
    print(chr_npc.npc_list[0].axe_skill)
    # mech.add_item_to_thebag(good_box)
    # print(chr_npc.npc_list[0])
    # =====
    # mech.torso = items.vest_of_holy_tester
    # test_obj.chr_belongings()
    print('==========')
    # mech.chr_belongings()
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
    locationTester(traveler)
