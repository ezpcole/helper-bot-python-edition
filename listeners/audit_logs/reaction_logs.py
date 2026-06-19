###############################################
#
# File: listeners.audit_logs.reaction_logs
# Date: 29/04/2026 (EU)
# Date Edited: 07/05/2026 (EU)
# Purpose:
#  
# Author: snow2code
#
###############################################


import discord
from discord.ext import commands
from utils.discordbot import Bot
from utils.semifunc import SemiFunc
from datetime import datetime

class ReactionLogs(commands.Cog):
    def __init__(self, bot):
        self.bot: Bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: discord.RawReactionActionEvent):
        # Ignore #selfroles and #verify
        if payload.channel_id == 1418954294656499773 or payload.channel_id == 1419037577280880804:
            return
        
        # None replacements
        channel = self.bot.get_channel(payload.channel_id)
        message: discord.Message = await channel.fetch_message(payload.message_id)

        payload.member = self.bot.get_user(payload.user_id)
        payload.message_author_id = message.author.id


        logs = self.bot.get_channel(1501753222270943252)

        thread_exists = False
        thread: discord.Thread = None

        for thread_ in logs.threads:
            if thread_.name.find(str(payload.member.id)) >= 0:
                thread_exists = True
                thread = thread_

                # await thread.add_user(self.bot.user)


        embed = self.bot.create_embed_notitle(color=discord.Color.red())
        message = f"https://discord.com/channels/{payload.guild_id}/{payload.channel_id}/{payload.message_id}"
            
        embed.description = f"**Reaction added to {message}**"
        embed.add_field(name="emoji:",value=f"```{payload.emoji}```",inline=False)
            
        embed.timestamp = datetime.utcnow()
        if payload.member:
            embed.set_author(name=payload.member.name, icon_url=payload.member.avatar)
        embed.set_footer(text=f"Author: {payload.message_author_id} | Message ID: {payload.message_id}")


        if thread_exists:
            await thread.send(embed=embed)
        else:
            name = f"{payload.user_id} ({payload.member.name})"
            
            thread = await logs.create_thread(
                name=name,
                auto_archive_duration=10080,
                type=discord.ChannelType.public_thread
            )

            await thread.send(embed=embed)
            # await logs.send(f"{payload.member.name} ({payload.member.id}) - {thread.mention}")
    
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload: discord.RawReactionActionEvent):
        # Ignore #selfroles and #verify
        if payload.channel_id == 1418954294656499773 or payload.channel_id == 1419037577280880804:
            return
        
        # None replacements
        channel = self.bot.get_channel(payload.channel_id)
        message: discord.Message = await channel.fetch_message(payload.message_id)

        payload.member = self.bot.get_user(payload.user_id)
        payload.message_author_id = message.author.id


        logs = self.bot.get_channel(1501753222270943252)

        thread_exists = False
        thread: discord.Thread = None

        for thread_ in logs.threads:
            if thread_.name.find(str(payload.member.id)) >= 0:
                thread_exists = True
                thread = thread_

                # await thread.add_user(self.bot.user)


        embed = self.bot.create_embed_notitle(color=discord.Color.red())
        message = f"https://discord.com/channels/{payload.guild_id}/{payload.channel_id}/{payload.message_id}"
            
        embed.description = f"**Reaction removed from {message}**"
        embed.add_field(name="emoji:",value=f"```{payload.emoji}```",inline=False)
            
        embed.timestamp = datetime.utcnow()
        if payload.member:
            embed.set_author(name=payload.member.name, icon_url=payload.member.avatar)
        embed.set_footer(text=f"Author: {payload.message_author_id} | Message ID: {payload.message_id}")


        if thread_exists:
            await thread.send(embed=embed)
        else:
            name = f"{payload.user_id} ({payload.member.name})"

            thread = await logs.create_thread(
                name=name,
                auto_archive_duration=10080,
                type=discord.ChannelType.public_thread
            )
            
            await thread.send(embed=embed)
            # await logs.send(f"{payload.member.name} ({payload.member.id}) - {thread.mention}")

async def setup(bot):
    await bot.add_cog(ReactionLogs(bot))
