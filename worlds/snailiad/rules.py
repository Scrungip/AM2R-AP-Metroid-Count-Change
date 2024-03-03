from random import Random
from typing import Dict, TYPE_CHECKING

from worlds.generic.Rules import set_rule, forbid_item
from BaseClasses import CollectionState
from .options import SnailiadOptions
if TYPE_CHECKING:
    from . import SnailiadWorld


def boss_1(options: SnailiadOptions, state: CollectionState, player: int) -> bool:
    if options.Open_Areas == 1:
        return True
    return state.has("Boss 1", player)


def boss_2(options: SnailiadOptions, state: CollectionState, player: int) -> bool:
    if options.Open_Areas == 1:
        return True
    return state.has("Boss 2", player)


def boss_3(options: SnailiadOptions, state: CollectionState, player: int) -> bool:
    if options.Open_Areas == 1:
        return True
    return state.has("Boss 3", player)


def boss_4(options: SnailiadOptions, state: CollectionState, player: int) -> bool:
    if options.Open_Areas == 1:
        return True
    return state.has("Boss 4", player)


def is_snaily(options: SnailiadOptions) -> bool:
    if options.Character_Select == 0:
        return True
    else:
        return False


def is_sluggy(options: SnailiadOptions) -> bool:
    if options.Character_Select == 1:
        return True
    else:
        return False


def is_upside(options: SnailiadOptions) -> bool:
    if options.Character_Select == 2:
        return True
    else:
        return False


def is_leggy(options: SnailiadOptions) -> bool:
    if options.Character_Select == 3:
        return True
    else:
        return False


def is_blobby(options: SnailiadOptions) -> bool:
    if options.Character_Select == 4:
        return True
    else:
        return False


def is_leechy(options: SnailiadOptions) -> bool:
    if options.Character_Select == 5:
        return True
    else:
        return False


def has_high_jump(state: CollectionState, player: int) -> bool:
    return state.has("High Jump", player) or state.has("Wall Grab", player) or can_fly(state, player)


def can_fly(state: CollectionState, player: int) -> bool:
    return has_gravity_shell(state, player)


def has_peashooter(state: CollectionState, player: int, options: SnailiadOptions) -> bool:
    if options.Start_With_Broom == 1:
        return True
    return state.has("Pea Shooter", player) or state.has("Progressive Weapon", player, 1) or has_boomerang(state, player)


def has_boomerang(state: CollectionState, player: int) -> bool:
    return state.has("Boomerang", player) or state.has("Progressive Weapon", player, 2) or has_rainbow_wave(state, player)


def has_rainbow_wave(state: CollectionState, player: int) -> bool:
    return state.has("Rainbow Wave", player) or state.has("Progressive Weapon", player, 3)


def has_weapon(state: CollectionState, player: int) -> bool:  # todo SnailiadWorld.options (Look at TUNIC #L92)
    return has_peashooter(state, player, SnailiadWorld.options) or has_boomerang(state, player) or has_rainbow_wave(state, player)


def has_devastator(state: CollectionState, player: int) -> bool:
    return state.has("Devastator", player) or state.has("Progressive Modifier", player, 2)


def has_ice_shell(state: CollectionState, player: int) -> bool:
    if SnailiadWorld.options.Difficulty_Select == 2:
        return True
    else:
        return state.has("Ice Snail", player) or state.has("Progressive Shell", player, 1)


def has_gravity_shell(state: CollectionState, player: int) -> bool:
    if SnailiadWorld.options.Difficulty_Select == 2:
        return state.has("Gravity Shell", player) or state.has("Progressive Shell", player, 1) or state.has("Magnetic Foot", player) or state.has("Corkscrew Jump", player) or state.has("Angel Hop", player)
    else:
        return state.has("Gravity Shell", player) or state.has("Progressive Shell", player, 2) or state.has("Magnetic Foot", player) or state.has("Corkscrew Jump", player) or state.has("Angel Hop", player)


def has_metal_shell(state: CollectionState, player: int) -> bool:
    if SnailiadWorld.options.Difficulty_Select == 2:
        return state.has("Full Metal Snail", player) or state.has("Progressive Shell", player, 2)
    else:
        return state.has("Full Metal Snail", player) or state.has("Progressive Shell", player, 3)


