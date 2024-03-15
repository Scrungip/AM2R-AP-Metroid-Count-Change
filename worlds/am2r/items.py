import itertools
from collections import Counter
from typing import Dict, List, NamedTuple, Set

from BaseClasses import Item, ItemClassification, MultiWorld
from .options import MetroidsAreChecks, MetroidsRequired, get_option_value, TrapFillPercentage, RemoveFloodTrap, RemoveTossTrap, RemoveShortBeam, RemoveEMPTrap, RemoveOHKOTrap, RemoveTouhouTrap


class ItemData(NamedTuple):
    code: int
    group: str
    classification: ItemClassification = ItemClassification.progression
    game_id: int = 0
    required_num: int = 0
    

class AM2RItem(Item):
    game: str = "AM2R"


def create_item(player: int, name: str) -> Item:
    item_data = item_table[name]
    return AM2RItem(name, item_data.classification, item_data.code, player)


def create_fixed_item_pool() -> List[str]:
    required_items: Dict[str, int] = {name: data.required_num for name, data in item_table.items()}
    return list(Counter(required_items).elements())


def create_metroid_items(MetroidsRequired: MetroidsRequired, MetroidsAreChecks: MetroidsAreChecks) -> List[str]:
    metroid_count = 0
    if MetroidsAreChecks == MetroidsAreChecks.option_include_A6:
        metroid_count = MetroidsRequired.value
    elif MetroidsAreChecks == MetroidsAreChecks.option_exclude_A6:
        metroid_count += MetroidsRequired.value - 5
    return ["Metroid" for _ in range(metroid_count)]


def create_trap_items(multiworld: MultiWorld, player: int, locations_to_trap: int) -> List[str]:
    trap_pool = trap_weights.copy()

    if multiworld.RemoveFloodTrap[player].value == 1:
        del trap_pool["Flood Trap"]

    if multiworld.RemoveTossTrap[player].value == 1:
        del trap_pool["Big Toss Trap"]

    if multiworld.RemoveShortBeam[player].value == 1:
        del trap_pool["Short Beam"]

    if multiworld.RemoveEMPTrap[player].value == 1:
        del trap_pool["EMP Trap"]
    
    if multiworld.RemoveTouhouTrap[player].value == 1:
        del trap_pool["Touhou Trap"]

    if multiworld.RemoveOHKOTrap[player].value == 1:
        del trap_pool["OHKO Trap"]

    return multiworld.random.choices(
        population=list(trap_pool.keys()),
        weights=list(trap_pool.values()),
        k=locations_to_trap
    )


def create_random_items(multiworld: MultiWorld, player: int, random_count: int) -> List[str]:
    filler_pool = filler_weights.copy()

    return multiworld.random.choices(
        population=list(filler_pool.keys()),
        weights=list(filler_pool.values()),
        k=random_count
    )


def create_all_items(multiworld: MultiWorld, player: int) -> None:
    sum_locations = len(multiworld.get_unfilled_locations(player))

    itempool = (
        create_fixed_item_pool()
        + create_metroid_items(multiworld.MetroidsRequired[player], multiworld.MetroidsAreChecks[player])
    )

    trap_percentage = get_option_value(multiworld, player, "TrapFillPercentage")
    trap_fill = trap_percentage / 100

    random_count = sum_locations - len(itempool)
    locations_to_trap = int(trap_fill * random_count)
    itempool += create_trap_items(multiworld, player, locations_to_trap)

    random_count = sum_locations - len(itempool)
    itempool += create_random_items(multiworld, player, random_count)

    multiworld.itempool += [create_item(player, name) for name in itempool]


