from enum import IntEnum
from typing import NamedTuple, Optional
from BaseClasses import Location, Item, ItemClassification

class PokemonStadiumLocation(Location):
    game = 'PokemonStadium'

class PokemonStadiumItem(Item):
    game = 'PokemonStadium'

class ItemData(NamedTuple):
    ap_code: Optional[int]
    classification: ItemClassification
    count: Optional[int] = 1

class LocData(NamedTuple):
    ap_code: Optional[int]
    region: Optional[str]
