import test_functions


def doStart():
    print("You are starting the game.\n"
          "This is the first running beta of the game.\n"
          "Let's start from creating the character.\n"
          "============================================\n")
    print("Let's create the character first.")
    player = test_functions.createPlayer()
    # Flag for exiting the game
    exitFlag = False

    while player.hp > 0 and not exitFlag:
        # Select game mod
        choice = test_functions.mainModesMenu()
        # Perform action
        if choice == "1":
            test_functions.nakedBrutalityMod(player)
        elif choice == "2":
            test_functions.fairFight(player)
        elif choice == "3":
            test_functions.sandBoxFight(player)
        elif choice == "4":
            test_functions.continousMode(player)
        elif choice == "5":
            player.printbag_cnt()
        elif choice == "6":
            print(player.location)
        elif choice == "0":
            # Changing flag to True to quit the program
            exitFlag = True
            print("End, quiting.........................")


if __name__ == '__main__':
    doStart()
