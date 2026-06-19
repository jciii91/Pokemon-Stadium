import random

from worlds.Files import APTokenTypes

from .constants import (
    kanto_dex_names,
    growth_rates,
    petit_cup_indexes,
    petitcupr1_levels,
    pikacupr1_levels,
    pika_cup_indexes,
    pokecupr1_master_levels,
    pokecupr1_ultra_levels,
    rom_offsets,
    vanilla_movesets,
)
from . import util
from .randomizePokemonBaseValues import BaseValuesRandomizer
from . import randomMovesetGenerator
from . import writeDisplayData

NOP = bytes([0x00,0x00,0x00,0x00])

class Randomizer():
    def __init__(self, version="US_1.0", bst_factor=1, glc_trainer_factor=1, pokecup_trainer_factor=1, primecup_trainer_factor=1, petitcup_trainer_factor=1,
                 pikacup_trainer_factor=1, glc_rental_factor=1, pokecup_rental_factor=1, primecup_rental_factor=1, petitcup_rental_factor=1, pikacup_rental_factor=1,
                 rental_list_shuffle_factor=1, rls_glc_factor=1, rls_poke_factor=1, rls_prime_factor=1, rls_petit_factor=1, rls_pika_factor=1):
        self.version = version
        self.bst_factor = bst_factor
        self.glc_trainer_factor = glc_trainer_factor
        self.pokecup_trainer_factor = pokecup_trainer_factor
        self.primecup_trainer_factor = primecup_trainer_factor
        self.petitcup_trainer_factor = petitcup_trainer_factor
        self.pikacup_trainer_factor = pikacup_trainer_factor
        self.glc_rental_factor = glc_rental_factor
        self.pokecup_rental_factor = pokecup_rental_factor
        self.primecup_rental_factor = primecup_rental_factor
        self.petitcup_rental_factor = petitcup_rental_factor
        self.rental_list_shuffle_factor = rental_list_shuffle_factor
        self.pikacup_rental_factor = pikacup_rental_factor
        self.rls_glc_factor = rls_glc_factor
        self.rls_poke_factor = rls_poke_factor
        self.rls_prime_factor = rls_prime_factor
        self.rls_petit_factor = rls_petit_factor
        self.rls_pika_factor = rls_pika_factor

        self.evs = []
        self.ivs = []
        for _ in range(0, 149):
            self.evs.append(util.Util.random_int_set(0, 65535, 5))
            self.ivs.append(util.Util.random_string_hex(4))

        self.new_display_stats = []
        self.bst_list = []

        if(bst_factor == 1):
            for i in range(149):
                stats = kanto_dex_names[i]['bst']
                self.bst_list.append(stats)
                self.new_display_stats.append(stats)


    def disable_checksum(self, patch) -> None:
        offset = rom_offsets[self.version]["CheckSum1"]
        patch.write_token(APTokenTypes.WRITE, offset, NOP)

        offset = rom_offsets[self.version]["CheckSum2"]
        patch.write_token(APTokenTypes.WRITE, offset, NOP)


    def randomize_base_stats(self, patch) -> None:
        offset = rom_offsets[self.version]["BaseStats"]
        for i in range(149):
            stats = kanto_dex_names[i]['bst']
            if self.bst_factor > 1:
                randomized_base_stats = BaseValuesRandomizer.randomize_stats(stats, self.bst_factor)

                # Convert to list of integers for BST processing
                self.bst_list.append(list(randomized_base_stats))

                # Store modified stats for display
                self.new_display_stats.append(randomized_base_stats)

                # Write the new randomized stats back
                patch.write_token(APTokenTypes.WRITE, offset, bytes(randomized_base_stats))
            else:
                # store vanilla stats
                self.bst_list.append(stats)
                self.new_display_stats.append(stats)

            # Move to the next Pokémon entry (skip 18 additional bytes)
            offset += 23


    def write_pokemon_bytes(self, patch, offset, dex_index, pokemon, factor, level) -> None:
        pokedex_num = dex_index + 1
        patch.write_token(APTokenTypes.WRITE, offset, bytes([pokedex_num]))  # Write Pokémon index
        offset += 1

        offset += 5  # Seek forward by 5 bytes

        new_type = bytes.fromhex(pokemon["type"])
        patch.write_token(APTokenTypes.WRITE, offset, bytes(new_type)) # Write Pokémon type
        offset += len(new_type)

        offset += 1  # Seek forward by 1 byte

        # Random moveset
        bst = self.bst_list[dex_index]
        new_attacks = randomMovesetGenerator.MovesetGenerator.get_random_moveset(bst, factor, new_type)
        for attack in new_attacks:
            patch.write_token(APTokenTypes.WRITE, offset, bytes([attack]))
            offset += 1

        offset += 4  # Seek forward by 4 bytes

        growth_rate = pokemon["gr"]
        exp_for_level = growth_rates[growth_rate][level]
        exp = int.to_bytes(int(exp_for_level), 3, "big")
        patch.write_token(APTokenTypes.WRITE, offset, exp)
        offset += 3

        for t in range(5):
            ev = int.to_bytes(self.evs[dex_index][t], 2, "big")
            patch.write_token(APTokenTypes.WRITE, offset, ev)
            offset += 2

        ivs_bytes = bytes.fromhex(self.ivs[dex_index])
        patch.write_token(APTokenTypes.WRITE, offset, ivs_bytes)
        offset += len(ivs_bytes)

        offset += 6  # Seek forward by 6 bytes

        new_stats = self.new_display_stats[dex_index]
        evs = self.evs[dex_index]
        ivs = self.ivs[dex_index]
        disp = writeDisplayData.DisplayDataWriter.write_gym_tower_display(new_stats, evs, ivs, level)
        patch.write_token(APTokenTypes.WRITE, offset, bytes(disp))
        offset += len(disp)

        pokemon_name = pokemon["name"].encode()
        patch.write_token(APTokenTypes.WRITE, offset, bytes(pokemon_name))
        offset += len(pokemon_name)

        # Check if a Nidoran is being written in to add their gender symbol
        if pokedex_num == 28:
            patch.write_token(APTokenTypes.WRITE, offset, bytes.fromhex("BE")) # Female symbol
            offset += 1
            pokemon_name += b" "
        elif pokedex_num == 31:
            patch.write_token(APTokenTypes.WRITE, offset, bytes.fromhex("A9")) # Male symbol
            offset += 1
            pokemon_name += b" "

        # Fill in blank spaces to make the name 11 bytes long
        if len(pokemon_name) < 11:
            blanks = 11 - len(pokemon_name)
            patch.write_token(APTokenTypes.WRITE, offset, b"\x00" * blanks)
            offset += blanks


    def randomize_glc_trainer_pokemon_round1(self, patch) -> None:
        offset = rom_offsets[self.version]["GymCastle_Round1"]
        for q in range(10):
            team_count = 4 if q < 9 else 7
            for _ in range(team_count):
                new_team = random.sample(range(149), 6)
                for s in range(6):
                    dex_index = new_team[s]
                    pokemon = kanto_dex_names[dex_index]
                    factor = self.glc_trainer_factor
                    level = 50
                    self.write_pokemon_bytes(patch, offset, dex_index, pokemon, factor, level)

                    offset += 25  # Seek forward by 25 bytes
                offset += 56  # Seek forward by 56 bytes
            offset += 16  # Seek forward by 16 bytes


    def randomize_pokecup_trainer_pokemon_round1(self, patch) -> None:
        offset = rom_offsets[self.version]["PokeCup_Round1"]
        for q in range(4):
            team_count = 8 
            for _ in range(team_count):
                new_team = random.sample(range(149), 6)
                for s in range(6):
                    dex_index = new_team[s]
                    pokemon = kanto_dex_names[dex_index]
                    factor = self.glc_trainer_factor

                    if q < 2:
                        level = 50 + q
                    elif q == 2:
                        level = pokecupr1_ultra_levels[_][s]
                    else:
                        level = pokecupr1_master_levels[_][s]

                    self.write_pokemon_bytes(patch, offset, dex_index, pokemon, factor, level)

                    offset += 25  # Seek forward by 25 bytes
                offset += 56  # Seek forward by 56 bytes
            offset += 16  # Seek forward by 16 bytes


    def randomize_primecup_trainer_pokemon_round1(self, patch) -> None:
        offset = rom_offsets[self.version]["PrimeCup_Round1"]
        for q in range(4):
            team_count = 8
            for _ in range(team_count):
                new_team = random.sample(range(149), 6)
                for s in range(6):
                    dex_index = new_team[s]
                    pokemon = kanto_dex_names[dex_index]
                    factor = self.primecup_trainer_factor
                    level = 100
                    self.write_pokemon_bytes(patch, offset, dex_index, pokemon, factor, level)

                    offset += 25  # Seek forward by 25 bytes
                offset += 56  # Seek forward by 56 bytes
            offset += 16  # Seek forward by 16 bytes


    def randomize_petitcup_trainer_pokemon_round1(self, patch) -> None:
        offset = rom_offsets[self.version]["PetitCup_Round1"]
        team_count = 8
        for _ in range(team_count):
            new_team = random.sample(petit_cup_indexes, 6)
            for s in range(6):
                dex_index = new_team[s]
                pokemon = kanto_dex_names[dex_index]
                factor = self.petitcup_trainer_factor
                level = petitcupr1_levels[_][s]
                self.write_pokemon_bytes(patch, offset, dex_index, pokemon, factor, level)

                offset += 25  # Seek forward by 25 bytes
            offset += 56  # Seek forward by 56 bytes
        offset += 16  # Seek forward by 16 bytes


    def randomize_pikacup_trainer_pokemon_round1(self, patch) -> None:
        offset = rom_offsets[self.version]["PikaCup_Round1"]
        team_count = 8
        for _ in range(team_count):
            new_team = random.sample(pika_cup_indexes, 6)
            for s in range(6):
                dex_index = new_team[s]
                pokemon = kanto_dex_names[dex_index]
                factor = self.pikacup_trainer_factor
                level = pikacupr1_levels[_][s]
                self.write_pokemon_bytes(patch, offset, dex_index, pokemon, factor, level)

                offset += 25  # Seek forward by 25 bytes
            offset += 56  # Seek forward by 56 bytes
        offset += 16  # Seek forward by 16 bytes


    def write_rental_pokemon_bytes(self, patch, offset, index, factor, level) -> None:
        offset += 9

        # Random moveset
        bst_list = self.bst_list[index]
        type_bytes = bytes.fromhex(kanto_dex_names[index]["type"])
        new_attacks = randomMovesetGenerator.MovesetGenerator.get_random_moveset(bst_list, factor, type_bytes)
        for attack in new_attacks:
            patch.write_token(APTokenTypes.WRITE, offset, bytes([attack]))
            offset += 1

        offset += 4

        growth_rate = kanto_dex_names[index]["gr"]
        exp_for_level = growth_rates[growth_rate][level]
        exp_bytes = int.to_bytes(int(exp_for_level), 3, "big")
        patch.write_token(APTokenTypes.WRITE, offset, exp_bytes)
        offset += 3

        for k in range(5):
            ev = int.to_bytes(self.evs[index][k], 2, "big")
            patch.write_token(APTokenTypes.WRITE, offset, bytes(ev))
            offset += 2

        ivs_bytes = bytes.fromhex(self.ivs[index])
        patch.write_token(APTokenTypes.WRITE, offset, ivs_bytes)
        offset += len(ivs_bytes)

        offset += 6

        stats = self.new_display_stats[index]
        evs = self.evs[index]
        ivs = self.ivs[index]
        disp = writeDisplayData.DisplayDataWriter.write_gym_tower_display(stats, evs, ivs, level)
        patch.write_token(APTokenTypes.WRITE, offset, bytes(disp))
        offset += len(disp)

        offset += 36


    def randomize_glc_rentals_round1(self, patch) -> None:
        offset = rom_offsets[self.version]["Rentals_GymCastle_Round1"] + 4
        factor = self.glc_rental_factor

        glc_indexes = list(range(149))
        if self.rental_list_shuffle_factor == 2 or self.rls_glc_factor > 1:
            random.shuffle(glc_indexes)

        for index in glc_indexes:
            self.write_rental_pokemon_bytes(patch, offset, index, factor, 50)


    def randomize_pokecup_rentals(self, patch) -> None:
        offset = rom_offsets[self.version]["Rentals_PokeCup"] + 4
        factor = self.pokecup_rental_factor

        pokecup_indexes = list(range(149))
        if self.rental_list_shuffle_factor == 2 or self.rls_poke_factor > 1:
            random.shuffle(pokecup_indexes)

        for index in pokecup_indexes:
            self.write_rental_pokemon_bytes(patch, offset, index, factor, 50)


    def randomize_primecup_rentals_round1(self, patch) -> None:
        offset = rom_offsets[self.version]["Rentals_PrimeCup_Round1"] + 4
        factor = self.primecup_rental_factor

        prime_cup_indexes = list(range(149))
        if self.rental_list_shuffle_factor == 2 or self.rls_prime_factor > 1:
            random.shuffle(prime_cup_indexes)

        for index in prime_cup_indexes:
            self.write_rental_pokemon_bytes(patch, offset, index, factor, 100)


    def randomize_petitcup_rentals(self, patch) -> None:
        offset = rom_offsets[self.version]["Rentals_PetitCup"] + 4
        factor = self.petitcup_rental_factor

        if self.rental_list_shuffle_factor == 2 or self.rls_petit_factor > 1:
            random.shuffle(petit_cup_indexes)

        for index in petit_cup_indexes:
            self.write_rental_pokemon_bytes(patch, offset, index, factor, 25)


    def randomize_pikacup_rentals(self, patch) -> None:
        offset = rom_offsets[self.version]["Rentals_PikaCup"] + 4
        factor = self.pikacup_rental_factor

        if self.rental_list_shuffle_factor == 2 or self.rls_pika_factor > 1:
            random.shuffle(pika_cup_indexes)

        for index in pika_cup_indexes:
            self.write_rental_pokemon_bytes(patch, offset, index, factor, 15)
