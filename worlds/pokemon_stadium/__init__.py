from BaseClasses import Tutorial
import settings
from worlds.AutoWorld import WebWorld

from .options import OPTION_GROUPS
from .rom import PokemonStadiumProcedurePatch

class PokemonStadiumWebWorld(WebWorld):
    """
    Webhost info for Pokemon Stadium
    """

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to playing Pokémon Stadium with Archipelago.",
        "English",
        "setup_en.md",
        "setup/en",
        ["JCIII"]
    )

    tutorials = [setup_en]
    option_groups = OPTION_GROUPS

class PokemonStadiumSettings(settings.Group):
    class PokemonStadiumRomFile(settings.UserFilePath):
        """File name of your English Pokemon Stadium ROM"""
        description = "Pokemon Stadium ROM File"
        copy_to = "Pokemon Stadium (USA).z64"
        md5s = [PokemonStadiumProcedurePatch.hash]

    rom_file: PokemonStadiumRomFile = PokemonStadiumRomFile(PokemonStadiumRomFile.copy_to)
