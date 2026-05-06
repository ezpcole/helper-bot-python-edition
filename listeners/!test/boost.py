###############################################
#
# File: testing.listeners.boost
# Date: 06/05/2026 (EU)
# Date Edited: 06/05/2026 (EU)
# Purpose:
#  
# Author: snow2code
#
###############################################


import discord

from datetime import datetime
from discord.ext import commands
from utils.discordbot import Bot
from utils.semifunc import SemiFunc

class TestBoost(commands.Cog):
    def __init__(self, bot):
        self.bot: Bot = bot

    @commands.Cog.listener()
    async def on_message(self, msg: discord.Message):
        # 13/03/2026 - Bugfix: DMs can cause some issues.
        if not isinstance(msg.channel, discord.DMChannel):
            if msg.author.bot == False:
                print("Meow!")
            pass

async def setup(bot):
    await bot.add_cog(TestBoost(bot))