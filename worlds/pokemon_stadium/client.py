import asyncio

from typing import TYPE_CHECKING, Optional, Set

import Utils
import worlds._bizhawk as bizhawk
from worlds._bizhawk.client import BizHawkClient

from .data import data
from .options import Goal, RemoteItems

if TYPE_CHECKING:
    from worlds._bizhawk.context import BizHawkClientContext

EXPECTED_ROM_NAME = "pokemon stadium / AP 5"

COMPLETED_CASTLE_FLAG = data.constants["COMPLETED_CASTLE_FLAG"]

class PokemonStadiumClient(BizHawkClient):
    game = "Pokémon Stadium"
    system = "N64"
    patch_suffix = ".apstadium"

    local_checked_locations: Set[int]
    goal_flag: Optional[int]

    def initialize_client(self):
        self.local_checked_locations = set()
        self.goal_flag = None
    
    async def validate_rom(self, ctx: "BizHawkClientContext") -> bool:
        from CommonClient import logger

        try:
            # Check ROM name/patch version
            rom_name_bytes = ((await bizhawk.read(ctx.bizhawk_ctx, [(0x108, 32, "ROM")]))[0])
            rom_name = bytes([byte for byte in rom_name_bytes if byte != 0]).decode("ascii")
            if not rom_name.startswith("pokemon stadium"):
                return False
            if rom_name == "pokemon stadium":
                logger.info("ERROR: You appear to be running an unpatched version of Pokémon Stadium. "
                            "You need to generate a patch file and use it to create a patched ROM.")
                return False
            if rom_name != EXPECTED_ROM_NAME:
                logger.info("ERROR: The patch file used to create this ROM is not compatible with "
                            "this client. Double check your client version against the version being "
                            "used by the generator.")
                return False
        except UnicodeDecodeError:
            return False
        except bizhawk.RequestFailedError:
            return False  # Should verify on the next pass

        ctx.game = self.game
        ctx.items_handling = 0b001
        ctx.want_slot_data = True
        ctx.watcher_timeout = 0.125

        self.initialize_client()

        return True
    
    async def set_auth(self, ctx: "BizHawkClientContext") -> None:
        import base64
        auth_raw = (await bizhawk.read(ctx.bizhawk_ctx, [(data.rom_addresses["gArchipelagoInfo"], 16, "ROM")]))[0]
        ctx.auth = base64.b64encode(auth_raw).decode("utf-8")
    
    async def game_watcher(self, ctx: "BizHawkClientContext") -> None:
        if ctx.server is None or ctx.server.socket.closed or ctx.slot_data is None:
            return
        
        if ctx.slot_data["goal"] == Goal.option_castle:
            self.goal_flag = COMPLETED_CASTLE_FLAG
        
        if ctx.slot_data["remote_items"] == RemoteItems.option_true and not ctx.items_handling & 0b010:
            ctx.items_handling = 0b011
            Utils.async_start(ctx.send_msgs([{
                "cmd": "ConnectUpdate",
                "items_handling": ctx.items_handling
            }]))

            # Need to make sure items handling updates and we get the correct list of received items
            # before continuing. Otherwise we might give some duplicate items and skip others.
            # Should patch remote_items option value into the ROM in the future to guarantee we get the
            # right item list before entering this part of the code
            await asyncio.sleep(0.75)
            return
