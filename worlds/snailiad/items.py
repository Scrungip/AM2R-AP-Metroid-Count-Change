from itertools import groupby
from typing import Dict, List, Set, NamedTuple
from BaseClasses import ItemClassification


class SnailiadItemData(NamedTuple):
    classification: ItemClassification
    quantity_in_item_pool: int
    item_id_offset: int
    item_group: str = ""


item_base_id = 1000000000000  # todo actual base ID

item_table: Dict[str, SnailiadItemData] = {
    "Pea Shooter": SnailiadItemData(ItemClassification.progression, 1, 0, "Weapon"),  # todo Progression or Not
    "Boomerang": SnailiadItemData(ItemClassification.progression, 1, 0, "Weapon"),
    "Super Secret Boomerang": SnailiadItemData(ItemClassification.progression, 0, 0, "Weapon"),
    "Rainbow Wave": SnailiadItemData(ItemClassification.progression, 1, 0, "Weapon"),
    "Debug Rainbow Wave": SnailiadItemData(ItemClassification.progression, 0, 0, "Weapon"),
    "Progressive Weapon": SnailiadItemData(ItemClassification.progression, 3, 0, "Weapon"),
    "Rapid Fire": SnailiadItemData(ItemClassification.progression, 1, 0, "Modifier"),
    "Backfire": SnailiadItemData(ItemClassification.progression, 1, 0, "Modifier"),
    "Devastator": SnailiadItemData(ItemClassification.progression, 1, 0, "Modifier"),
    "Progressive Modifier": SnailiadItemData(ItemClassification.progression, 2, 0, "Modifier"),
    "Ice Snail": SnailiadItemData(ItemClassification.progression, 1, 0, "Shell"),
    "Gravity Shell": SnailiadItemData(ItemClassification.progression, 1, 0, "Shell"),
    "Magnetic Foot": SnailiadItemData(ItemClassification.progression, 0, 0, "Shell"),
    "Corkscrew Jump": SnailiadItemData(ItemClassification.progression, 0, 0, "Shell"),
    "Angel Hop": SnailiadItemData(ItemClassification.progression, 1, 0, "Shell"),
    "Full Metal Snail": SnailiadItemData(ItemClassification.progression, 1, 0, "Shell"),
    "Progressive Shell": SnailiadItemData(ItemClassification.progression, 3, 0, "Shell"),
    "Gravity Shock": SnailiadItemData(ItemClassification.progression, 1, 0, "Ability"),
    "High Jump": SnailiadItemData(ItemClassification.progression, 1, 0, "Ability"),
    "Wall Grab": SnailiadItemData(ItemClassification.progression, 1, 0, "Ability"),
    "Shell Shield": SnailiadItemData(ItemClassification.progression, 1, 0, "Ability"),
    "Shellmet": SnailiadItemData(ItemClassification.progression, 1, 0, "Ability"),
    "Helix Fragment": SnailiadItemData(ItemClassification.filler, 0, 0),
    "Nothing": SnailiadItemData(ItemClassification.filler, 0, 0),
    "Heart Container": SnailiadItemData(ItemClassification.progression, 11, 0),  # todo correct number
    "Gravity Lock": SnailiadItemData(ItemClassification.trap, 0, 0, "Trap"),
    "Weapon Lock": SnailiadItemData(ItemClassification.trap, 0, 0, "Trap"),
    "Lullaby Trap": SnailiadItemData(ItemClassification.trap, 0, 0, "Trap"),
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
