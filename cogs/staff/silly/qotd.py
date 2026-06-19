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
        
        await SemiFunc.log_command_use(self.bot, ctx.author, ctx.message.content, ctx.interaction, ctx)
        
        qotd_role = ctx.guild.get_role(1511978917890621531)

        # snowy: for testing
        testing = False
        channel = ctx.guild.get_channel(1414222708324958385)
        if testing:
            # Test
            channel = ctx.guild.get_channel(1517294723679650047)
        else:
            # Gen
            channel = ctx.guild.get_channel(1414222708324958385)

        # snowy: added comment for command to opt out instead.. as some don't have self roles visible
        channel.send(f"{qotd_role.mention}\nA new Question of the Day has arrived: {qotd_msg}\nPut your answers in {channel.mention}\n-# opt out of this through self roles or with ?pingoptout qotd in bot commands...if you really want to")


async def setup(bot):
    await bot.add_cog(qotd(bot))
