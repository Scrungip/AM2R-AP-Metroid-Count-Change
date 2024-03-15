import itertools
from typing import Union
from BaseClasses import MultiWorld, CollectionState
from .options import MetroidsRequired, MetroidsAreChecks, get_option_value


class AM2RLogic:
    player: int

    def __init__(self, world: MultiWorld, player: int):
        self.player = player

    def AM2R_can_bomb(self, state: CollectionState) -> bool:
        return state.has('Bombs', self.player) or state.has('Power Bomb', self.player, 2)

    def AM2R_can_jump(self, state: CollectionState) -> bool:
        return state.has_any({'Hi Jump', 'Space Jump', 'Bombs'}, self.player)

    def AM2R_can_fly(self, state: CollectionState) -> bool:
        return state.has_any({'Bombs', 'Space Jump'}, self.player)

    def AM2R_can_spider(self, state: CollectionState) -> bool:
        return state.has('Spiderball', self.player) \
            or self.AM2R_can_fly(state)

    def AM2R_can_schmove(self, state: CollectionState) -> bool:
        return self.AM2R_can_spider(state) \
            or state.has('Hi Jump', self.player)

    def AM2R_has_ballspark(self, state: CollectionState) -> bool:
        return state.has_all({'Speed Booster', 'Spring Ball'}, self.player)

    def AM2R_can_down(self, state: CollectionState) -> bool:
        amount = get_option_value(MultiWorld, self.player, "MetroidsRequired")
        check_state = get_option_value(MultiWorld, self.player, "MetroidsAreChecks")

        if check_state >= 1:
            return state.has("Metroid", self.player, amount) \
                and state.has("Ice Beam", self.player) and self.AM2R_can_spider(state) and self.AM2R_can_bomb(state) \
                and (state.has("Screw Attack", self.player) or state.has("Power Bomb", self.player))
        else:
            return state.has_all({"Speed Booster", "Ice Beam", "Super Missile"}, self.player) \
                and self.AM2R_can_fly(state) and self.AM2R_can_bomb(state) and (state.has("Screw Attack", self.player) or state.has("Power Bomb", self.player))

    def AM2R_can_lab(self, state: CollectionState) -> bool:
        amount = get_option_value(MultiWorld, self.player, "MetroidsRequired")
        check_state = get_option_value(MultiWorld, self.player, "MetroidsAreChecks")

        if check_state == 2:
            amount += 5
            return state.has("Metroid", self.player, amount) \
                and state.has("Ice Beam", self.player) and self.AM2R_can_spider(state) and self.AM2R_can_bomb(state) \
                and (state.has("Screw Attack", self.player) or state.has("Power Bomb", self.player))
        elif check_state == 1:
            return state.has("Metroid", self.player, amount) \
                and state.has("Ice Beam", self.player) and self.AM2R_can_spider(state) and self.AM2R_can_bomb(state) \
                and (state.has("Screw Attack", self.player) or state.has("Power Bomb", self.player))
        else:
            return state.has_all({"Speed Booster", "Ice Beam", "Super Missile"}, self.player) \
                and self.AM2R_can_fly(state) and self.AM2R_can_bomb(state) and (state.has("Screw Attack", self.player) or state.has("Power Bomb", self.player))