def can_gravity_shock(state: CollectionState, player: int) -> bool:
    return state.has("Gravity Shock", player) and has_gravity_shell(state, player)


def blue_door(state: CollectionState, player: int) -> bool:
    return has_weapon(state, player) or pink_door(state, player)


def pink_door(state: CollectionState, player: int) -> bool:
    return has_boomerang(state, player) or red_door(state, player)


def red_door(state: CollectionState, player: int) -> bool:
    return has_rainbow_wave(state, player) or green_door(state, player) or can_gravity_shock(state, player)


def green_door(state: CollectionState, player: int) -> bool:
    return (has_devastator(state, player) and has_weapon(state, player)) or (can_gravity_shock(state, player) and has_metal_shell(state, player))


def level_1_breakables(state: CollectionState, player: int) -> bool:
    return has_boomerang(state, player) or (has_weapon(state, player) and has_devastator(state, player))


def level_2_breakables(state: CollectionState, player: int) -> bool:
    return has_rainbow_wave(state, player) or (has_weapon(state, player) and has_devastator(state, player))


def level_3_breakables(state: CollectionState, player: int) -> bool:
    return (has_devastator(state, player) and has_weapon(state, player)) or (can_gravity_shock(state, player) and has_metal_shell(state, player))


def has_secret_knowledge(options: SnailiadOptions) -> bool:
    if options.Randomization_Type == SnailiadOptions.Randomization_Type.option_pro:
        return True
    return False


def create_region_rules(world: "SnailiadWorld") -> None:
    multiworld = world.multiworld
    player = world.player
    options = world.options

    multiworld.get_entrance("Snail Town -> Mare Carelia", player).can_reach = \
        lambda state: True

    multiworld.get_entrance("Snail Town -> Spiralis Silere", player).can_reach = \
        lambda state: level_2_breakables(state, player)

    multiworld.get_entrance("Snail Town -> Amastrida Abyssus", player).can_reach = \
        lambda state: red_door(state, player)

    multiworld.get_entrance("Snail Town -> Lux Lirata", player).can_reach = \
        lambda state: boss_3(options, state, player) and has_gravity_shell(state, player)

    multiworld.get_entrance("Snail Town -> Shrine of Iris", player).can_reach = \
        lambda state: level_1_breakables(state, player)

    multiworld.get_entrance("Mare Carelia -> Spiralis Silere", player).can_reach = \
        lambda state: level_1_breakables(state, player)

    multiworld.get_entrance("Spiralis Silere -> Amastrida Abyssus", player).can_reach = \
        lambda state: boss_2(options, state, player) and red_door(state, player)

    multiworld.get_entrance("Amastrida Abyssus -> Lux Lirata", player).can_reach = \
        lambda state: boss_3(options, state, player)


