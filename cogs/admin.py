import asyncio
import sys
from datetime import datetime

import discord
from discord.ext import commands


class AdminCog(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help='Changes your nickname.',
                      aliases=['nick'])
    @commands.has_guild_permissions(kick_members=True)
    async def nickname(self, ctx, member: discord.Member, *, nick=""):
        nickname = ''.join(nick)
        await member.edit(nick=nickname
                          )
        await ctx.send(f'Nickname changed for {member.mention}.')

    @commands.command(help="Admin only - Deletes messages")
    @commands.has_guild_permissions(kick_members=True)
    async def purge(self, ctx, limit: int):
        await ctx.channel.purge(limit=limit + 1)
        await asyncio.sleep(2)
        await ctx.send('Cleared by this guy: {}'.format(ctx.author.mention))

    @commands.command(help="Kicks members at will", pass_context=True)
    @commands.has_guild_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member, *reason):
        rearray = ' '.join(reason[:])
        log = self.bot.get_channel(843568644373741598)
        ban_kick = self.bot.get_channel(749362181782503455)
        await ctx.guild.kick(user=member)
        if not rearray:
            embed = discord.Embed(title=f":skull_crossbones: A member was kicked :skull_crossbones:",
                                  description=f"Member: {member}",
                                  timestamp=datetime.utcnow(),
                                    colour=discord.Color.magenta())
            embed.set_thumbnail(url=member.avatar_url)
            await log.send(embed=embed)
            await ctx.reply(f'{member.mention} is on the receiving end of "mod abuse" lmao')
        else:
            ed = discord.Embed(title=f":skull_crossbones: A member was kicked :skull_crossbones:",
                               description=f"{member}",
                               timestamp=datetime.utcnow(),
                               colour=discord.Color.magenta())
            ed.add_field(name="Reason",
                         value=f"{rearray}")
            ed.set_thumbnail(url=member.avatar_url)
            await log.send(embed=ed)
            await ctx.reply(f'{member.mention} is on the receiving end of "mod abuse" lmao')

    @commands.command(help="unban members who were previously bad",
                      pass_context=True)
    @commands.has_guild_permissions(ban_members=True)
    async def unban(self, ctx, member):
        await ctx.guild.unban(discord.Object(id=member))
        await ctx.reply(f"Member Unbanned :white_check_mark:")

    @commands.command(help="Ban a bad person", pass_context=True)
    @commands.has_guild_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member, *reason):
        rearray = ' '.join(reason[:])
        await ctx.guild.ban(user=member)
        log = self.bot.get_channel(843568644373741598)
        if not rearray:
            e1 = discord.Embed(title=f":bangbang: A member was banned :bangbang:",
                               description='',
                               timestamp=datetime.utcnow(),
                               colour=discord.Color.magenta())
            e1.add_field(name="Member:",
                         value=f"{member}\n"
                               f"ID: {member.id}\n"
                               f"*No Reason Specified For Ban*")
            e1.set_thumbnail(url=member.avatar_url)
            await log.send(embed=e1)
            await ctx.reply(f'{member.mention} is on the receiving end of "mod abuse" lmao')
        else:
            e2 = discord.Embed(title=f":bangbang: A member was banned :bangbang:",
                               description='',
                               timestamp=datetime.utcnow(),
                               colour=discord.Color.magenta())
            e2.add_field(name="Member:",
                         value=f"{member}\n"
                               f"ID: {member.id}\n")
            e2.add_field(name=f"Reason:",
                         value=f"{rearray}")

            e2.set_thumbnail(url=member.avatar_url)
            await log.send(embed=e2)
            await ctx.reply(f'{member.mention} is on the receiving end of "mod abuse" lmao')

    @commands.command(aliases=["mban"], usage="[member] (reason)", help="Ban multiple member at once")
    @commands.cooldown(1, 180, commands.BucketType.guild)
    @commands.has_permissions(ban_members=True)
    async def massban(self, ctx, members: commands.Greedy[int], *, reason=f"Massban - No reason provided"):
        msg = await ctx.send(f"Banning `{len(members)}` user(s)...\nEstimated Time, {len(members)} Seconds")
        thing = 0
        l = []
        for member in members:
            if member in ctx.guild.members:
                mem = ctx.guild.get_member(member)
                if mem.top_role.position > ctx.author.top_role.position:
                    return
            try:
                await ctx.guild.ban(discord.Object(id=member), reason=f"{ctx.author}: {reason}")
                await asyncio.sleep(1)
                l.append(str(member))
                thing += 1
            except:
                pass
            await msg.edit(content=f"{msg.content}\n\n:white_check_mark: They Gone. lmao")

    @commands.command(help="Create warnings against members",
                      aliases=["warn", "slap", "whip"], pass_context=True)
    @commands.has_guild_permissions(kick_members=True)
    async def warn_create(self, ctx, member: discord.Member, *args):
        log = self.bot.get_channel(843568644373741598)
        reason = " ".join(args)
        embed = discord.Embed(title="User Warned!",
                              description=f"**{member}** was warned by **{ctx.message.author}**!",
                              color=discord.Color.magenta())
        embed.add_field(name="Reason:", value=reason)
        await log.send(embed=embed)
        await ctx.message.delete()
        await member.send(f"You were warned by **{ctx.message.author}**!\nReason: {reason}")

    @commands.command(aliases=["sm", "slowmo"])
    @commands.has_permissions(administrator=True)
    async def slowmode(self, ctx, time=None):
        if time == None:
            await ctx.send(f"this channel's slowmode is **`{ctx.channel.slowmode_delay}`**")
        else:
            await ctx.channel.edit(slowmode_delay=time)
            await ctx.send(f"I changed the slowmode to **`{time}`**")


def setup(bot):
    bot.add_cog(AdminCog(bot))
