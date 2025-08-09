from typing import List, Dict, Any
from dataclasses import dataclass
from worlds.AutoWorld import PerGameCommonOptions
from Options import Choice, OptionGroup, Toggle, Range

def create_option_groups() -> List[OptionGroup]:
    option_group_list: List[OptionGroup] = []
    for name, options in pokemon_stadium_option_groups.items():
        option_group_list.append(OptionGroup(name=name, options=options))

    return option_group_list

class VictoryCondition(Choice):
    """
    Choose victory condition
    """
    display_name = "Victory Condition"
    option_defeat_rival = 1
    option_clear_master_ball_cup = 2
    default = 1

class GymCastleTrainerRandomness(Choice):
    """
    Controls the level of randomness for the enemy teams in Gym Leader Castle.
    Vanilla - No change
    Low - Stats are fairly even in distribution. Moveset has a status, STAB, and higher attack stat aligned move. (4th move is fully random)
    Medium - No extreme stat distributions. Moveset has a STAB, and higher attack stat aligned move. (3rd and 4th moves are fully random)
    High - All stat distributions possible. Moveset has a higher attack stat aligned move. (all other moves are fully random)
    """
    display_name = "Gym Castle Trainer Randomness"
    option_vanilla = 1
    option_low = 2
    option_medium = 3
    option_high = 4
    default = 1

@dataclass
class PokemonStadiumOptions(PerGameCommonOptions):
    VictoryCondition:   VictoryCondition
    ExtraLocations:     GymCastleTrainerRandomness

# This is where you organize your options
# Its entirely up to you how you want to organize it
pokemon_stadium_option_groups: Dict[str, List[Any]] = {
    "General Options": [VictoryCondition, GymCastleTrainerRandomness],
}
