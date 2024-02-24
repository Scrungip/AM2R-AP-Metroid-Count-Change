from typing import Dict, Set, NamedTuple
from itertools import groupby


class SnailiadLocationData(NamedTuple):
    region: str
    location_group: str = "region"


location_based_id = 1000000000000  # todo actual base ID

location_table: Dict[str, SnailiadLocationData] = {
    "Original Testing Room": SnailiadLocationData(""), # lev2 && (jump || p3 || p4)
    "Snail Town - Love Snail\'s Tunnel": SnailiadLocationData(""),
}


location_name_to_id: Dict[str, int] = {name: location_based_id + index for index, name in enumerate(location_table)}


def get_location_group(location_name: str) -> str:
    loc_group = location_table[location_name].location_group
    if loc_group == "region":
        loc_group = location_table[location_name].region.lower()
    return loc_group


location_name_group: Dict[str, Set[str]] = {
    group: set(location_names) for group, location_names in groupby(sorted(location_table, key=get_location_group), get_location_group) if group != ""
}
