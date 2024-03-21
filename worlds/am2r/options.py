from dataclasses import dataclass

from Options import DefaultOnToggle, Toggle, StartInventoryPool, Choice, Range, PerGameCommonOptions


class LogicDificulty(Choice):
    """Easy: Assumes developer intended solutions and expects little to none trick knowledge and less than optimal use of ammos
    Required Tricks: Simple single wall Wall-Jumps, Knowledge of the Low% Super Missile block in Distribution Center
    Required Damage: Hydro Station Nest Vines with 2 E-Tanks
    Normal: Assumes knowledge over the game and expects some trick knowledge
    Required Tricks: Simple Morph Glides, tricky single wall Wall-Jumps, Knowledge of Shinesparks to reach areas
    Required Damage: Hydro Nest Vines (1E), Doom Treadmill Spikes, Spikes to Patricia(A4 Right Side Zeta)"""
    display_name = "Logic Dificulty"
    default = 0
    option_easy = 0
    option_normal = 1
    option_hard = 2  # todo add hard mode definitions


class AmmoLogic(Choice):
    """Normal: Assumes you get 5 missiles and 2 Super Missiles/Power Bombs per pack
    Fusion: Assumes you get 2 missiles and 1 Super Missile/Power Bomb per pack
    picking normal and then playing on fusion or hard difficulty could make the game impossible"""
    display_name = "Ammo Logic"
    default = 0
    option_normal = 0
    option_fusion = 1


class MetroidsRequired(Range):
    """Chose how many Metroids need to be killed or obtained to go through to the omega nest"""
    display_name = "Metroids Required for Omega Nest"
    range_start = 0
    range_end = 46
    default = 46


class MetroidsAreChecks(Choice):  # I kinda want to explode this option and have it always be on
    """Have each of the 46 non lab Metroids be treated as locations"""
    display_name = "Metroids are Checks"
    default = 2
    option_disabled = 0
    option_exclude_A6 = 1
    option_include_A6 = 2


class StartLocation(Toggle):
    """Randomize Starting Location"""
    display_name = "Randomize Start Location"


class AreaRando(Choice):
    """Activates Area Randomization and or Boss Randomization, also activates rolling saves as softlock prevention
    Area Randomizer will shuffle various Areas arround in order to create a new expierence
    Boss Randomization randomizes Arachnus, Torizo Ascended, and Genesis with each other also then randomizes
    Temple Guardian, Tester and Serris
    Both activates Both independently on their own"""
    display_name = "Area Randomizer"
    default = 0
    option_disabled = 0
    option_boss_rando = 1
    option_area_rando = 2


class RemovePowerGrip(Toggle):
    """Adds Power Grip to the item pool and removes it from the start inventory"""
    display_name = "Remove Power Grip"


class RemoveMorphBall(Toggle):
    """Adds Morph Ball to the item pool and removes it from the start inventory"""
    display_name = "Remove Morph Ball"


class RemoveBeam(Toggle):
    """Removes your Arm Cannon and makes it a findable item"""
    display_name = "Remove Beam"


class MissileLauncher(Choice):
    """Removes the 30 Starting Missiles or add a missile launcher to the item pool"""
    display_name = "Remove Missiles"
    default = 0
    option_vanilla = 0
    option_remove = 1
    option_launcher = 2


class SuperLauncher(Toggle):
    """Super Missile Launcher"""
    display_name = "Super Missile Launcher"


class PowerLauncher(Toggle):
    """Power Bomb Launcher"""
    display_name = "Power Bomb Launcher"


class TrapFillPercentage(Range):
    """Adds in slightly inconvenient traps into the item pool"""
    display_name = "Trap Fill Percentage"
    range_start = 0
    range_end = 100
    default = 0


class RemoveFloodTrap(Toggle):
    """Removes Flood Traps from trap fill"""
    display_name = "Remove Flood Trap"


class RemoveTossTrap(Toggle):
    """There is a pipebomb in your mailbox"""
    display_name = "Remove Toss Trap"


class RemoveShortBeam(Toggle):
    """Remove muscle memory trap"""
    display_name = "Remove Short Beam"


class RemoveEMPTrap(Toggle):
    """Yes we know that it looks weird during the idle animation, but it's a vanilla bug"""
    display_name = "Remove EMP Trap"


class RemoveTouhouTrap(Toggle):
    """Removes Touhou Traps from trap fill"""
    display_name = "Remove Touhou Trap"


class RemoveOHKOTrap(Toggle):
    """Removes OHKO Traps from trap fill"""
    display_name = "Remove OHKO Trap"


@dataclass
class AM2ROptions(PerGameCommonOptions):
    logic_dificulty: LogicDificulty
    ammo_logic: AmmoLogic
    metroids_required: MetroidsRequired
    metroids_are_checks: MetroidsAreChecks
    start_location: StartLocation
    area_rando: AreaRando
    remove_power_grip: RemovePowerGrip
    remove_morph_ball: RemoveMorphBall
    remove_beam: RemoveBeam
    missile_launcher: MissileLauncher
    super_launcer: SuperLauncher
    power_launcer: PowerLauncher
    trap_fill_percentage: TrapFillPercentage
    remove_flood_trap: RemoveFloodTrap
    remove_toss_trap: RemoveTossTrap
    remove_short_beam: RemoveShortBeam
    remove_EMP_trap: RemoveEMPTrap
    remove_touhou_trap: RemoveTouhouTrap
    remove_OHKO_trap: RemoveOHKOTrap
    start_inventory_pool: StartInventoryPool
