"""
Classes and functions related to creating a ROM patch
"""

from settings import get_settings
from worlds.Files import APProcedurePatch, APTokenMixin

class PokemonStadiumProcedurePatch(APProcedurePatch, APTokenMixin):
    game = "Pokemon Stadium"
    hash = "605b89b67018abcea91e693a4dd25be3"
    patch_file_ending = ".apstadium"
    result_file_ending = ".z64"

    procedure = [
        ("apply_bsdiff4", ["base_patch.bsdiff4"]),
        ("apply_tokens", ["token_data.bin"])
    ]

    @classmethod
    def get_source_data(cls) -> bytes:
        with open(get_settings().pokemon_stadium_settings.rom_file, "rb") as infile:
            base_rom_bytes = bytes(infile.read())

        return base_rom_bytes
