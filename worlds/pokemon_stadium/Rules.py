from worlds.generic.Rules import add_rule
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import PokemonStadiumWorld

def set_rules(world: "PokemonStadiumWorld"):
    player = world.player
    options = world.options

    # Gym Access
    add_rule(world.multiworld.get_entrance("Gym Leader Castle -> Pewter Gym", player), lambda state: state.has("Pewter City Key", player))
    add_rule(world.multiworld.get_entrance("Gym Leader Castle -> Cerulean Gym", player), lambda state: state.has("Cerulean City Key", player))
    add_rule(world.multiworld.get_entrance("Gym Leader Castle -> Vermillion Gym", player), lambda state: state.has("Vermillion City Key", player))
    add_rule(world.multiworld.get_entrance("Gym Leader Castle -> Celadon Gym", player), lambda state: state.has("Celadon City Key", player))
    add_rule(world.multiworld.get_entrance("Gym Leader Castle -> Fuchsia Gym", player), lambda state: state.has("Fuchsia City Key", player))
    add_rule(world.multiworld.get_entrance("Gym Leader Castle -> Saffron Gym", player), lambda state: state.has("Saffron City Key", player))
    add_rule(world.multiworld.get_entrance("Gym Leader Castle -> Cinnabar Gym", player), lambda state: state.has("Cinnabar City Key", player))
    add_rule(world.multiworld.get_entrance("Gym Leader Castle -> Viridian Gym", player), lambda state: state.has("Viridian City Key", player))

    # Victory condition rule!
    world.multiworld.completion_condition[player] = lambda state: state.has("Victory", player)
