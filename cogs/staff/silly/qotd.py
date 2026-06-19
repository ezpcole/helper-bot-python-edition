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
    def __init__(self, bot):
        self.bot: Bot = bot

    @commands.guild_only()
    @commands.hybrid_command(name="qotd")
    async def qotd(self, ctx: Context, qotd_msg: str):
        """
        qotd
        
        Parameters
        ----------
        ctx: Context
            The context of the command invocation
        qotd_msg:
            The question
        """
        if SemiFunc.command_disabled(ctx):
            await ctx.reply("That command is currently disabled.")
            return
        
        if not SemiFunc.can_use_command(ctx, ctx.author, "staff"):
            await ctx.reply("That command is staff only.")
            return
        
        # should be self.bot, eza lmao
        # i understand though, as you haven't done anything with discord.py

        # ALSO, could be better with the channel id, and role id.. for now we're just testing, so it's fine for now.
        qotd_channel = self.bot.get_channel(1517294723679650047)
        general_channel = self.bot.get_channel(1414222708324958385)
        qotd_role = self.bot.get_role(1511978917890621531)

        # snowy: for testing
        testing = True
        if testing:
            channel =
            if qotd_channel:
                # snowy: added comment for command to opt out instead.. as some don't have self roles visible
                qotd_channel.send(f"{qotd_role.mention}\nA new Question of the Day has arrived: {qotd_msg}\nPut your answers in {general_channel.mention}\n-# opt out of this through self roles or with ?pingoptout qotd in bot commands...if you really want to")
        else:

        await SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction, ctx)

async def setup(bot):
    await bot.add_cog(qotd(bot))