item_table: Dict[str, ItemData] = {
    "Missile":                  ItemData(8678000, "Ammo", ItemClassification.filler, 15),
    "Super Missile":            ItemData(8678001, "Ammo", ItemClassification.progression, 16, 1),
    "Power Bomb":               ItemData(8678002, "Ammo", ItemClassification.progression, 18, 2),
    "Energy Tank":              ItemData(8678003, "Ammo", ItemClassification.filler, 17, 1),
    #  "Arm Cannon":            ItemData8678004, ("Equipment", ItemClassification.progression, ID, 1),
    #  "Morph Ball":            ItemData8678005, ("Equipment", ItemClassification.progression, ID, 1),
    #  "Power Grip":            ItemData8678006, ("Equipment", ItemClassification.progression, ID, 1),
    "Bombs":                    ItemData(8678007, "Equipment", ItemClassification.progression, 0, 1),
    "Spider Ball":              ItemData(8678008, "Equipment", ItemClassification.progression, 2, 1),
    "Hi Jump":                  ItemData(8678009, "Equipment", ItemClassification.progression, 4, 1),
    "Spring Ball":              ItemData(8678010, "Equipment", ItemClassification.progression, 3, 1),
    "Space Jump":               ItemData(8678011, "Equipment", ItemClassification.progression, 6, 1),
    "Speed Booster":            ItemData(8678012, "Equipment", ItemClassification.progression, 7, 1),
    "Screw Attack":             ItemData(8678013, "Equipment", ItemClassification.progression, 8, 1),
    "Varia Suit":               ItemData(8678014, "Equipment", ItemClassification.useful, 5, 1),
    "Gravity Suit":             ItemData(8678015, "Equipment", ItemClassification.progression, 9, 1),
    "Charge Beam":              ItemData(8678016, "Beam", ItemClassification.progression, 10, 1),
    "Wave Beam":                ItemData(8678017, "Beam", ItemClassification.useful, 12, 1),
    "Spazer":                   ItemData(8678018, "Beam", ItemClassification.useful, 13, 1),
    "Plasma Beam":              ItemData(8678019, "Beam", ItemClassification.useful, 14, 1),
    "Ice Beam":                 ItemData(8678020, "Beam", ItemClassification.progression, 11, 1),
    "Flood Trap":               ItemData(8678021, "Trap", ItemClassification.trap, 21),
    "Big Toss Trap":            ItemData(8678022, "Trap", ItemClassification.trap, 22),
    "Short Beam":               ItemData(8678023, "Trap", ItemClassification.trap, 23),
    "EMP Trap":                 ItemData(8678024, "Trap", ItemClassification.trap, 24),
    "OHKO Trap":                ItemData(8678026, "Trap", ItemClassification.trap, 25),
    "Touhou Trap":              ItemData(8678027, "Trap", ItemClassification.trap, 26),
    "Metroid":                  ItemData(8678025, "MacGuffin", ItemClassification.progression_skip_balancing, 19),
    "The Galaxy is at Peace":   ItemData(None, "Victory", ItemClassification.progression)

}
filler_weights: Dict[str, int] = {
    "Missile":          44,
    "Super Missile":    9,
    "Power Bomb":       8,
    "Energy Tank":      9
}

trap_weights: Dict[str, int] = {
    "Flood Trap":           1,
    "Big Toss Trap":        1,
    "Short Beam":           1,
    "EMP Trap":             1,
    "Touhou Trap":          1,
    "OHKO Trap":            1
}


def get_item_group(item_name: str) -> str:
    return item_table[item_name].group


def item_is_filler(item_name: str) -> bool:
    return item_table[item_name].classification == ItemClassification.filler


def item_is_trap(item_name: str) -> bool:
    return item_table[item_name].classification == ItemClassification.trap


trap_items: List[str] = list(filter(item_is_trap, item_table.keys()))
filler_items: List[str] = list(filter(item_is_filler, item_table.keys()))

item_name_to_id: Dict[str, int] = {name: data.code for name, data in item_table.items()}


item_name_groups: Dict[str, Set[str]] = {
    group: set(item_names) for group, item_names in itertools.groupby(item_table, get_item_group)
}
