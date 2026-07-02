from worlds.generic.Rules import set_rule
from typing import TYPE_CHECKING, List, Tuple

if TYPE_CHECKING:
    from . import PokemonStadiumWorld

def set_rules(world: "PokemonStadiumWorld"):
    player = world.player
    options = world.options

    # Gym Access
    gym_info_tuples = [
        ('Pewter', 'BROCK'),
        ('Cerulean', 'MISTY'),
        ('Vermillion', 'SURGE'),
        ('Celadon', 'ERIKA'),
        ('Fuchsia', 'KOGA'),
        ('Saffron', 'SABRINA'),
        ('Cinnabar', 'BLAINE'),
        ('Viridian', 'GIOVANNI'),
    ]
    set_glc_base_rules(world, player, gym_info_tuples)

    # Cup Access
    set_cup_base_rules(world, player)

    #Trainersanity All
    if world.options.Trainersanity.value == 1:
        trainers = ['Bug Boy', 'Lad', 'Jr(M)']
        set_glc_trainersanity_rules(world, player, 'Pewter', trainers)

        trainers = ['Fisher', 'Jr(F)', 'Swimmer']
        set_glc_trainersanity_rules(world, player, 'Cerulean', trainers)

        trainers = ['Sailor', 'Rocker', 'Old Man']
        set_glc_trainersanity_rules(world, player, 'Vermillion', trainers)

        trainers = ['Lass', 'Beauty', 'Cool(F)']
        set_glc_trainersanity_rules(world, player, 'Celadon', trainers)

        trainers = ['Biker', 'Tamer', 'Juggler']
        set_glc_trainersanity_rules(world, player, 'Fuchsia', trainers)

        trainers = ['Cue Ball', 'Burglar', 'Medium']
        set_glc_trainersanity_rules(world, player, 'Saffron', trainers)

        trainers = ['Judoboy', 'Psychic', 'Nerd']
        set_glc_trainersanity_rules(world, player, 'Cinnabar', trainers)

        trainers = ['Rocket', 'Lab Man', 'Cool(M)']
        set_glc_trainersanity_rules(world, player, 'Viridian', trainers)

        trainers = ['Bug Boy', 'Lad', 'Nerd', 'Sailor', 'Jr(F)', 'Jr(M)', 'Lass', 'Pokémaniac']
        set_cup_trainersanity_rules(world, player, 'Poké', trainers)

        trainers = ['Cue Ball', 'Rocket', 'Judoboy', 'Gambler', 'Cool(F)', 'Bird Boy', 'Lab Man', 'Cool(M)']
        set_cup_trainersanity_rules(world, player, 'Prime', trainers)

    # Beat Rival Rule
    badges = ["Boulder Badge", "Cascade Badge", "Thunder Badge", "Rainbow Badge", "Soul Badge", "Marsh Badge", "Volcano Badge", "Earth Badge"]
    badge_requirement = world.options.BadgeRequirement.value
    has_enough_badges = lambda state: state.has_from_list(badges, player, badge_requirement)
    set_rule(world.multiworld.get_location("Beat Rival", player), has_enough_badges)

    # Master Ball Cups Cleared Rule
    collected_all_poke_cup_tiers = lambda state: state.count('Poké Cup - Tier Upgrade', player) > 2
    collected_all_prime_cup_tiers = lambda state: state.count('Prime Cup - Tier Upgrade', player) > 2
    set_rule(world.multiworld.get_location("Master Ball Cups Cleared", player), collected_all_poke_cup_tiers and collected_all_prime_cup_tiers)

    # Rival + Cups Rule
    full_clear = has_enough_badges and collected_all_poke_cup_tiers and collected_all_prime_cup_tiers
    set_rule(world.multiworld.get_location('Beat Rival and Clear Both Master Ball Cups', player), full_clear)

    # Victory condition rule!
    world.multiworld.completion_condition[player] = lambda state: state.has("Victory", player)


def set_glc_base_rules(world: 'PokemonStadiumWorld', player: int, gym_info_tuples: List[Tuple[str, str]]):
    for gym_info in gym_info_tuples:
        gym = gym_info[0]
        leader = gym_info[1]
        location = f'{gym_info[0]} Gym'
        item = f'{gym} City Key' if gym != 'Cinnabar' else f'{gym} Island Key'
        set_rule(world.multiworld.get_location(location, player), lambda state: state.has(item, player))
        set_rule(world.multiworld.get_location(leader, player), lambda state: state.has(item, player))


def set_cup_base_rules(world: 'PokemonStadiumWorld', player: int):
    cups = ['Poké', 'Prime']
    tiers = ['Great', 'Ultra', 'Master']
    for cup in cups:
        item = f'{cup} Cup - Tier Upgrade'
        for i, tier in enumerate(tiers):
            location = f'{cup} Cup - {tier} Ball - Prize'
            set_rule(world.multiworld.get_location(location, player), lambda state: state.count(item, player) > i)


def set_glc_trainersanity_rules(world: 'PokemonStadiumWorld', player: int, gym_name: str, trainers: List[str]):
    item = f'{gym_name} City Key' if gym_name != 'Cinnabar' else f'{gym_name} Island Key'
    for i, trainer in enumerate(trainers):
        location = f'{gym_name} Gym - {trainer}'
        set_rule(world.multiworld.get_location(location, player), lambda state: state.has(item, player))


def set_cup_trainersanity_rules(world: 'PokemonStadiumWorld', player: int, cup_name: str, trainers: List[str]):
    tiers = ['Great', 'Ultra', 'Master']
    item = f'{cup_name} Cup - Tier Upgrade'
    for i, tier in enumerate(tiers):
        for trainer in trainers:
            location = f'{cup_name} Cup - {tier} Ball - {trainer}'
            set_rule(world.multiworld.get_location(location, player), lambda state: state.count(item, player) > i)
