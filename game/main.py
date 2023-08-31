import hrs_profs
import Utils
import actions
import chr_npc


# TODO: Implement choices, alternative options and check for input.
def createPlayer():
    """At the beginning ask player for the input to create a new player."""
    playerName = input("What is your name? ")
    playerGener = input("What is your gender? ")
    playerSpecialization = input("What is your specialization, S - swordsman, X - axeman ")
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
# TODO Make options for the game, several modes, continuous fights, looking for loot etc. Make npc and character with
    #  clothes
    while player.hp > 0 and not exitFlag:
        choices = [
            ["F", "Get a fight with random enemy"],
            ["B", "Check your bag"],
        ]
        # Prompt for user action
        choice = Utils.getUserChoice(choices)
        # Perform action
        if choice == "F":
            Utils.create_npcs(number_of_npcs=1, requested_level=1)
            enemy = chr_npc.npc_list[0]
            actions.battle(player, enemy)
            if player.hp <= 0:
                # Game over
                Utils.gameOver()
        elif choice == "B":
            player.chr_belongings()


if __name__ == '__main__':
    doStart()
