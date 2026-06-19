###############################################
#
# File: cogs.users.misc.pingoptout
# Date: 30/04/2026 (EU)
# Date Edited: 04/06/2026 (EU)
# Purpose: 
#  
# Author: snow2code
#
###############################################


from discord import app_commands
from discord.ext import commands
from discord.errors import *
from utils.discordbot import Bot
from utils.custom.context import Context
from utils.database import Database

class UserCommands__Misc__Pingoptout(commands.Cog):
    def __init__(self, bot):
        self.bot: Bot = bot
    
    @commands.guild_only()
    @commands.hybrid_command(name="pingoptout")
    @app_commands.allowed_installs(guilds=True, users=False)
    @app_commands.allowed_contexts(guilds=True, dms=True, private_channels=False)
    async def pingoptout(self, ctx: Context, type: str):
        """
        Opt out of either:
        random hug or boop pings from the bot
        QOTD pings
        
        Parameters
        ----------
        ctx: Context
            The context of the command invocation
        type: str
            The type of ping (random, qotd)
        """
        
        user = ctx.author

        if type.lower() == "qotd":
            qotd_role = ctx.guild.get_role(1511978917890621531)
            if user.get_role(1511978917890621531):
                await user.remove_roles(qotd_role)
                await ctx.reply("You've opted out of Question of the Day pings successfully.")
            else:
                await user.add_roles(qotd_role)
                await ctx.reply("You've opted in to Question of the Day pings successfully.")
        elif type.lower() == "random":
            allowed = Database.allow_ping(user.id)

            if allowed == True:
                Database.userdata_conn.execute(f'UPDATE pings SET allowed=? WHERE user_id=?', (0, user.id))
                Database.userdata_conn.commit()
                await ctx.reply("You've opted out of boop and hug pings successfully.")
            else:
                Database.userdata_conn.execute(f'UPDATE pings SET allowed=? WHERE user_id=?', (1, user.id))
                Database.userdata_conn.commit()
                await ctx.reply("You've opted in to boop and hug pings successfully.")
        else:
            await ctx.reply("Bad paramater. Types of pings to opt out of:\nQOTD (Question of the Day Role Ping)\nRandom (Random hug and Boop pings)")
        
async def setup(bot):
    await bot.add_cog(UserCommands__Misc__Pingoptout(bot))
