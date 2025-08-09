from BaseClasses import Region
from .Types import PokemonStadiumLocation
from .Locations import location_table, is_valid_location
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import PokemonStadiumWorld

def create_regions(world: "PokemonStadiumWorld"):
    overworld = create_region(world, "Overworld")
    gym_leader_castle = create_region_and_connect(world, "Gym Leader Castle", "Overworld -> Gym Leader Castle", overworld)

    # ---------------------------------- Gym Leader Castle ----------------------------------
    create_region_and_connect(world, "Pewter Gym", "Gym Leader Castle -> Pewter Gym", gym_leader_castle)
    create_region_and_connect(world, "Cerulean Gym", "Gym Leader Castle -> Cerulean Gym", gym_leader_castle)
    create_region_and_connect(world, "Vermillion Gym", "Gym Leader Castle -> Vermillion Gym", gym_leader_castle)
    create_region_and_connect(world, "Celadon Gym", "Gym Leader Castle -> Celadon Gym", gym_leader_castle)
    create_region_and_connect(world, "Fuchsia Gym", "Gym Leader Castle -> Fuchsia Gym", gym_leader_castle)
    create_region_and_connect(world, "Saffron Gym", "Gym Leader Castle -> Saffron Gym", gym_leader_castle)
    create_region_and_connect(world, "Cinnabar Gym", "Gym Leader Castle -> Cinnabar Gym", gym_leader_castle)
    create_region_and_connect(world, "Viridian Gym", "Gym Leader Castle -> Viridian Gym", gym_leader_castle)

def create_region(world: "PokemonStadiumWorld", name: str) -> Region:
    reg = Region(name, world.player, world.multiworld)

    for (key, data) in location_table.items():
        if data.region == name:
            if not is_valid_location(world, key):
                continue
            location = PokemonStadiumLocation(world.player, key, data.ap_code, reg)
            reg.locations.append(location)
    
    world.multiworld.regions.append(reg)
    return reg

def create_region_and_connect(world: "PokemonStadiumWorld", name: str, entrancename: str, connected_region: Region) -> Region:
    reg: Region = create_region(world, name)
    connected_region.connect(reg, entrancename)
    return reg
