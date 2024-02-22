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
    "Pea Shooter": SnailiadItemData(ItemClassification.progression, 0, 0, "Weapon"),  # todo Progression or Not
    "Boomerang": SnailiadItemData(ItemClassification.progression, 0, 0, "Weapon"),
    "Super Secret Boomerang": SnailiadItemData(ItemClassification.progression, 0, 0, "Weapon"),
    "Rainbow Wave": SnailiadItemData(ItemClassification.progression, 0, 0, "Weapon"),
    "Progressive Weapon": SnailiadItemData(ItemClassification.progression, 0, 0, "Weapon"),
    "Rapid Fire": SnailiadItemData(ItemClassification.progression, 0, 0, "Modifier"),
    "Devastator": SnailiadItemData(ItemClassification.progression, 0, 0, "Modifier"),
    "Progressive Modifier": SnailiadItemData(ItemClassification.progression, 0, 0, "Modifier"),
    "Ice Snail": SnailiadItemData(ItemClassification.progression, 0, 0, "Shell"),
    "Gravity Shell": SnailiadItemData(ItemClassification.progression, 0, 0, "Shell"),
    "Full Metal Snail": SnailiadItemData(ItemClassification.progression, 0, 0, "Shell"),
    "Progressive Shell": SnailiadItemData(ItemClassification.progression, 0, 0, "Shell"),
    "Gravity Shock": SnailiadItemData(ItemClassification.progression, 0, 0, "Ability"),
    "High Jump": SnailiadItemData(ItemClassification.progression, 0, 0, "Ability"),
    "Shell Shield": SnailiadItemData(ItemClassification.progression, 0, 0, "Ability"),
    "Helix Fragment": SnailiadItemData(ItemClassification.progression, 0, 0, ),
    "Heart Container": SnailiadItemData(ItemClassification.progression, 0, 0,),
    "Gravity Lock": SnailiadItemData(ItemClassification.trap, 0, 0, "Trap"),
    "Weapon Lock": SnailiadItemData(ItemClassification.trap, 0, 0, "Trap"),
    "Lullaby Trap": SnailiadItemData(ItemClassification.trap, 0, 0, "Trap"),


}