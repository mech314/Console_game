import items
import Utils

bag = []


def add_item_to_thebag(loot: list, specific_item=None):
    if specific_item or specific_item == 0:
        bag.append(loot[specific_item])
        del loot[specific_item]
    else:
        exitFlag = False
        print("What items you want to take?\n"
              "______________________________")
        while not exitFlag:
            choices = [["D", "I'm done!"]]
            print("Currently in the box:")
            for count, item in enumerate(loot, start=0):
                choices.insert(len(loot), [str(count), item.name])
                print("________________________________")
                print(count, item.name)
            for item in bag:
                print("Your bag contents: ")
                print(item.name)
                print("________________________________")
            print("What do you want to do? ")
            print("________________________________")
            choice = Utils.getUserChoice(choices)
            if str(choice) == "D":
                exitFlag = True
            elif isinstance(int(choice), int):
                bag.append(loot[int(choice)])
                del loot[int(choice)]


print("___________________________________\n")
add_item_to_thebag(items.good_box, specific_item=0)
print("Now in the box")
for item in items.good_box:
    print(item.name)
