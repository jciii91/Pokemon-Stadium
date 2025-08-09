import logging

from BaseClasses import MultiWorld, Item, Tutorial
from worlds.AutoWorld import World, CollectionState, WebWorld
from typing import Dict

from .Locations import get_location_names, get_total_locations
from .Items import create_item, create_itempool, item_table
from .Options import PokemonStadiumOptions
from .Regions import create_regions

class PokemonStadiumWeb(WebWorld):
    theme = "Party"

    tutorials = [Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up (the game you are randomizing) for Archipelago. "
        "This guide covers single-player, multiworld, and related software.",
        "English",
        "setup_en.md",
        "setup/en",
        ["JCIII"]
    )]

class PokemonStadiumWorld(World):
    game = "Pokemon Stadium"

    item_name_to_id = {name: data.ap_code for name, data in item_table.items()}

    location_name_to_id = get_location_names()

    options_dataclass = PokemonStadiumOptions
    options = PokemonStadiumOptions

    web = PokemonStadiumWeb()

    def __init__(self, multiworld: "MultiWorld", player: int):
        super().__init__(multiworld, player)

    def generate_early(self):
        self.multiworld.push_precollected()

    def create_regions(self):
        create_regions(self)

    def create_items(self):
        self.multiworld.itempool += create_itempool(self)

    def create_item(self, name: str) -> Item:
        return create_item(self, name)

    def fill_slot_data(self) -> Dict[str, object]:
        slot_data: Dict[str, object] = {
            "options": {
                "StartingGyms":         self.options.VictoryCondition.value,
                "StartingCups":         self.options.GymCastleTrainerRandomness.value,
            },
            "Seed": self.multiworld.seed_name,  # to verify the server's multiworld
            "Slot": self.multiworld.player_name[self.player],  # to connect to server
            "TotalLocations": get_total_locations(self) # get_total_locations(self) comes from Locations.py
        }

        return slot_data

    def collect(self, state: "CollectionState", item: "Item") -> bool:
        return super().collect(state, item)

    def remove(self, state: "CollectionState", item: "Item") -> bool:
        return super().remove(state, item)
