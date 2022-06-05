# class Helmet(Armor):
#     """Everything that will be on your head"""
#
#     def __init__(self, name, armor, durability, hp=0, luck=0, strength=0, agility=0,
#                  movement=0, intelligence=0, critical_chance=0, armor_type=None):
#         super().__init__(name, armor, durability, hp, luck, strength, agility,
#                          movement, intelligence, critical_chance, armor_type)
#         self.armor_type = 'helmet'
#
#
# class Jacket(Armor):
#     """Jacket has sleeves so it protect torso and both hands"""
#
#     def __init__(self, name, armor, durability, hp=0, luck=0, strength=0, agility=0,
#                  movement=0, intelligence=0, critical_chance=0, armor_type=None):
#         super().__init__(name, armor, durability, hp, luck, strength, agility,
#                          movement, intelligence, critical_chance, armor_type)
#         self.armor_type = 'jacket'
#
#
# class Vest(Armor):
#     """Vest has not sleeves, so it will protect only torso"""
#
#     def __init__(self, name, armor, durability, hp=0, luck=0, strength=0, agility=0,
#                  movement=0, intelligence=0, critical_chance=0, armor_type=None):
#         super().__init__(name, armor, durability, hp, luck, strength, agility,
#                          movement, intelligence, critical_chance, armor_type)
#         self.armor_type = 'vest'
#
#
# class Armlet(Armor):
#     """Will be on your arms, can be used only with Vest or without anything on torso, could be used on both hands"""
#
#     def __init__(self, name, armor, durability, hp=0, luck=0, strength=0, agility=0,
#                  movement=0, intelligence=0, critical_chance=0, armor_type=None):
#         super().__init__(name, armor, durability, hp, luck, strength, agility,
#                          movement, intelligence, critical_chance, armor_type)
#         self.armor_type = 'armlet'
#
#
# class Trousers(Armor):
#     """Everything that will be on your legs"""
#
#     def __init__(self, name, armor, durability, hp=0, luck=0, strength=0, agility=0,
#                  movement=0, intelligence=0, critical_chance=0, armor_type=None):
#         super().__init__(name, armor, durability, hp, luck, strength, agility,
#                          movement, intelligence, critical_chance, armor_type)
#         self.armor_type = 'trousers'
#
#
# class Boots(Armor):
#     """Everything that will be on your feet"""
#
#     def __init__(self, name, armor, durability, hp=0, luck=0, strength=0, agility=0,
#                  movement=0, intelligence=0, critical_chance=0, armor_type=None):
#         super().__init__(name, armor, durability, hp, luck, strength, agility,
#                          movement, intelligence, critical_chance, armor_type)
#         self.armor_type = 'boots'
#
#
# class Naked(Armor):
#     """Just naked"""
#
#     def __init__(self, name, armor, durability=math.inf, hp=0, luck=0, strength=0, agility=0,
#                  movement=0, intelligence=0, critical_chance=0, armor_type=None):
#         super().__init__(name, armor, durability, hp, luck, strength, agility,
#                          movement, intelligence, critical_chance, armor_type)
#         self.armor_type = 'naked'
