import hrs_profs, items, Utils, actions, chr_npc


# Create holy tester character
def completeCharacter():
    """Creates predefined character"""
    print("Here is your character!")
    playerName = "Holy Tester"
    playerGener = "Ban Hammer"
    playerSpecialization = "swordsman"
    player = hrs_profs.Hero(name=playerName, gender=playerGener, spec=playerSpecialization, chr_type='player',
                            head=items.helmet_of_holy_tester, torso=items.vest_of_holy_tester,
                            right_arm=items.armlet_of_holy_tester1, left_arm=items.armlet_of_holy_tester2,
                            legs=items.trousers_of_holy_tester, feet=items.boots_of_holy_tester,
                            active_weapon=items.super_sword)
    print("Here are your stats")
    # Print what your stats
    player.print_chr()
    print("Here is what on the character")
    # Print what you have on
    player.print_whats_on()
    return player


# Create naked character with your input
def createNakedCharacter():
    """Going to ask for input to create naked character"""
    playerName = input("What is your name? ")
    playerGener = input("What is your gender? ")
    playerSpecialization = input("What is your specialization, S - swordsman, X - axeman ")
    if playerSpecialization.lower().strip() == "s":
        playerSpecialization = "swordsman"
    elif playerSpecialization.lower().strip() == "x":
        playerSpecialization = "axeman"
    player = hrs_profs.Hero(name=playerName, gender=playerGener, spec=playerSpecialization, chr_type="player")
    return player


# Creat naked character with option to pick up loot
def createNaked_withLoot():
    """Going to ask for input to create naked character and some loot to pick up"""
    playerName = input("What is your name? ")
    playerGener = input("What is your gender? ")
    playerSpecialization = input("What is your specialization, S - swordsman, X - axeman ")
    if playerSpecialization.lower().strip() == "s":
        playerSpecialization = "swordsman"
    elif playerSpecialization.lower().strip() == "x":
        playerSpecialization = "axeman"
    player = hrs_profs.Hero(name=playerName, gender=playerGener, spec=playerSpecialization, chr_type="player")
    player.add_item_to_thebag(items.small_health_potion)
    player.add_item_to_thebag(items.simple_box)
    return player


def createPlayer():
    """Creates different character"""
    choice = None
    while not choice:
        choices = [
            ["1", "Holy Tester (very strong)"],
            ["2", "Naked (very weak)"],
            ["3", "Naked with some loot (also weak)"]
        ]
        # Prompt for user action
        choice = Utils.getUserChoice(choices)
        if choice == "1":
            player = completeCharacter()
        elif choice == "2":
            player = createNakedCharacter()
        elif choice == "3":
            player = createNaked_withLoot()
    print("Welcome to the new world of this game, adventurer.\n"
          "Your character look like this:")
    return player


# Main test menu functionality and choices
def mainModesMenu():
    # Choices what to do
    print("What do you want to do? ")
    choices = [
        ["1", "Naked Brutality (you gonna die)"],
        ["2", "Fair fight"],
        ["3", "Sandbox, you gonna kill everyone"],
        ["4", "Continuous game, fight, loot, fight etc."],
        ["5", "Check your bag"],
        ["0", "Quit."]
    ]
    # Prompt for user action
    return Utils.getUserChoice(choices)


# Fight test menu functionality and choices
def fightMenu(player, enemy):
    gameON = True
    while gameON:
        print(f"You are going to fight with {enemy.name}.\n")
        choices = [
            ["1", f"See {enemy.name} stats"],
            ["2", f"What clothes are on the {enemy.name}"],
            ["3", f"See all items {enemy.name} has"],
            ["4", "Just Fight"],
            ["5", "Put Armor and weapon on"],
            ["6", "See what is on me and my stats"],
            ["7", "See all my belongings"],
            ["8", "Run!"],
        ]
        choice = Utils.getUserChoice(choices)
        if choice == "1":
            enemy.print_chr()
        # Print enemy apparel
        elif choice == "2":
            enemy.print_whats_on()
        # Print all enemy items including apparel
        elif choice == "3":
            enemy.chr_belongings()
        # Activate battle between player and the enemy
        elif choice == "4":
            actions.battle(player, enemy)
        elif choice == "5":
            player.put_on_items()
        # Run away from the current mode into the main menu
        elif choice == "6":
            player.print_chr()
            player.print_whats_on()
        elif choice == "8":
            print(f"You ran away from {enemy.name}...\n"
                  f"You coward!")
            # Walk out of the fight section back to mode section
            gameON = False
        elif choice == "7":
            player.chr_belongings()
        # Stop program
        elif choice == "0":
            print("End, quiting.........................")
            # Changing flag False to quit section
            exit()
        if player.hp <= 0:
            # Game over
            Utils.gameOver()
            gameON = False
        # Looting functionality is unfinished
        elif enemy.hp <= 0:
            print(f"Congratulation, you have bitten {enemy.name} very easily")
            gameON = False
            # print("There is some loot dropped")
            # print(enemy.loot)
            # player.add_item_to_thebag(loot=enemy.loot)


# Naked Brutality mode
def nakedBrutalityMod(player):
    enemy = Utils.create_npcs(requested_name="Drunk fellar", requested_level=9, append_to_list=False)
    fightMenu(player, enemy)


# Fair fight mode
def fairFight(player):
    enemy = Utils.create_npcs(requested_name="Drunk fellar", requested_level=[1, 6], append_to_list=False)
    fightMenu(player, enemy)


# Sand box mode
def sandBoxFight(player):
    enemy = Utils.create_npcs(requested_level=1, append_to_list=False)
    fightMenu(player, enemy)


# Continous mode
def continousMode(player):
    Utils.create_npcs(requested_level=[1, 10], number_of_npcs=2)
    for enemy in chr_npc.npc_list:
        fightMenu(player, enemy)
