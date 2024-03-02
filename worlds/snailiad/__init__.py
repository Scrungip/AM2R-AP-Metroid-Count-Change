from typing import Dict, List, Any

from BaseClasses import Region, Location, Item, Tutorial, ItemClassification
from .items import item_name_to_id, item_table, filler_items, item_name_group
from .locations import location_table, location_name_group, location_name_to_id
from .rules import create_region_rules, create_location_rules
from .regions import snailiad_regions
from .options import SnailiadOptions
from worlds.AutoWorld import WebWorld, World
from decimal import Decimal, ROUND_HALF_UP


class SnailiadWeb(WebWorld):
    tutorials = [
        Tutorial(
            tutorial_name= "Multiworld Setup Guide",
            description= "A Guide to setting up a Snailiad+ Multiworld",
            language="English",
            file_name="setup_en.md",
            link="setup/en",
            authors=["Ehseezed, EpsilonTheDerg"]
        )
    ]
    theme = "ice"
    game = "Snailiad"


class SnaliadItem(Item):
    game: str = "Snailiad"


class SnailiadLocation(Location):
    game: str = "Snailiad"


class SnailiadWorld(World):
    """
    Snail™
    """  # todo Description
    game = "Snailiad"
    web = SnailiadWeb()

    data_version = 0
    options: SnailiadOptions
    item_name_groups = item_name_group
    location_name_groups = location_name_group

    item_name_to_id = item_name_to_id
    location_name_to_id = location_name_to_id

    def generate_early(self) -> None:
        if hasattr(self.multiworld, "re_gen_passthrough"):
            if "Snailiad" in self.multiworld.re_gen_passthrough:
                passthrough = self.multiworld.re_gen_passthrough["Snailiad"]
                self.options.Progressive_Items.value = passthrough["Progressive_Items"]
                self.options.Randomization_Type.value = passthrough["Randomization_Type"]

    def create_item(self, name: str) -> SnaliadItem:
        item_data = item_table[name]
        return SnaliadItem(name, item_data.classification, self.item_name_to_id[name], self.player)

    def create_items(self) -> None:
        character = self.options.Character_Select
        progressive = self.options.Progressive_Items
        helix_locks = self.options.Helix_Locks
        difficulty = self.options.Difficulty_Select
        nothings = 2  # SSB and DRW will never be generated

        snaliad_items: List[SnaliadItem] = []

        items_to_create: Dict[str, int] = {item: data.quantity_in_item_pool for item, data in item_table.items()}

        if progressive:
            items_to_create["Pea Shooter"] = 0
            items_to_create["Boomerang"] = 0
            items_to_create["Rainbow Wave"] = 0
            items_to_create["Rapid Fire"] = 0
            items_to_create["Devastator"] = 0
            items_to_create["Ice Snail"] = 0
            items_to_create["Gravity Shell"] = 0
            items_to_create["Magnetic Foot"] = 0
            items_to_create["Corkscrew Jump"] = 0
            items_to_create["Angel Hop"] = 0
            items_to_create["Full Metal Snail"] = 0
            items_to_create["Progressive Weapon"] = 3
            items_to_create["Progressive Modifier"] = 2
            if difficulty == difficulty.option_insane:
                items_to_create["Progressive Shell"] = 2
                nothings += 1
            else:
                items_to_create["Progressive Shell"] = 3
            nothings += 2

        if difficulty == difficulty.option_insane:
            items_to_create["Ice Snail"] = 0
            nothings += 1

        if character == character.option_sluggy:
            items_to_create["Shell Shield"] = 0
            nothings += 1

        if character == character.option_upside:
            items_to_create["Gravity Shell"] = 0
            items_to_create["Magnetic Foot"] = 1

        if character == character.option_leggy:
            items_to_create["Gravity Shell"] = 0
            items_to_create["Corkscrew Jump"] = 1

        if character == character.option_blobby:
            items_to_create["Gravity Shell"] = 0
            items_to_create["Angel Hop"] = 1
            items_to_create["Wall Grab"] = 1

        if character == character.option_leechy:
            items_to_create["Shell Shield"] = 0
            nothings += 1

        if helix_locks:
            pieces = 0
            fragments = SnaliadItem("Helix Fragment", ItemClassification.progression, self.item_name_to_id["Helix Fragment"], self.player)
            while pieces < 20:
                snaliad_items.append(fragments)
                pieces += 1

            items_to_create["Helix Fragment"] = 10
