from Options import Choice, Toggle

class Goal(Choice):
    """
    Determines what your goal is to consider the game beaten.

    - Castle: Clear Gym Leader Castle by defeating Gary
    """
    display_name = "Goal"
    default = 0
    option_castle = 0

class RemoteItems(Toggle):
    """
    Instead of placing your own items directly into the ROM, all items are received from the server, including items you find for yourself.

    This enables co-op of a single slot and recovering more items after a lost save file (if you're so unlucky).

    But it changes pickup behavior slightly and requires connection to the server to receive any items.
    """
    display_name = "Remote Items"
