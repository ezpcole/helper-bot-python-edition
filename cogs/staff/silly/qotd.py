###############################################
#
# File: cogs.staff.silly.qotd
# Date: 6/18/2026 (NAW)
# Date Edited: 6/18/2026 (NAW)
# Purpose: question of the day
#  
# Author: e4za
#
###############################################


import discord

from discord.ext import commands
from utils.custom.context import Context
from utils.discordbot import Bot
from utils.semifunc import SemiFunc

class qotd(commands.Cog):
    
    await SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction, ctx)



async def setup(bot):
    await bot.add_cog(qotd(bot))
