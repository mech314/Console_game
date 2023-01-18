import random
import global_vars
from dataclasses import dataclass
from typing import Dict, Tuple, NamedTuple, Any


class WeaponStat(NamedTuple):
    a: Tuple[int, int]
    b: Tuple[int, int]


_weapon_types = {
    "sword": {
        "damage": WeaponStat((1, 4), (3, 5)),
        "durability": (15, 30),
        "hp": (0, 1),
        "luck": (1, 3),
        "strength": (0, 0),
        "agility": (-3, -1),
        "movement": (-3, -1),
        "intelligence": (1, 5),
        "critical_chance": (0, 5),
    },
    "small sword": {
        "damage": WeaponStat((3, 7), (7, 9)),
        "durability": (25, 45),
        "hp": (5, 15),
        "luck": (1, 3),
        "strength": (1, 4),
        "agility": (0, 0),
        "movement": (1, 3),
        "intelligence": (0, 0),
        "critical_chance": (0, 5),
    },
    "heavy sword": {
        "damage": WeaponStat((2, 5), (6, 8)),
        "durability": (15, 30),
        "hp": (5, 10),
        "luck": (0, 0),
        "strength": (2, 5),
        "agility": (-1, 3),
        "movement": (1, 3),
        "intelligence": (0, 0),
        "critical_chance": (0, 5),
    },
    "axe": {
        "damage": WeaponStat((1, 3), (4, 5)),
        "durability": (15, 30),
        "hp": (1, 5),
        "luck": (1, 3),
        "strength": (1, 3),
        "agility": (-3, -1),
        "movement": (-2, -1),
        "intelligence": (0, 0),
        "critical_chance": (0, 5),
    },
    "small axe": {
        "damage": WeaponStat((1, 3), (4, 5)),
        "durability": (15, 30),
        "hp": (1, 5),
        "luck": (1, 3),
        "strength": (1, 3),
        "agility": (-3, -1),
        "movement": (-2, -1),
        "intelligence": (0, 0),
        "critical_chance": (0, 5),
    },
    "heavy axe": {
        "damage": WeaponStat((1, 3), (4, 5)),
        "durability": (15, 30),
        "hp": (1, 5),
        "luck": (1, 3),
        "strength": (1, 3),
        "agility": (-3, -1),
        "movement": (-2, -1),
        "intelligence": (0, 0),
        "critical_chance": (0, 5),
    }
}


@dataclass
class Weapon:
    _id = 0

    name: str
    condition: Any = None
    damage: Tuple[int, int] = (0, 0)
    durability: int = 0
    hp: int = 0
    luck: int = 0
    strength: int = 0
    agility: int = 0
    movement: int = 0
    intelligence: int = 0
    critical_chance: int = 0
    level: int = 1
    item_type: str = 'weapon'
    weapon_type: str = ''
    not_custom: bool = True

    def __post_init__(self):
        # Why not use a global variable for this?
        Weapon._id += 1

        if self.weapon_type in global_vars.swords:
            self.weapon_type = 'sword'
        elif self.weapon_type in global_vars.axes:
            self.weapon_type = 'axe'
        if self.condition is None:  # If condition is 'fist' armor will be just naked.
            self.damage = (0, 1)
            self.weapon_type = 'fist'
        elif self.condition:
            self.weapon_maker()

    def _gen_seed(self, lower: int, upper: int) -> int:
        seed = random.randint(lower, upper)
        item_stat = (self.level * global_vars.item_modifier[self.condition])
        return int(seed * item_stat)

    def _maker(self, _stats: Any) -> tuple[int, int] | int:
        if isinstance(_stats, WeaponStat):
            return self._gen_seed(*_stats.a), self._gen_seed(*_stats.b)
        else:
            return self._gen_seed(*_stats)

    def weapon_maker(self):
        """This functions only for automatically generated items, Custom items will be made by hand."""
        if not self.not_custom and self.weapon_type.lower() != 'fist':
            return

        item_stats = _weapon_types.get(self.weapon_type.lower(), None)
        if item_stats is None:
            return

        for name_stat, _stats in item_stats.items():
            setattr(self, name_stat, self._maker(_stats))

    @property
    def weapon_chr(self):
        """Creates the dictionary that has all characteristics of an item even if they are equal to 0. However,
        omits some attributes  like 'not_custom' etc."""
        wpn = dict(
            name=self.name,
            level=self.level,
            damage=self.damage,
            durability=self.durability,
            condition=self.condition,
            luck=self.luck,
            strength=self.strength,
            agility=self.agility,
            movement=self.movement,
            intelligence=self.intelligence,
            critical_chance=self.critical_chance,
            weapon_type=self.weapon_type,
            weapon_spec=self.weapon_spec,
        )
        return {k.capitalize(): v for k, v in wpn.items()}

    @property
    def print_wpn_chr(self):
        """"Show all attributes of an object"""
        arm_chr = {key: value for (key, value) in self.__dict__.items() if value}
        return {k.capitalize(): v for k, v in arm_chr.items()}


if __name__ == '__main__':
    weapon = Weapon('test1', 'excellent', weapon_type='sword')
    print(weapon.weapon_chr)
    print(weapon.print_wpn_chr)

    weapon2 = Weapon('test2', 'excellent', weapon_type='small sword')
    print(weapon2.weapon_chr)
    print(weapon2.print_wpn_chr)

    weapon3 = Weapon('test3', 'rusty', weapon_type='axe')
    print(weapon3.weapon_chr)
    print(weapon3.print_wpn_chr)