import random


def bag_contents_chance():
    """Will calculate the chance and the amount of items to put into the bag"""
    number_of_items = False
    if random.randint(0, 100) < 90:
        if random.randint(0, 100) < 10:
            number_of_items = 3
        elif random.randint(0, 100) < 30:
            number_of_items = 2
        elif random.randint(0, 100) < 100:
            number_of_items = 1
    return number_of_items


def printer():
    if bag_contents_chance():
        print(bag_contents_chance())




printer()