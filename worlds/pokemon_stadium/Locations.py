from typing import Dict, TYPE_CHECKING
import logging

from .Types import LocData

if TYPE_CHECKING:
    from . import PokemonStadiumWorld

def get_total_locations(world: 'PokemonStadiumWorld') -> int:
    return len(location_table)

def get_location_names() -> Dict[str, int]:
    names = {name: data.ap_code for name, data in location_table.items()}

    return names

def is_valid_location(world: 'PokemonStadiumWorld', name) -> bool:
    return True

pokemon_stadium_locations = {
    'Pewter Gym':       LocData(20000001, 'Gym Leader Castle'),
    'Cerulean Gym':     LocData(20000002, 'Gym Leader Castle'),
    'Vermillion Gym':   LocData(20000003, 'Gym Leader Castle'),
    'Celadon Gym':      LocData(20000004, 'Gym Leader Castle'),
    'Fuchsia Gym':      LocData(20000005, 'Gym Leader Castle'),
    'Saffron Gym':      LocData(20000006, 'Gym Leader Castle'),
    'Cinnabar Gym':     LocData(20000007, 'Gym Leader Castle'),
    'Viridian Gym':     LocData(20000008, 'Gym Leader Castle'),
}

event_locations = {
    'Beat Rival': LocData(20000000, 'Hall of Fame')
}

location_table = {
    **pokemon_stadium_locations,
    **event_locations
}