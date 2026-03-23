from worlds.generic.Rules import set_rule, add_item_rule
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import PokemonStadiumWorld

def set_rules(world: "PokemonStadiumWorld"):
    player = world.player
    options = world.options

    # Gym Access
    set_rule(world.multiworld.get_location("Pewter Gym", player), lambda state: state.has("Pewter City Key", player))
    set_rule(world.multiworld.get_location("Cerulean Gym", player), lambda state: state.has("Cerulean City Key", player))
    set_rule(world.multiworld.get_location("Vermillion Gym", player), lambda state: state.has("Vermillion City Key", player))
    set_rule(world.multiworld.get_location("Celadon Gym", player), lambda state: state.has("Celadon City Key", player))
    set_rule(world.multiworld.get_location("Fuchsia Gym", player), lambda state: state.has("Fuchsia City Key", player))
    set_rule(world.multiworld.get_location("Saffron Gym", player), lambda state: state.has("Saffron City Key", player))
    set_rule(world.multiworld.get_location("Cinnabar Gym", player), lambda state: state.has("Cinnabar Island Key", player))
    set_rule(world.multiworld.get_location("Viridian Gym", player), lambda state: state.has("Viridian City Key", player))

    set_rule(world.multiworld.get_location("BROCK", player), lambda state: state.has("Pewter City Key", player))
    set_rule(world.multiworld.get_location("MISTY", player), lambda state: state.has("Cerulean City Key", player))
    set_rule(world.multiworld.get_location("SURGE", player), lambda state: state.has("Vermillion City Key", player))
    set_rule(world.multiworld.get_location("ERIKA", player), lambda state: state.has("Celadon City Key", player))
    set_rule(world.multiworld.get_location("KOGA", player), lambda state: state.has("Fuchsia City Key", player))
    set_rule(world.multiworld.get_location("SABRINA", player), lambda state: state.has("Saffron City Key", player))
    set_rule(world.multiworld.get_location("BLAINE", player), lambda state: state.has("Cinnabar Island Key", player))
    set_rule(world.multiworld.get_location("GIOVANNI", player), lambda state: state.has("Viridian City Key", player))

    # Cup Access
    set_rule(world.multiworld.get_location("Poké Cup - Great Ball - Prize", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 0)
    set_rule(world.multiworld.get_location("Poké Cup - Ultra Ball - Prize", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 1)
    set_rule(world.multiworld.get_location("Poké Cup - Master Ball - Prize", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 2)

    set_rule(world.multiworld.get_location("Prime Cup - Great Ball - Prize", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 0)
    set_rule(world.multiworld.get_location("Prime Cup - Ultra Ball - Prize", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 1)
    set_rule(world.multiworld.get_location("Prime Cup - Master Ball - Prize", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 2)

    #Trainersanity All
    if world.options.Trainersanity.value == 1:
        set_rule(world.multiworld.get_location("Pewter Gym - Bug Boy", player), lambda state: state.has("Pewter City Key", player))
        set_rule(world.multiworld.get_location("Pewter Gym - Lad", player), lambda state: state.has("Pewter City Key", player))
        set_rule(world.multiworld.get_location("Pewter Gym - Jr(M)", player), lambda state: state.has("Pewter City Key", player))

        set_rule(world.multiworld.get_location("Cerulean Gym - Fisher", player), lambda state: state.has("Cerulean City Key", player))
        set_rule(world.multiworld.get_location("Cerulean Gym - Jr(F)", player), lambda state: state.has("Cerulean City Key", player))
        set_rule(world.multiworld.get_location("Cerulean Gym - Swimmer", player), lambda state: state.has("Cerulean City Key", player))

        set_rule(world.multiworld.get_location("Vermillion Gym - Sailor", player), lambda state: state.has("Vermillion City Key", player))
        set_rule(world.multiworld.get_location("Vermillion Gym - Rocker", player), lambda state: state.has("Vermillion City Key", player))
        set_rule(world.multiworld.get_location("Vermillion Gym - Old Man", player), lambda state: state.has("Vermillion City Key", player))

        set_rule(world.multiworld.get_location("Celadon Gym - Lass", player), lambda state: state.has("Celadon City Key", player))
        set_rule(world.multiworld.get_location("Celadon Gym - Beauty", player), lambda state: state.has("Celadon City Key", player))
        set_rule(world.multiworld.get_location("Celadon Gym - Cool(F)", player), lambda state: state.has("Celadon City Key", player))
        
        set_rule(world.multiworld.get_location("Fuchsia Gym - Biker", player), lambda state: state.has("Fuchsia City Key", player))
        set_rule(world.multiworld.get_location("Fuchsia Gym - Tamer", player), lambda state: state.has("Fuchsia City Key", player))
        set_rule(world.multiworld.get_location("Fuchsia Gym - Juggler", player), lambda state: state.has("Fuchsia City Key", player))

        set_rule(world.multiworld.get_location("Saffron Gym - Cue Ball", player), lambda state: state.has("Saffron City Key", player))
        set_rule(world.multiworld.get_location("Saffron Gym - Burglar", player), lambda state: state.has("Saffron City Key", player))
        set_rule(world.multiworld.get_location("Saffron Gym - Medium", player), lambda state: state.has("Saffron City Key", player))

        set_rule(world.multiworld.get_location("Cinnabar Gym - Judoboy", player), lambda state: state.has("Cinnabar Island Key", player))
        set_rule(world.multiworld.get_location("Cinnabar Gym - Psychic", player), lambda state: state.has("Cinnabar Island Key", player))
        set_rule(world.multiworld.get_location("Cinnabar Gym - Nerd", player), lambda state: state.has("Cinnabar Island Key", player))

        set_rule(world.multiworld.get_location("Viridian Gym - Rocket", player), lambda state: state.has("Viridian City Key", player))
        set_rule(world.multiworld.get_location("Viridian Gym - Lab Man", player), lambda state: state.has("Viridian City Key", player))
        set_rule(world.multiworld.get_location("Viridian Gym - Cool(M)", player), lambda state: state.has("Viridian City Key", player))

        set_rule(world.multiworld.get_location("Poké Cup - Great Ball - Bug Boy", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 0)
        set_rule(world.multiworld.get_location("Poké Cup - Great Ball - Lad", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 0)
        set_rule(world.multiworld.get_location("Poké Cup - Great Ball - Nerd", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 0)
        set_rule(world.multiworld.get_location("Poké Cup - Great Ball - Sailor", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 0)
        set_rule(world.multiworld.get_location("Poké Cup - Great Ball - Jr(F)", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 0)
        set_rule(world.multiworld.get_location("Poké Cup - Great Ball - Jr(M)", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 0)
        set_rule(world.multiworld.get_location("Poké Cup - Great Ball - Lass", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 0)
        set_rule(world.multiworld.get_location("Poké Cup - Great Ball - Pokémaniac", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 0)

        set_rule(world.multiworld.get_location("Poké Cup - Ultra Ball - Bug Boy", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 1)
        set_rule(world.multiworld.get_location("Poké Cup - Ultra Ball - Lad", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 1)
        set_rule(world.multiworld.get_location("Poké Cup - Ultra Ball - Nerd", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 1)
        set_rule(world.multiworld.get_location("Poké Cup - Ultra Ball - Sailor", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 1)
        set_rule(world.multiworld.get_location("Poké Cup - Ultra Ball - Jr(F)", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 1)
        set_rule(world.multiworld.get_location("Poké Cup - Ultra Ball - Jr(M)", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 1)
        set_rule(world.multiworld.get_location("Poké Cup - Ultra Ball - Lass", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 1)
        set_rule(world.multiworld.get_location("Poké Cup - Ultra Ball - Pokémaniac", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 1)

        set_rule(world.multiworld.get_location("Poké Cup - Master Ball - Bug Boy", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 2)
        set_rule(world.multiworld.get_location("Poké Cup - Master Ball - Lad", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 2)
        set_rule(world.multiworld.get_location("Poké Cup - Master Ball - Nerd", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 2)
        set_rule(world.multiworld.get_location("Poké Cup - Master Ball - Sailor", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 2)
        set_rule(world.multiworld.get_location("Poké Cup - Master Ball - Jr(F)", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 2)
        set_rule(world.multiworld.get_location("Poké Cup - Master Ball - Jr(M)", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 2)
        set_rule(world.multiworld.get_location("Poké Cup - Master Ball - Lass", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 2)
        set_rule(world.multiworld.get_location("Poké Cup - Master Ball - Pokémaniac", player), lambda state: state.count('Poké Cup - Tier Upgrade', player) > 2)

        set_rule(world.multiworld.get_location("Prime Cup - Great Ball - Cue Ball", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 0)
        set_rule(world.multiworld.get_location("Prime Cup - Great Ball - Rocket", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 0)
        set_rule(world.multiworld.get_location("Prime Cup - Great Ball - Judoboy", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 0)
        set_rule(world.multiworld.get_location("Prime Cup - Great Ball - Gambler", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 0)
        set_rule(world.multiworld.get_location("Prime Cup - Great Ball - Cool(F)", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 0)
        set_rule(world.multiworld.get_location("Prime Cup - Great Ball - Bird Boy", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 0)
        set_rule(world.multiworld.get_location("Prime Cup - Great Ball - Lab Man", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 0)
        set_rule(world.multiworld.get_location("Prime Cup - Great Ball - Cool(M)", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 0)

        set_rule(world.multiworld.get_location("Prime Cup - Ultra Ball - Cue Ball", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 1)
        set_rule(world.multiworld.get_location("Prime Cup - Ultra Ball - Rocket", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 1)
        set_rule(world.multiworld.get_location("Prime Cup - Ultra Ball - Judoboy", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 1)
        set_rule(world.multiworld.get_location("Prime Cup - Ultra Ball - Gambler", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 1)
        set_rule(world.multiworld.get_location("Prime Cup - Ultra Ball - Cool(F)", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 1)
        set_rule(world.multiworld.get_location("Prime Cup - Ultra Ball - Bird Boy", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 1)
        set_rule(world.multiworld.get_location("Prime Cup - Ultra Ball - Lab Man", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 1)
        set_rule(world.multiworld.get_location("Prime Cup - Ultra Ball - Cool(M)", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 1)

        set_rule(world.multiworld.get_location("Prime Cup - Master Ball - Cue Ball", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 2)
        set_rule(world.multiworld.get_location("Prime Cup - Master Ball - Rocket", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 2)
        set_rule(world.multiworld.get_location("Prime Cup - Master Ball - Judoboy", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 2)
        set_rule(world.multiworld.get_location("Prime Cup - Master Ball - Gambler", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 2)
        set_rule(world.multiworld.get_location("Prime Cup - Master Ball - Cool(F)", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 2)
        set_rule(world.multiworld.get_location("Prime Cup - Master Ball - Bird Boy", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 2)
        set_rule(world.multiworld.get_location("Prime Cup - Master Ball - Lab Man", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 2)
        set_rule(world.multiworld.get_location("Prime Cup - Master Ball - Cool(M)", player), lambda state: state.count('Prime Cup - Tier Upgrade', player) > 2)

    # Beat Rival Rule
    badges = ["Boulder Badge", "Cascade Badge", "Thunder Badge", "Rainbow Badge", "Soul Badge", "Marsh Badge", "Volcano Badge", "Earth Badge"]
    set_rule(world.multiworld.get_location("Beat Rival", player), lambda state: state.has_all(badges, player))

    # Victory condition rule!
    world.multiworld.completion_condition[player] = lambda state: state.has("Victory", player)
