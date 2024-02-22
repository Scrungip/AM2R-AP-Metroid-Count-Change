from dataclasses import dataclass

from Options import DefaultOnToggle, Toggle, StartInventoryPool, Choice, Range, PerGameCommonOptions


class RandomizationType(Choice):
    """Changes the type of randomization between a Major Minor split
    a full item randomizer and one that accounts for knowledge."""
    display_name = "Randomization Type"
    option_split = 0
    option_full = 1
    option_pro = 2
    default = 1


class ProgressiveItems(DefaultOnToggle):
    """an on/off switch that toggles the stacking of various items.
    There are three progressive items: Weapon (pea > boom > wave),
    Weapon Mod (rapid > devastator), and Shell (ice > grav > metal)"""
    display_name = "Progressive Items"


class StartWithBroom(Toggle):
    """toggles the option to start the character with a Broom weapon
    in slot zero. The Broom acts like a melee version of the Peashooter,
    able to dispatch enemies, open blue doors, and get upgraded by
    Rapid Fire and Devastator, but is held back by its rate of fire and range"""
    display_name = "Start with Broom"


class AreaShuffle(Toggle):
    """Enables the Area Randomizer"""
    display_name = "Area Shuffle"


class HelixLocks(Toggle):
    """lets you lock boss doors until you have a certain
    number of helix fragments under your belt.  You need
    5 for boss 1, 10 for boss 2, 15 for boss 3, and 25 for boss 4"""
    display_name = "Helix Locks"


class MusicShuffle(Choice):
    """Enables the Music Randomizer"""
    display_name = "Music Shuffle"
    option_off = 0
    option_area = 1
    option_full = 2
    default = 0


class SnailsHaveHints(Toggle):
    """Enables the Snail Randomizer"""
    display_name = "Snails Have Hints"


class TrapFill(Range):
    """Number of traps to be placed in the world"""
    display_name = "Trap Fill"
    range_start = 0
    range_end = 25
    default = 0


@dataclass
class SnailiadOptions(PerGameCommonOptions):
    RandomizationType: RandomizationType
    ProgressiveItems: ProgressiveItems
    StartWithBroom: StartWithBroom
    AreaShuffle: AreaShuffle
    HelixLocks: HelixLocks
    MusicShuffle: MusicShuffle
    SnailsHaveHints: SnailsHaveHints
    start_inventory_from_pool: StartInventoryPool
