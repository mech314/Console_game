############################################
# Locations.py
# Location and map
# This file contains class for locations and map features
############################################
# Imports
import random
from abc import ABC, abstractmethod
import Effects
import hrs_profs


class Locations(ABC):
    def __init__(self,
                 coordinates: list,
                 terrain: str,
                 structures: list,
                 loot: list,
                 npc: list,
                 external_effect: object):
        self.coordinates = coordinates
        self.terrain = terrain
        self.structures = structures
        self.loot = loot
        self.npc = npc
        self.external_effect = external_effect

    def __repr__(self):
        return f'You are in {self.coordinates}, which has {self.external_effect.effect_name} effect on you.'


class Location(Locations):
    def __init__(self,
                 coordinates=None,  # Coordinates printed in 2D like 0,0 or 1,1
                 terrain="Plain",  # Type of terrain, don't know why now
                 structures=[],  # Any buildings, caves, mine etc
                 loot=[],  # Loot will be dropped here
                 npc=[],  # NPC will be now created to the list of npc for each location
                 external_effect=None):
        super().__init__(coordinates,
                         terrain,
                         structures,
                         loot,
                         npc,
                         external_effect)
        if coordinates is None:
            self.coordinates = [0, 0]

        # When enter the location change character's coordinates and add stats
        def enterLocation(player, effect):
            player.location = self.coordinates
            addEffect(player, effect)

        # When leave the location change character's coordinates and add stats
        def leaveLocation(player, effect):
            player.location = None
            removeEffect(player, effect)

        # Adds the effect of the location to player stats
        def addEffect(player, effect):
            if effect.effect_name != "no effect":
                player.hp += effect.hp,
                player.luck += effect.luck,
                player.strength += effect.strength,
                player.agility += effect.agility,
                player.movement += effect.movement,
                player.intelligence += effect.intelligence,
                player.critical_chance += effect.critical_chance,
                player.sword_skill += effect.sword_skill,
                player.knife_skill += effect.knife_skill,
                player.axe_skill += effect.axe_skill,
                player.bow_skill += effect.bow_skill,
                player.fist_skill += effect.fist_skill

        # Removes the effect of the location to player stats
        def removeEffect(player, effect):
            if effect.effect_name != "no effect":
                player.hp -= effect.hp,
                player.luck -= effect.luck,
                player.strength -= effect.strength,
                player.agility -= effect.agility,
                player.movement -= effect.movement,
                player.intelligence -= effect.intelligence,
                player.critical_chance += effect.critical_chance,
                player.sword_skill -= effect.sword_skill,
                player.knife_skill -= effect.knife_skill,
                player.axe_skill -= effect.axe_skill,
                player.bow_skill -= effect.bow_skill,
                player.fist_skill -= effect.fist_skill


loc_0_0 = Location(coordinates=[0, 0], terrain="Plain", structures=[], loot=[], npc=[], external_effect=Effects.city)
loc_1_0 = Location(coordinates=[1, 0], terrain="Plain", structures=[], loot=[], npc=[],
                   external_effect=Effects.no_effect)
loc_1_m1 = Location(coordinates=[1, -1], terrain="Plain", structures=[], loot=[], npc=[], external_effect=Effects.city)
loc_0_m1 = Location(coordinates=[0, -1], terrain="Plain", structures=[], loot=[], npc=[], external_effect=Effects.city)
loc_m1_m1 = Location(coordinates=[-1, -1], terrain="Plain", structures=[], loot=[], npc=[],
                     external_effect=Effects.city)
loc_m1_0 = Location(coordinates=[-1, 0], terrain="Plain", structures=[], loot=[], npc=[], external_effect=Effects.city)
loc_m1_1 = Location(coordinates=[-1, 1], terrain="Plain", structures=[], loot=[], npc=[], external_effect=Effects.city)
loc_0_1 = Location(coordinates=[0, 1], terrain="Plain", structures=[], loot=[], npc=[], external_effect=Effects.city)
loc_1_1 = Location(coordinates=[1, 1], terrain="Plain", structures=[], loot=[], npc=[], external_effect=Effects.city)
