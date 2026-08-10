from typing import Dict, TYPE_CHECKING
import logging

from .Types import LocData

if TYPE_CHECKING:
    from . import PokemonStadiumWorld

def get_total_locations(world: 'PokemonStadiumWorld') -> int:
    if world.options.Trainersanity.value == 1:
        location_table.update(trainersanity_locations)

    return len(location_table)

def get_location_names() -> Dict[str, int]:
    temp_loc_table = location_table.copy()
    temp_loc_table.update(trainersanity_locations)

    names = {name: data.ap_code for name, data in temp_loc_table.items()}

    return names

def is_valid_location(world: 'PokemonStadiumWorld', name) -> bool:
    return True

pokemon_stadium_locations = {
    'Magikarp\'s Splash':                       LocData(20000100, 'Kids Club'),
    'Clefairy Says':                            LocData(20000101, 'Kids Club'),
    'Run, Rattata, Run':                        LocData(20000102, 'Kids Club'),
    'Snore War':                                LocData(20000103, 'Kids Club'),
    'Thundering Dynamo':                        LocData(20000104, 'Kids Club'),
    'Sushi-Go-Round':                           LocData(20000105, 'Kids Club'),
    'Ekans\'s Hoop Hurl':                       LocData(20000106, 'Kids Club'),
    'Rock Harden':                              LocData(20000107, 'Kids Club'),
    'Dig! Dig! Dig!':                           LocData(20000108, 'Kids Club'),

    'Poké Cup - Poké Ball - Prize':             LocData(20000300, 'Poké Cup'),
    'Poké Cup - Poké Ball - Tier Upgrade':      LocData(20000309, 'Poké Cup'),
    'Poké Cup - Great Ball - Prize':            LocData(20000310, 'Poké Cup'),
    'Poké Cup - Great Ball - Tier Upgrade':     LocData(20000319, 'Poké Cup'),
    'Poké Cup - Ultra Ball - Prize':            LocData(20000320, 'Poké Cup'),
    'Poké Cup - Ultra Ball - Tier Upgrade':     LocData(20000329, 'Poké Cup'),
    'Poké Cup - Master Ball - Prize':           LocData(20000330, 'Poké Cup'),

    'Petit Cup Prize':                          LocData(20000400, 'Petit Cup'),

    'Pika Cup Prize':                           LocData(20000500, 'Pika Cup'),

    'Prime Cup - Poké Ball - Prize':            LocData(20000600, 'Prime Cup'),
    'Prime Cup - Poké Ball - Tier Upgrade':     LocData(20000609, 'Prime Cup'),
    'Prime Cup - Great Ball - Prize':           LocData(20000610, 'Prime Cup'),
    'Prime Cup - Great Ball - Tier Upgrade':    LocData(20000619, 'Prime Cup'),
    'Prime Cup - Ultra Ball - Prize':           LocData(20000620, 'Prime Cup'),
    'Prime Cup - Ultra Ball - Tier Upgrade':    LocData(20000629, 'Prime Cup'),
    'Prime Cup - Master Ball - Prize':          LocData(20000630, 'Prime Cup'),

    'BROCK':                                    LocData(20000704, 'Gym Leader Castle'),
    'Pewter Gym':                               LocData(20000705, 'Gym Leader Castle'),
    'MISTY':                                    LocData(20000714, 'Gym Leader Castle'),
    'Cerulean Gym':                             LocData(20000715, 'Gym Leader Castle'),
    'SURGE':                                    LocData(20000724, 'Gym Leader Castle'),
    'Vermillion Gym':                           LocData(20000725, 'Gym Leader Castle'),
    'ERIKA':                                    LocData(20000734, 'Gym Leader Castle'),
    'Celadon Gym':                              LocData(20000735, 'Gym Leader Castle'),
    'KOGA':                                     LocData(20000744, 'Gym Leader Castle'),
    'Fuchsia Gym':                              LocData(20000745, 'Gym Leader Castle'),
    'SABRINA':                                  LocData(20000754, 'Gym Leader Castle'),
    'Saffron Gym':                              LocData(20000755, 'Gym Leader Castle'),
    'BLAINE':                                   LocData(20000764, 'Gym Leader Castle'),
    'Cinnabar Gym':                             LocData(20000765, 'Gym Leader Castle'),
    'GIOVANNI':                                 LocData(20000774, 'Gym Leader Castle'),
    'Viridian Gym':                             LocData(20000775, 'Gym Leader Castle'),
}

event_locations = {
    'Beat Rival':                                   LocData(20000001, 'Hall of Fame'),
    'Master Ball Cups Cleared':                     LocData(20000002, 'Hall of Fame'),
    'Beat Rival and Clear Both Master Ball Cups':   LocData(20000003, 'Hall of Fame'),
}

