from itertools import groupby
from typing import Dict, List, Set, NamedTuple
from BaseClasses import ItemClassification


class SnailiadItemData(NamedTuple):
    classification: ItemClassification
    quantity_in_item_pool: int
    item_id_offset: int
    in_game_id: int
    item_group: str = ""


item_base_id = 9500000  # todo actual base ID

item_table: Dict[str, SnailiadItemData] = {
    "Pea Shooter": SnailiadItemData(ItemClassification.progression, 1, 0, 0, "Weapon"),  # todo Progression or Not
    "Boomerang": SnailiadItemData(ItemClassification.progression, 1, 0, 1, "Weapon"),
    "Super Secret Boomerang": SnailiadItemData(ItemClassification.progression, 0, 0, 11, "Weapon"),
    "Rainbow Wave": SnailiadItemData(ItemClassification.progression, 1, 0, 2, "Weapon"),
    "Debug Rainbow Wave": SnailiadItemData(ItemClassification.progression, 0, 0, 12, "Weapon"),
    "Progressive Weapon": SnailiadItemData(ItemClassification.progression, 3, 0, 100000, "Weapon"),  # todo confirm with epsilon what IDs the progressibve items are
    "Rapid Fire": SnailiadItemData(ItemClassification.progression, 1, 0, 6, "Modifier"),
    "Backfire": SnailiadItemData(ItemClassification.progression, 1, 0, 6, "Modifier"),
    "Devastator": SnailiadItemData(ItemClassification.progression, 1, 0, 3, "Modifier"),
    "Progressive Modifier": SnailiadItemData(ItemClassification.progression, 2, 0, 200000, "Modifier"),
    "Ice Snail": SnailiadItemData(ItemClassification.progression, 1, 0, 7, "Shell"),
    "Gravity Shell": SnailiadItemData(ItemClassification.progression, 1, 0, 8, "Shell"),
    "Magnetic Foot": SnailiadItemData(ItemClassification.progression, 0, 0, 8, "Shell"),
    "Corkscrew Jump": SnailiadItemData(ItemClassification.progression, 0, 0, 8, "Shell"),
    "Angel Hop": SnailiadItemData(ItemClassification.progression, 1, 0, 8, "Shell"),
    "Full Metal Snail": SnailiadItemData(ItemClassification.progression, 1, 0, 9, "Shell"),
    "Progressive Shell": SnailiadItemData(ItemClassification.progression, 3, 0, 300000, "Shell"),
    "Gravity Shock": SnailiadItemData(ItemClassification.progression, 1, 0, 10, "Ability"),
    "High Jump": SnailiadItemData(ItemClassification.progression, 1, 0, 4, "Ability"),
    "Wall Grab": SnailiadItemData(ItemClassification.progression, 1, 0, 4, "Ability"),
    "Shell Shield": SnailiadItemData(ItemClassification.progression, 1, 0, 5, "Ability"),
    "Shellmet": SnailiadItemData(ItemClassification.progression, 1, 0, 5, "Ability"),
    "Helix Fragment": SnailiadItemData(ItemClassification.filler, 0, 0, 24, ""),
    "Nothing": SnailiadItemData(ItemClassification.filler, 0, 0, 400000, ""),
    "Heart Container": SnailiadItemData(ItemClassification.progression, 11, 0, 13, ""),
    "Gravity Lock": SnailiadItemData(ItemClassification.trap, 0, 0, 500000, "Trap"),
    "Weapon Lock": SnailiadItemData(ItemClassification.trap, 0, 0, 600000, "Trap"),
    "Lullaby Trap": SnailiadItemData(ItemClassification.trap, 0, 0, 700000, "Trap"),
    "Spider Trap": SnailiadItemData(ItemClassification.trap, 0, 0, 800000,  "Trap"),
}

slot_data_item_names = []

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
