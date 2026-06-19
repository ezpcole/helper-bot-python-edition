###############################################
#
# File: listeners.on__ready.random_hug_boop
# Date: 30/04/2026
# Date Edited: 03/05/2026 (EU)
# Purpose:
#  
# Author: snow2code
#
###############################################


import random
import discord
import asyncio

from discord.ext import commands
from utils.discordbot import Bot
from utils.files import files
from utils.semifunc import SemiFunc
from utils.database import Database

class RandomHugBoop(commands.Cog):
    def __init__(self, bot):
        self.bot: Bot = bot
        self.randomly_huggin_var = False

    @commands.Cog.listener()
    async def on_ready(self):
        if self.randomly_huggin_var == False:
            self.randomly_huggin_var = True
            self.bot.loop.create_task(self.randomly_huggin())

    async def randomly_huggin(self):
        bot = self.bot
        config = files._bot_config()
        await bot.wait_until_ready()

        while not bot.is_closed():
            await asyncio.sleep(7200) # Final
            # await asyncio.sleep(3600) # Final
            # await asyncio.sleep(5) # Testing time
            
            # guild = bot.get_guild( config['test_server_id'] )
            guild = bot.get_guild( config['main_server_id'] )

            members = []

            # 02/05/2024, snowy: Other code didn't work out...
            for member in guild.members:
                if member.bot:
                    continue

                if Database.allow_ping(member.id) == False:
                    continue

                # Let's be respectable. If using offline, invisible or DND status, reroll
                if member.status in [discord.Status.offline, discord.Status.invisible, discord.Status.dnd]:
                    continue

                members.append(member)

            # 14/05/2026 (EU) snow2code: We should probably not have two latest messages be him hugging or booping
            await self.send(members)

    async def send(self, members: list[discord.Member]):
        # 14/05/2026 (EU) snow2code: We should probably not have two latest messages be him hugging or booping
        random_member = random.choice(members)
        choice = random.choice(["hug", "boop"])

        channel_id = 1414222708324958385
        guild = self.bot.get_guild( files._bot_config()['main_server_id'] )

        if self.bot.user.id == files._bot_config()['test_bot_id']:
            guild = self.bot.get_guild(1480087423433052242)
            channel_id = 1501656987761643551

        channel = guild.get_channel(channel_id)

        if channel.last_message == None:
            await channel.send(f"{random_member.mention} ***{choice}***\n-# Opt out of this with ?pingoptout or /pingoptout in <#1477493580061741156>")
        else:
            if channel.last_message.author.id not in [files._bot_config()['main_bot_id'], files._bot_config()['test_bot_id']]:
                await channel.send(f"{random_member.mention} ***{choice}***\n-# Opt out of this with ?pingoptout or /pingoptout in <#1477493580061741156>")

async def setup(bot):
    await bot.add_cog(RandomHugBoop(bot))
