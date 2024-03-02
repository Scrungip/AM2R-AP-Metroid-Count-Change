from itertools import groupby
from typing import Dict, List, Set, NamedTuple
from BaseClasses import ItemClassification


class SnailiadItemData(NamedTuple):
    classification: ItemClassification
    quantity_in_item_pool: int
    item_id_offset: int
    item_group: str = ""
    in_game_id: int


item_base_id = 1000000000000  # todo actual base ID

item_table: Dict[str, SnailiadItemData] = {
    "Pea Shooter": SnailiadItemData(ItemClassification.progression, 1, 0, "Weapon", 0),  # todo Progression or Not
    "Boomerang": SnailiadItemData(ItemClassification.progression, 1, 0, "Weapon", 1),
    "Super Secret Boomerang": SnailiadItemData(ItemClassification.progression, 0, 0, "Weapon", 11),
    "Rainbow Wave": SnailiadItemData(ItemClassification.progression, 1, 0, "Weapon", 2),
    "Debug Rainbow Wave": SnailiadItemData(ItemClassification.progression, 0, 0, "Weapon", 12),
    "Progressive Weapon": SnailiadItemData(ItemClassification.progression, 3, 0, "Weapon", 100000),  # todo confirm with epsilon what IDs the progressibve items are
    "Rapid Fire": SnailiadItemData(ItemClassification.progression, 1, 0, "Modifier", 6),
    "Backfire": SnailiadItemData(ItemClassification.progression, 1, 0, "Modifier", 6),
    "Devastator": SnailiadItemData(ItemClassification.progression, 1, 0, "Modifier", 3),
    "Progressive Modifier": SnailiadItemData(ItemClassification.progression, 2, 0, "Modifier", 200000),
    "Ice Snail": SnailiadItemData(ItemClassification.progression, 1, 0, "Shell", 7),
    "Gravity Shell": SnailiadItemData(ItemClassification.progression, 1, 0, "Shell", 8),
    "Magnetic Foot": SnailiadItemData(ItemClassification.progression, 0, 0, "Shell", 8),
    "Corkscrew Jump": SnailiadItemData(ItemClassification.progression, 0, 0, "Shell", 8),
    "Angel Hop": SnailiadItemData(ItemClassification.progression, 1, 0, "Shell", 8),
    "Full Metal Snail": SnailiadItemData(ItemClassification.progression, 1, 0, "Shell", 9),
    "Progressive Shell": SnailiadItemData(ItemClassification.progression, 3, 0, "Shell", 300000),
    "Gravity Shock": SnailiadItemData(ItemClassification.progression, 1, 0, "Ability", 10),
    "High Jump": SnailiadItemData(ItemClassification.progression, 1, 0, "Ability", 4),
    "Wall Grab": SnailiadItemData(ItemClassification.progression, 1, 0, "Ability", 4),
    "Shell Shield": SnailiadItemData(ItemClassification.progression, 1, 0, "Ability", 5),
    "Shellmet": SnailiadItemData(ItemClassification.progression, 1, 0, "Ability", 5),
    "Helix Fragment": SnailiadItemData(ItemClassification.filler, 0, 0, "", 24),
    "Nothing": SnailiadItemData(ItemClassification.filler, 0, 0, "", 400000),
    "Heart Container": SnailiadItemData(ItemClassification.progression, 11, 0, "", 13),
    "Gravity Lock": SnailiadItemData(ItemClassification.trap, 0, 0, "Trap", 500000),
    "Weapon Lock": SnailiadItemData(ItemClassification.trap, 0, 0, "Trap", 600000),
    "Lullaby Trap": SnailiadItemData(ItemClassification.trap, 0, 0, "Trap", 700000),
    "Spider Trap": SnailiadItemData(ItemClassification.trap, 0, 0, "Trap", 800000),
}

item_name_to_id: Dict[str, int] = {name: item_base_id + data.item_id_offset for name, data in item_table.items()}

filler_items: List[str] = [name for name, data in item_table.items() if data.classification == ItemClassification.filler]


def get_item_group(item_name: str) -> str:

    return item_table[item_name].item_group


item_name_group: Dict[str, Set[str]] = {
    group: set(item_names) for group, item_names in groupby(sorted(item_table, key=get_item_group), get_item_group) if group != ""
}

extra_groups: Dict[str, Set[str]] = {
    "Flight": {"Angel Hop", "Corkscrew Jump", "Magnetic Foot", "Gravity Shell"},
    "Jump": {"High Jump", "Wall Grab"},
    "Shield": {"Shell Shield", "Shellmet"},
    "Rapid": {"Rapid Fire", "Backfire"},
}  # if item groups are requested to be added, they can be added here

item_name_group.update(extra_groups)
