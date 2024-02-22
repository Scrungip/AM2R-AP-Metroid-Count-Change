from random import Random
from typing import Dict, TYPE_CHECKING

from worlds.generic.Rules import set_rule, forbid_item
from BaseClasses import CollectionState
from .options import SnailiadOptions
if TYPE_CHECKING:
    from . import SnailiadWorld


def has_peashooter(state: CollectionState, player: int, options: SnailiadOptions) -> bool:
    if options.StartWithBroom:
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
    return state.has("Ice Snail", player) or state.has("Progressive Shell", player, 1)


def has_gravity_shell(state: CollectionState, player: int) -> bool:
    return state.has("Gravity Shell", player) or state.has("Progressive Shell", player, 2)


def has_metal_shell(state: CollectionState, player: int) -> bool:
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
    if options.RandomizationType == SnailiadOptions.RandomizationType.option_pro:
        return True
    return False
