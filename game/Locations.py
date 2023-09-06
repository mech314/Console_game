############################################
# Locations.py
# Location and map
# This file contains class for locations and map features
############################################
# Imports
import random
from dataclasses import dataclass
import Effects
import hrs_profs


@dataclass()
class Location:
    """"""

    coordinates: tuple[int, int] = None,  # Coordinates printed in 2D like 0,0 or 1,1
    terrain: str = "Plain",  # Type of terrain, don't know why now
    structures: list = [],  # Any buildings, caves, mine etc
    loot: list = [],  # Loot will be dropped here
    npc: list = [],  # NPC will be now created to the list of npc for each location
    external_effect: object = None  # Instance of effect class

    def __post_init__(self):
        if self.coordinates is None:
            self.coordinates = (0, 0)
        if self.external_effect is None:
            self.external_effect = Effects.no_effect

    @property
    def locationInfo(self):
        return f'You are in {self.coordinates}, which is a {self.external_effect.effect_name}.'


loc_0_0 = Location(coordinates=(0, 0), terrain="Plain", structures=[], loot=[], npc=[], external_effect=Effects.city)
loc_1_0 = Location(coordinates=(1, 0), terrain="Plain", structures=[], loot=[], npc=[],
                   external_effect=Effects.desert)
loc_1_m1 = Location(coordinates=(1, -1), terrain="Plain", structures=[], loot=[], npc=[], external_effect=Effects.city)
loc_0_m1 = Location(coordinates=(0, -1), terrain="Plain", structures=[], loot=[], npc=[], external_effect=Effects.city)
loc_m1_m1 = Location(coordinates=(-1, -1), terrain="Plain", structures=[], loot=[], npc=[],
                     external_effect=Effects.city)
loc_m1_0 = Location(coordinates=(-1, 0), terrain="Plain", structures=[], loot=[], npc=[], external_effect=Effects.city)
loc_m1_1 = Location(coordinates=(-1, 1), terrain="Plain", structures=[], loot=[], npc=[], external_effect=Effects.city)
loc_0_1 = Location(coordinates=(0, 1), terrain="Plain", structures=[], loot=[], npc=[], external_effect=Effects.city)
loc_1_1 = Location(coordinates=(1, 1), terrain="Plain", structures=[], loot=[], npc=[], external_effect=Effects.city)
loc_2_0 = Location(coordinates=(2, 0), terrain="Plain", structures=[], loot=[], npc=[],
                   external_effect=Effects.desert)
loc_0_2 = Location(coordinates=(0, 2), terrain="Plain", structures=[], loot=[], npc=[], external_effect=Effects.city)
loc_3_0 = Location(coordinates=(3, 0), terrain="Plain", structures=[], loot=[], npc=[],
                   external_effect=Effects.desert)
