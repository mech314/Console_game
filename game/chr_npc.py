from console_game.game import hrs_profs
from console_game.game import items


npc_list = []

mech = hrs_profs.Hero(name='Mech', gender="Male", clan='Boyz', spec="Swordsman", chr_type='player', bag=[])

badboy = hrs_profs.Axeman(name="Bob", gender="male", clan="BoyZ", spec="Axeman", level=1)

# badboy = hrs_profs.Axeman('BadBoy', 'Male', 'Enemy', hp=10, head=items.simple_helmet,
#                           torso=items.simple_jacket, legs=items.simple_trousers, feet=items.simple_boots,
#                           active_weapon=items.heavy_axe)
# badboy1 = hrs_profs.Axeman('BadBoy', 'Male', 'Enemy', hp=10, head=items.simple_helmet,
#                            torso=items.simple_jacket, legs=items.simple_trousers, feet=items.simple_boots,
#                            active_weapon=items.heavy_axe)
# badboy2 = hrs_profs.Axeman('BadBoy', 'Male', 'Enemy', hp=10, head=items.simple_helmet,
#                            torso=items.simple_jacket, legs=items.simple_trousers, feet=items.simple_boots,
#                            active_weapon=items.heavy_axe)
# badboy3 = hrs_profs.Axeman('BadBoy', 'Male', 'Enemy', hp=10, head=items.simple_helmet,
#                            torso=items.simple_jacket, legs=items.simple_trousers, feet=items.simple_boots,
#                            active_weapon=items.heavy_axe)
#
# bigboy = hrs_profs.Axeman('BadBoy', 'Male', 'Enemy', hp=400, head=items.simple_helmet,
#                           torso=items.simple_jacket, legs=items.simple_trousers, feet=items.simple_boots,
#                           active_weapon=items.heavy_ass_axe)
