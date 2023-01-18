"""Dictionary containing the multipliers for item condition"""
item_modifier = {
    'broken': 0.5,
    'rusty': 0.6,
    'simple': 0.8,
    'normal': 1,
    'excellent': 1.2,
    'heroic': 1.3
}

"""Dictionary containing the multipliers for each level"""
level_multipliers = {
    "1": 1,
    "2": 1.13,
    "3": 1.2,
    "4": 1.29,
    "5": 1.33,
    "6": 1.45,
    "7": 1.49,
    "8": 1.53,
    "9": 1.55,
    "10": 1.9,
    "11": 2.4
}

"""Dictionary containing the reference stats for NPCs"""
ref_stats = {
    "hp": (90, 120),
    "luck": (1, 3),
    "strength": (2, 5),
    "agility": (1, 3),
    "movement": (1, 4),
    "intelligence": (1, 3),
}

armor_types = ['helmet', 'vest', 'jacket', 'armlet', 'trousers', 'boots']  # All types of armor
weapon_types = ['sword', 'small sword', 'heavy sword', 'axe', 'heavy axe', 'small axe']  # All types of weapon
swords = ['sword', 'small sword', 'heavy sword']     # All Sword types
axes = ['axe', 'heavy axe', 'small axe']    # All Axe types
condition_list = ['broken', 'rusty', 'simple', 'normal', 'excellent', 'heroic']  # Types of item conditions
genders = ['male', 'female', 'ork', 'child']  # all genders
clans = ['Boyz', 'Strangers']  # all clans
specializations = ['axeman', 'swordsman']  # all specs