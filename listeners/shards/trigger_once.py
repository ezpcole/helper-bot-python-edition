###############################################
#
# File: listeners.shards.trigger_once
# Date: 06/05/2026 (EU)
# Date Edited: 06/05/2026 (EU)
# Purpose: Have shards trigger once.
#  just to be safe. they are called however
#  many shards there is that many times
#  ..so
#  
# Author: snow2code
#
###############################################


from discord.ext import commands
from utils.discordbot import Bot


class Shards(commands.Cog):
    def __init__(self, bot):
        self.bot: Bot = bot
        self.shards_triggered = set()

    @commands.Cog.listener()
    async def on_shard_ready(self, shard_id):
        pass

        # if shard_id not in self.shards_triggered:
        #     print(f"shard {shard_id} is ready")
        #     self.shards_triggered.add(shard_id)
        # else:
        #     print(f"shard {shard_id} was triggered already")

async def setup(bot):
    await bot.add_cog(Shards(bot))