def create_location_rules(world: "SnailiadWorld") -> None:
    multiworld = world.multiworld
    player = world.player
    options = world.options

    set_rule(multiworld.get_location("Original Testing Room", player),
             lambda state: has_secret_knowledge(options) and level_2_breakables(state, player) and (has_high_jump(state, player) or is_upside(options) or is_leggy(options)))

    set_rule(multiworld.get_location("Leggy Snail\'s Tunnel", player),
             lambda state: level_1_breakables(state, player))

    set_rule(multiworld.get_location("Town Overtunnel", player),
             lambda state: level_1_breakables(state, player) or (has_high_jump(state, player) and has_secret_knowledge(options))
             or (has_secret_knowledge(options) and (is_sluggy(options) or is_upside(options) or is_leggy(options) or is_leechy(options))))

    set_rule(multiworld.get_location("Super Secret Alcove", player),
             lambda state: has_secret_knowledge(options) and (level_1_breakables(state, player) or has_high_jump(state, player)
             or is_sluggy(options) or is_upside(options) or is_leggy(options) or is_leechy(options)))

    set_rule(multiworld.get_location("Love Snail\'s Alcove", player),
             lambda state: level_1_breakables(state, player) or has_high_jump(state, player) or is_sluggy(options)
             or is_upside(options) or is_leggy(options) or is_leechy(options))

    set_rule(multiworld.get_location("Suspicious Tree", player),
             lambda state: level_2_breakables(state, player))

    set_rule(multiworld.get_location("Anger Management Room", player),
             lambda state: level_2_breakables(state, player))

    set_rule(multiworld.get_location("Percentage Snail\'s Hidey Hole", player),
             lambda state: level_2_breakables(state, player))

    set_rule(multiworld.get_location("Digging Grounds", player),
             lambda state: True)

    set_rule(multiworld.get_location("Cave Snail\'s Cave", player),
             lambda state: True)

    set_rule(multiworld.get_location("Fragment Cave", player),
             lambda state: level_2_breakables(state, player))

    set_rule(multiworld.get_location("Discombobulatory Alcove", player),
             lambda state: True)

    set_rule(multiworld.get_location("Seabed Caves", player),
             lambda state: True)

    set_rule(multiworld.get_location("Fine Dining (Peashooter)", player),
             lambda state: True)

    set_rule(multiworld.get_location("Fine Dining (Fragment)", player),
             lambda state: level_2_breakables(state, player))

    set_rule(multiworld.get_location("The Maze Room", player),
             lambda state: level_1_breakables(state, player))

    set_rule(multiworld.get_location("Monument of Greatness", player),
             lambda state: level_1_breakables(state, player))

    set_rule(multiworld.get_location("Heart of the Sea", player),
             lambda state: red_door(state, player))

    set_rule(multiworld.get_location("Daily Helping of Calcium", player),
             lambda state: pink_door(state, player) or has_secret_knowledge(options))

    set_rule(multiworld.get_location("Dig, Snaily, Dig", player),
             lambda state: green_door(state, player))

    set_rule(multiworld.get_location("Skywatcher\'s Loot", player),
             lambda state: level_1_breakables(state, player))

    set_rule(multiworld.get_location("Signature Croissants (Boomerang)", player),
             lambda state: boss_1(options, state, player))

    set_rule(multiworld.get_location("Signature Croissants (Heart)", player),
             lambda state: boss_1(options, state, player) and level_1_breakables(state, player))

    set_rule(multiworld.get_location("Squared Snelks", player),
             lambda state: has_secret_knowledge(options) and (can_fly(state, player) or is_upside(options) or is_leggy(options)))

    set_rule(multiworld.get_location("Frost Shrine", player),
             lambda state: level_2_breakables(state, player))

    set_rule(multiworld.get_location("Sweater Required", player),
             lambda state: level_1_breakables(state, player) and has_ice_shell(state, player))

    set_rule(multiworld.get_location("A Secret to Snowbody", player),
             lambda state: pink_door(state, player))

    set_rule(multiworld.get_location("Devil\'s Alcove", player),
             lambda state: green_door(state, player))

    set_rule(multiworld.get_location("Ice Climb", player),
             lambda state: has_secret_knowledge(options) or (has_high_jump(state, player) or can_fly(state, player)
             or has_ice_shell(state, player) or is_upside(options) or is_leggy(options)))

    set_rule(multiworld.get_location("The Labyrinth (Fragment)", player),
             lambda state: level_2_breakables(state, player))

    set_rule(multiworld.get_location("The Labyrinth (High Jump)", player),
             lambda state: level_2_breakables(state, player) or has_secret_knowledge(options))

    set_rule(multiworld.get_location("Sneaky, Sneaky", player),
             lambda state: red_door(state, player))

    set_rule(multiworld.get_location("Prismatic Prize (Heart)", player),
             lambda state: red_door(state, player))

    set_rule(multiworld.get_location("Prismatic Prize (Rainbow Wave)", player),
             lambda state: boss_2(options, state, player) or red_door(state, player))

    set_rule(multiworld.get_location("Hall of Fire", player),  # todo how much health?
             lambda state: (has_metal_shell(state, player) or state.has("Heart Container", player))
             and (pink_door(state, player) or red_door(state, player)))

    set_rule(multiworld.get_location("Scorching Snelks", player),
             lambda state: has_secret_knowledge(options) and has_metal_shell(state, player) and (can_fly(state, player)
             or level_3_breakables(state, player) or red_door(state, player)))

    set_rule(multiworld.get_location("Hidden Hideout", player),
             lambda state: has_secret_knowledge(options) and (can_fly(state, player) or level_3_breakables(state, player)))

    set_rule(multiworld.get_location("Green Cache", player),
             lambda state: red_door(state, player) or level_3_breakables(state, player))

    set_rule(multiworld.get_location("Furnace", player),
             lambda state: level_2_breakables(state, player))

    set_rule(multiworld.get_location("Slitherine Grove", player),
             lambda state: red_door(state, player))

    set_rule(multiworld.get_location("Floaty Fortress (Top Left)", player),
             lambda state: pink_door(state, player) and (can_fly(state, player) or is_upside(options) or is_leggy(options)))

    set_rule(multiworld.get_location("Floaty Fortress (Bottom Right)", player),
             lambda state: pink_door(state, player) and (can_fly(state, player) or is_upside(options) or is_leggy(options)))

    set_rule(multiworld.get_location("Woah Mama", player),
                lambda state: level_2_breakables(state, player))

    set_rule(multiworld.get_location("Shocked Shell", player),
             lambda state: level_2_breakables(state, player) and (has_high_jump(state, player) or is_sluggy(options)
             or is_upside(options) or is_leggy(options) or is_leechy(options)))

    set_rule(multiworld.get_location("Gravity Shrine", player),
             lambda state: level_2_breakables(state, player))

    set_rule(multiworld.get_location("Fast Food", player),
             lambda state: can_fly(state, player) or (has_secret_knowledge(options) and red_door(state, player)))

    set_rule(multiworld.get_location("The Bridge", player),
             lambda state: boss_3(options, state, player) or (red_door(state, player) and (has_high_jump(state, player)
             or is_sluggy(options) or is_upside(options) or is_leggy(options) or is_leechy(options))))

    set_rule(multiworld.get_location("Transit 90", player),
             lambda state: level_3_breakables(state, player))

    set_rule(multiworld.get_location("Steel Shrine", player),  # todo how much health?
             lambda state: red_door(state, player) and (has_metal_shell(state, player) or state.has("Heart Container", player)))

    set_rule(multiworld.get_location("Space Balcony (Heart)", player),
             lambda state: level_3_breakables(state, player) and (has_metal_shell(state, player) or state.has("Heart Container", player)))

    set_rule(multiworld.get_location("Space Balcony (Fragment)", player),
             lambda state: level_3_breakables(state, player) and (has_metal_shell(state, player) or state.has("Heart Container", player)))

    set_rule(multiworld.get_location("The Vault", player),
             lambda state: red_door(state, player) and (has_metal_shell(state, player) or state.has("Heart Container", player)))

    set_rule(multiworld.get_location("Holy Hideaway", player),
             lambda state: red_door(state, player) and (has_metal_shell(state, player) or state.has("Heart Container", player))
             and (can_fly(state, player) or is_upside(options) or is_leggy(options) or is_blobby(options)))

    set_rule(multiworld.get_location("Arctic Alcove", player),
             lambda state: red_door(state, player) and (has_metal_shell(state, player) or state.has("Heart Container", player))
             and (can_fly(state, player) or is_upside(options) or is_leggy(options) or is_blobby(options)))

    set_rule(multiworld.get_location("Lost Loot", player),
             lambda state: has_secret_knowledge(options) and red_door(state, player) and (has_metal_shell(state, player) or state.has("Heart Container", player))
             and (can_fly(state, player) or is_upside(options) or is_leggy(options) or is_blobby(options)))

    set_rule(multiworld.get_location("Reinforcements", player),
             lambda state: red_door(state, player) and (has_metal_shell(state, player) or state.has("Heart Container", player))
             and (can_fly(state, player) or is_upside(options) or is_leggy(options) or is_blobby(options)))

    set_rule(multiworld.get_location("Glitched Goodies", player),
             lambda state: pink_door(state, player))
