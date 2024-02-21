from random import Random
from typing import Dict, TYPE_CHECKING

from worlds.generic.Rules import set_rule, forbid_item
from BaseClasses import CollectionState


def blue_door(state: CollectionState, player: int) -> bool:
    return state.has("", player)


def pink_door(state: CollectionState, player: int) -> bool:
    return state.has("", player)


def red_door(state: CollectionState, player: int) -> bool:
    return state.has("", player)


