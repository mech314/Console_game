import hrs_profs
import items

mech = hrs_profs.Swordsman('Mech', "Male", 'Boyz', chr_type='player')

badboy = hrs_profs.Axeman('BadBoy', 'Male', 'Enemy', hp=10, head=items.simple_helmet,
                          torso=items.simple_jacket, legs=items.simple_trousers, feet=items.simple_boots,
                          active_weapon=items.heavy_axe)
badboy1 = hrs_profs.Axeman('BadBoy', 'Male', 'Enemy', hp=10, head=items.simple_helmet,
                          torso=items.simple_jacket, legs=items.simple_trousers, feet=items.simple_boots,
                          active_weapon=items.heavy_axe)
badboy2 = hrs_profs.Axeman('BadBoy', 'Male', 'Enemy', hp=10, head=items.simple_helmet,
                          torso=items.simple_jacket, legs=items.simple_trousers, feet=items.simple_boots,
                          active_weapon=items.heavy_axe)
badboy3 = hrs_profs.Axeman('BadBoy', 'Male', 'Enemy', hp=10, head=items.simple_helmet,
                          torso=items.simple_jacket, legs=items.simple_trousers, feet=items.simple_boots,
                          active_weapon=items.heavy_axe)

bigboy = hrs_profs.Axeman('BadBoy', 'Male', 'Enemy', hp=400, head=items.simple_helmet,
                          torso=items.simple_jacket, legs=items.simple_trousers, feet=items.simple_boots,
                          active_weapon=items.heavy_ass_axe)