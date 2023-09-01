import hrs_profs
import Utils
import actions
import chr_npc
import items


# TODO: Implement choices, alternative options and check for input.
def createPlayer():
    """At the beginning ask player for the input to create a new player."""
    playerName = input("What is your name? ")
    playerGener = input("What is your gender? ")
    playerSpecialization = input("What is your specialization, S - swordsman, X - axeman ")
    #playerName = "A"
    #playerGener = "b"
    #playerSpecialization = "s"
    if playerSpecialization.lower().strip() == "s":
        playerSpecialization = "swordsman"
    elif playerSpecialization.lower().strip() == "x":
        playerSpecialization = "axeman"
    player = hrs_profs.Hero(name=playerName, gender=playerGener, spec=playerSpecialization, chr_type="player")
    print("Welcome to the new world of this game, adventurer.\n"
          "Your character look like this:")
    player.print_chr()
    return player


def doStart():
    print("You are starting the game.\n"
          "This is the first running beta of the game.\n"
          "Let's start from creating the character.\n"
          "============================================\n")
    print("Let's create the character first.")
    player = createPlayer()
    # Flag for exiting the game
    exitFlag = False
    print("What do you want to do? ")
    # TODO Make options for the game, several modes, continuous fights, looking for loot etc. Make npc and character
    #  with clothes
    while player.hp > 0 and not exitFlag:
        choices = [
            ["N", "Naked Brutality (you gonna die)"],
            ["F", "Fair fight"],
            ["S", "Sandbox, you gonna kill everyone"],
            ["G", "Continuous game, fight, loot, fight etc."],
            ["B", "Check your bag"],
        ]
        # Prompt for user action
        choice = Utils.getUserChoice(choices)
        # Perform action
        if choice == "N":
            # Flag for continuous regime
            gameON = True
            while gameON:
                Utils.create_npcs(number_of_npcs=1, requested_name="Drunk fellar", requested_level=9)
                enemy = chr_npc.npc_list[0]
                print(f"You are going to fight with {enemy.name}.\n")
                choices = [
                    ["S", f"See {enemy.name} stats"],
                    ["C", f"What clothes are on the {enemy.name}"],
                    ["B", f"See all items {enemy.name} has"],
                    ["F", "Just Fight"],
                    ["Q", "Run!"],
                ]
                choice = Utils.getUserChoice(choices)
                if choice == "S":
                    enemy.print_chr()
                elif choice == "C":
                    enemy.print_whats_on()
                elif choice == "B":
                    enemy.chr_belongings()
                elif choice == "F":
                    actions.battle(player, enemy)
                elif choice == "Q":
                    print(f"You ran away from {enemy.name}...\n"
                          f"You coward!")
                    gameON = False
                if player.hp <= 0:
                    # Game over
                    Utils.gameOver()
                    gameON = False
                    exitFlag = True
        elif choice == "F":
            # Flag for continuous regime
            Utils.create_npcs(number_of_npcs=1, requested_level=player.level + 3)
            enemy = chr_npc.npc_list[0]
            player.add_item_to_thebag(items.small_health_potion)
            player.chr_belongings()
            player.add_item_to_thebag(items.simple_box)
            gameON = True
            while gameON:
                print(f"You are going to fight with {enemy.name}.\n")
                choices = [
                    ["S", f"See {enemy.name} stats"],
                    ["C", f"What clothes are on the {enemy.name}"],
                    ["B", f"See all items {enemy.name} has"],
                    ["F", "Just Fight"],
                    ["Q", "Run!"],
                    ["A", "Put Armor and weapon on"],
                    ["G", "See what is on me and my stats"],
                    ["Z", "See all my belongings"]
                ]
                choice = Utils.getUserChoice(choices)
                if choice == "S":
                    enemy.print_chr()
                elif choice == "C":
                    enemy.print_whats_on()
                elif choice == "G":
                    player.print_chr()
                    player.print_whats_on()
                elif choice == "A":
                    player.put_on_items()
                elif choice == "Z":
                    player.chr_belongings()
                elif choice == "B":
                    enemy.chr_belongings()
                elif choice == "F":
                    actions.battle(player, enemy)
                elif choice == "Q":
                    print(f"You ran away from {enemy.name}...\n"
                          f"You coward!")
                    gameON = False
                if player.hp <= 0:
                    # Game over
                    Utils.gameOver()
                    gameON = False
                    exitFlag = True
                elif enemy.hp <= 0:
                    print(f"Congratulation, you have bitten {enemy.name} very easily")
                    # print("There is some loot dropped")
                    # print(enemy.loot)
                    # player.add_item_to_thebag(loot=enemy.loot)
        elif choice == "S":
            pass
        elif choice == "G":
            print("This mode is not available yet")
        elif choice == "B":
            player.printbag_cnt()


if __name__ == '__main__':
    doStart()
