from copy import deepcopy
import random
from typing import List

from .constants import (
    modifier_sums,
    kanto_attacks,
)


class MovesetGenerator:
    @staticmethod
    def get_random_moveset_and_modifiers(bst: int, seed=None) -> List[int]:
        if seed is not None:
            random.seed(seed)

        min_bst = int(bst - 25 / 1.52)
        max_bst = int(bst + 25 / 0.66)
        random_bst = random.randint(min_bst, max_bst)

        modifier_sum = (random_bst / bst) * 4
        closest_key = min(modifier_sums.keys(), key=lambda k: abs(k - modifier_sum))
        modifiers = random.choice(modifier_sums[closest_key])

        new_attacks = []
        for modifier in modifiers:
            possible_attacks = deepcopy(kanto_attacks[modifier])

            while True:
                new_attack = random.choice(possible_attacks)

                if new_attack not in new_attacks:
                    new_attacks.append(new_attack)
                    break
                else:
                    possible_attacks.remove(new_attack)

        return new_attacks, modifiers