trainersanity_locations = {
    'Poké Cup - Poké Ball - Biker':             LocData(20000301, 'Poké Cup'),
    'Poké Cup - Poké Ball - Rocker':            LocData(20000302, 'Poké Cup'),
    'Poké Cup - Poké Ball - Juggler':           LocData(20000303, 'Poké Cup'),
    'Poké Cup - Poké Ball - Beauty':            LocData(20000304, 'Poké Cup'),
    'Poké Cup - Poké Ball - Medium':            LocData(20000305, 'Poké Cup'),
    'Poké Cup - Poké Ball - Tamer':             LocData(20000306, 'Poké Cup'),
    'Poké Cup - Poké Ball - Psychic':           LocData(20000307, 'Poké Cup'),
    'Poké Cup - Poké Ball - Old Man':           LocData(20000308, 'Poké Cup'),
    'Poké Cup - Great Ball - Biker':            LocData(20000311, 'Poké Cup'),
    'Poké Cup - Great Ball - Rocker':           LocData(20000312, 'Poké Cup'),
    'Poké Cup - Great Ball - Juggler':          LocData(20000313, 'Poké Cup'),
    'Poké Cup - Great Ball - Beauty':           LocData(20000314, 'Poké Cup'),
    'Poké Cup - Great Ball - Medium':           LocData(20000315, 'Poké Cup'),
    'Poké Cup - Great Ball - Tamer':            LocData(20000316, 'Poké Cup'),
    'Poké Cup - Great Ball - Psychic':          LocData(20000317, 'Poké Cup'),
    'Poké Cup - Great Ball - Old Man':          LocData(20000318, 'Poké Cup'),
    'Poké Cup - Ultra Ball - Biker':            LocData(20000321, 'Poké Cup'),
    'Poké Cup - Ultra Ball - Rocker':           LocData(20000322, 'Poké Cup'),
    'Poké Cup - Ultra Ball - Juggler':          LocData(20000323, 'Poké Cup'),
    'Poké Cup - Ultra Ball - Beauty':           LocData(20000324, 'Poké Cup'),
    'Poké Cup - Ultra Ball - Medium':           LocData(20000325, 'Poké Cup'),
    'Poké Cup - Ultra Ball - Tamer':            LocData(20000326, 'Poké Cup'),
    'Poké Cup - Ultra Ball - Psychic':          LocData(20000327, 'Poké Cup'),
    'Poké Cup - Ultra Ball - Old Man':          LocData(20000328, 'Poké Cup'),
    'Poké Cup - Master Ball - Biker':           LocData(20000331, 'Poké Cup'),
    'Poké Cup - Master Ball - Rocker':          LocData(20000332, 'Poké Cup'),
    'Poké Cup - Master Ball - Juggler':         LocData(20000333, 'Poké Cup'),
    'Poké Cup - Master Ball - Beauty':          LocData(20000334, 'Poké Cup'),
    'Poké Cup - Master Ball - Medium':          LocData(20000335, 'Poké Cup'),
    'Poké Cup - Master Ball - Tamer':           LocData(20000336, 'Poké Cup'),
    'Poké Cup - Master Ball - Psychic':         LocData(20000337, 'Poké Cup'),
    'Poké Cup - Master Ball - Old Man':         LocData(20000338, 'Poké Cup'),

    'Petit Cup - Bug Boy':                      LocData(20000401, 'Petit Cup'),
    'Petit Cup - Lad':                          LocData(20000402, 'Petit Cup'),
    'Petit Cup - Nerd':                         LocData(20000403, 'Petit Cup'),
    'Petit Cup - Sailor':                       LocData(20000404, 'Petit Cup'),
    'Petit Cup - Jr(F)':                        LocData(20000405, 'Petit Cup'),
    'Petit Cup - Jr(M)':                        LocData(20000406, 'Petit Cup'),
    'Petit Cup - Lass':                         LocData(20000407, 'Petit Cup'),
    'Petit Cup - Pokémaniac':                   LocData(20000408, 'Petit Cup'),

    'Pika Cup - Bug Boy':                       LocData(20000501, 'Pika Cup'),
    'Pika Cup - Lad':                           LocData(20000502, 'Pika Cup'),
    'Pika Cup - Swimmer':                       LocData(20000503, 'Pika Cup'),
    'Pika Cup - Burglar':                       LocData(20000504, 'Pika Cup'),
    'Pika Cup - Mr. Fix':                       LocData(20000505, 'Pika Cup'),
    'Pika Cup - Hiker':                         LocData(20000506, 'Pika Cup'),
    'Pika Cup - Lass':                          LocData(20000507, 'Pika Cup'),
    'Pika Cup - Fisher':                        LocData(20000508, 'Pika Cup'),

    'Prime Cup - Poké Ball - Cue Ball':         LocData(20000601, 'Prime Cup'),
    'Prime Cup - Poké Ball - Rocket':           LocData(20000602, 'Prime Cup'),
    'Prime Cup - Poké Ball - Judoboy':          LocData(20000603, 'Prime Cup'),
    'Prime Cup - Poké Ball - Gambler':          LocData(20000604, 'Prime Cup'),
    'Prime Cup - Poké Ball - Cool(F)':          LocData(20000605, 'Prime Cup'),
    'Prime Cup - Poké Ball - Bird Boy':         LocData(20000606, 'Prime Cup'),
    'Prime Cup - Poké Ball - Lab Man':          LocData(20000607, 'Prime Cup'),
    'Prime Cup - Poké Ball - Cool(M)':          LocData(20000608, 'Prime Cup'),
    'Prime Cup - Great Ball - Cue Ball':        LocData(20000611, 'Prime Cup'),
    'Prime Cup - Great Ball - Rocket':          LocData(20000612, 'Prime Cup'),
    'Prime Cup - Great Ball - Judoboy':         LocData(20000613, 'Prime Cup'),
    'Prime Cup - Great Ball - Gambler':         LocData(20000614, 'Prime Cup'),
    'Prime Cup - Great Ball - Cool(F)':         LocData(20000615, 'Prime Cup'),
    'Prime Cup - Great Ball - Bird Boy':        LocData(20000616, 'Prime Cup'),
    'Prime Cup - Great Ball - Lab Man':         LocData(20000617, 'Prime Cup'),
    'Prime Cup - Great Ball - Cool(M)':         LocData(20000618, 'Prime Cup'),
    'Prime Cup - Ultra Ball - Cue Ball':        LocData(20000621, 'Prime Cup'),
    'Prime Cup - Ultra Ball - Rocket':          LocData(20000622, 'Prime Cup'),
    'Prime Cup - Ultra Ball - Judoboy':         LocData(20000623, 'Prime Cup'),
    'Prime Cup - Ultra Ball - Gambler':         LocData(20000624, 'Prime Cup'),
    'Prime Cup - Ultra Ball - Cool(F)':         LocData(20000625, 'Prime Cup'),
    'Prime Cup - Ultra Ball - Bird Boy':        LocData(20000626, 'Prime Cup'),
    'Prime Cup - Ultra Ball - Lab Man':         LocData(20000627, 'Prime Cup'),
    'Prime Cup - Ultra Ball - Cool(M)':         LocData(20000628, 'Prime Cup'),
    'Prime Cup - Master Ball - Cue Ball':       LocData(20000631, 'Prime Cup'),
    'Prime Cup - Master Ball - Rocket':         LocData(20000632, 'Prime Cup'),
    'Prime Cup - Master Ball - Judoboy':        LocData(20000633, 'Prime Cup'),
    'Prime Cup - Master Ball - Gambler':        LocData(20000634, 'Prime Cup'),
    'Prime Cup - Master Ball - Cool(F)':        LocData(20000635, 'Prime Cup'),
    'Prime Cup - Master Ball - Bird Boy':       LocData(20000636, 'Prime Cup'),
    'Prime Cup - Master Ball - Lab Man':        LocData(20000637, 'Prime Cup'),
    'Prime Cup - Master Ball - Cool(M)':        LocData(20000638, 'Prime Cup'),

    'Pewter Gym - Bug Boy':                     LocData(20000701, 'Gym Leader Castle'),
    'Pewter Gym - Lad':                         LocData(20000702, 'Gym Leader Castle'),
    'Pewter Gym - Jr(M)':                       LocData(20000703, 'Gym Leader Castle'),
    'Cerulean Gym - Fisher':                    LocData(20000711, 'Gym Leader Castle'),
    'Cerulean Gym - Jr(F)':                     LocData(20000712, 'Gym Leader Castle'),
    'Cerulean Gym - Swimmer':                   LocData(20000713, 'Gym Leader Castle'),
    'Vermillion Gym - Sailor':                  LocData(20000721, 'Gym Leader Castle'),
    'Vermillion Gym - Rocker':                  LocData(20000722, 'Gym Leader Castle'),
    'Vermillion Gym - Old Man':                 LocData(20000723, 'Gym Leader Castle'),
    'Celadon Gym - Lass':                       LocData(20000731, 'Gym Leader Castle'),
    'Celadon Gym - Beauty':                     LocData(20000732, 'Gym Leader Castle'),
    'Celadon Gym - Cool(F)':                    LocData(20000733, 'Gym Leader Castle'),
    'Fuchsia Gym - Biker':                      LocData(20000741, 'Gym Leader Castle'),
    'Fuchsia Gym - Tamer':                      LocData(20000742, 'Gym Leader Castle'),
    'Fuchsia Gym - Juggler':                    LocData(20000743, 'Gym Leader Castle'),
    'Saffron Gym - Cue Ball':                   LocData(20000751, 'Gym Leader Castle'),
    'Saffron Gym - Burglar':                    LocData(20000752, 'Gym Leader Castle'),
    'Saffron Gym - Medium':                     LocData(20000753, 'Gym Leader Castle'),
    'Cinnabar Gym - Judoboy':                   LocData(20000761, 'Gym Leader Castle'),
    'Cinnabar Gym - Psychic':                   LocData(20000762, 'Gym Leader Castle'),
    'Cinnabar Gym - Nerd':                      LocData(20000763, 'Gym Leader Castle'),
    'Viridian Gym - Rocket':                    LocData(20000771, 'Gym Leader Castle'),
    'Viridian Gym - Lab Man':                   LocData(20000772, 'Gym Leader Castle'),
    'Viridian Gym - Cool(M)':                   LocData(20000773, 'Gym Leader Castle'),
}

location_table = {
    **pokemon_stadium_locations,
    **event_locations
}
