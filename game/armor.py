import random
import global_vars
from dataclasses import dataclass
from typing import Dict, Tuple, NamedTuple, Any


class ArmorStat(NamedTuple):
    a: Tuple[int, int]
    b: Tuple[int, int]


_armor_types = {
    "helmet": {
        "armor": ArmorStat((1, 4), (3, 5)),
        "durability": (15, 30),
        "hp": (0, 1),
        "luck": (1, 3),
        "strength": (0, 0),
        "agility": (-3, -1),
        "movement": (-3, -1),
        "intelligence": (1, 5),
        "critical_chance": (0, 5),
    },
    "jacket": {
        "armor": ArmorStat((3, 7), (7, 9)),
        "durability": (25, 45),
        "hp": (5, 15),
        "luck": (1, 3),
        "strength": (1, 4),
        "agility": (0, 0),
        "movement": (1, 3),
        "intelligence": (0, 0),
        "critical_chance": (0, 5),
    },
    "vest": {
        "armor": ArmorStat((2, 5), (6, 8)),
        "durability": (15, 30),
        "hp": (5, 10),
        "luck": (0, 0),
        "strength": (2, 5),
        "agility": (-1, 3),
        "movement": (1, 3),
        "intelligence": (0, 0),
        "critical_chance": (0, 5),
    },
    "armlet": {
        "armor": ArmorStat((1, 3), (4, 5)),
        "durability": (15, 30),
        "hp": (1, 5),
        "luck": (1, 3),
        "strength": (1, 3),
        "agility": (-3, -1),
        "movement": (-2, -1),
        "intelligence": (0, 0),
        "critical_chance": (0, 5),
    },
    "trousers": {
        "armor": ArmorStat((1, 4), (3, 5)),
        "durability": (15, 30),
        "hp": (1, 5),
        "luck": (1, 3),
        "strength": (5, 7),
        "agility": (1, 7),
        "movement": (3, 9),
        "intelligence": (0, 0),
        "critical_chance": (0, 5),
    },
    "boots": {
        "armor": ArmorStat((1, 4), (3, 5)),
        "durability": (15, 30),
        "hp": (15, 30),
        "luck": (1, 3),
        "strength": (1, 3),
        "agility": (1, 6),
        "movement": (5, 10),
        "intelligence": (0, 0),
        "critical_chance": (0, 5),
    },
}


@dataclass
class Armor:
    """Class for armor"""
    _id = 0

    name: str
    condition: Any = None
    armor: Tuple[int, int] = (0, 0)
    durability: int = 0
    hp: int = 0
    luck: int = 0
    strength: int = 0
    agility: int = 0
    movement: int = 0
    intelligence: int = 0
    critical_chance: int = 0
    level: int = 1
    item_type: str = 'clothes'
    armor_type: str = ''
    not_custom: bool = True

    item_modifier: Dict[str, float] = None

    def __post_init__(self):
        # Why not use a global variable for this?
        Armor._id += 1

        if self.condition is None:  # If condition is 'naked' armor will be just naked.
            self.armor = (0, 1)
            self.armor_type = 'naked'
        elif self.condition:
            self.armor_maker()

    def _gen_seed(self, lower: int, upper: int) -> int:
        seed = random.randint(lower, upper)
        item_stat = (self.level * global_vars.item_modifier[self.condition])
        return int(seed * item_stat)

    def _maker(self, _stats: Any) -> tuple[int, int] | int:
        if isinstance(_stats, ArmorStat):
            return self._gen_seed(*_stats.a), self._gen_seed(*_stats.b)
        else:
            return self._gen_seed(*_stats)

    def armor_maker(self):
        """This functions only for automatically generated items, Custom items will be made by hand."""
        if not self.not_custom or self.armor_type.lower() == 'naked':
            return

        item_stats = _armor_types.get(self.armor_type.lower(), None)
        if item_stats is None:
            return

        for name_stat, _stats in item_stats.items():
            setattr(self, name_stat, self._maker(_stats))

    @property
    def armor_chr(self):
        """Creates the dictionary that has all characteristics of an item even if they are equal to 0. However,
        omits some attributes  like 'not_custom' etc."""

        arm = dict(
            name=self.name,
            level=self.level,
            armor=self.armor,
            durability=self.durability,
            condition=self.condition,
            hp=self.hp,
            luck=self.luck,
            strength=self.strength,
            agility=self.agility,
            movement=self.movement,
            intelligence=self.intelligence,
            critical_chance=self.critical_chance,
            armor_type=self.armor_type,
        )
        return {k.capitalize(): v for k, v in arm.items()}

    @property
    def print_arm_chr(self):
        """Show all attributes of an object"""
        arm_chr = {key: value for (key, value) in self.__dict__.items() if value}
        return {k.capitalize(): v for k, v in arm_chr.items()}


if __name__ == '__main__':
    armor = Armor('test1', 'heroic', armor_type='helmet')
    print(armor.__dict__)
    print(armor.print_arm_chr)

    armor2 = Armor('test2', 'rusty', armor_type='jacket')
    print(armor2.armor_chr)
    print(armor2.print_arm_chr)

    armor3 = Armor('test3', 'heroic', armor_type='trousers')
    print(armor3.armor_chr)
    print(armor3.print_arm_chr)