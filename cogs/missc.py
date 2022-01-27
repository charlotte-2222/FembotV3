
import random

import discord
from discord.ext import commands
from datetime import datetime

currentDT = datetime.utcnow()
print(str(currentDT.year) + ", " + str(currentDT.month) + ", " + str(currentDT.day) + ", " + str(
    currentDT.hour) + ", " + str(currentDT.minute) + ", " + str(currentDT.second))


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Function for adding new timer

    # @commands.command(help="Report a fellow member for misconduct")
    # async def report(self, ctx, user: discord.Member, *reason):
    #     channel = self.bot(694637172271087749)  # since it's a cog u need self.bot
    #     author = ctx.message.author
    #     rearray = ' '.join(reason[:])  # converts reason argument array to string
    #     if not rearray:  # what to do if there is no reason specified
    #         await channel.send(f"{author} has reported {user}, reason unspecified")
    #         await ctx.author.send(f"You reported {user} without a specified reason")
    #         await ctx.message.delete()  # I would get rid of the command input
    #     else:
    #         await channel.send(f"{author} has reported {user}.\nReason: {rearray}")
    #         await ctx.author.send(f"You reported {user}\nReason for report for: {rearray}")
    #         await ctx.message.delete()

    @commands.command(help="This command will return which staff member is online, and their online status.",
                      pass_context=True,
                      aliases=['helpers'])
    async def staff(self, ctx):
        if ctx.guild.id != 694631281346084925:
            return
        online = []
        offline = []
        idle = []
        dnd = []
        staff = [i for i in ctx.guild.members if not i.bot and
                 694709812528677008 in [r.id for r in i.roles]]
        helpers = [i for i in ctx.guild.members if not i.bot and
                   914546242850271285 in [r.id for r in i.roles]]

        for i in staff:
            if i.status == discord.Status.online: online.append(
                f'**{i.name[0:1]}\u200b{i.name[1:len(i.name)]}**#{i.discriminator}')
            if i.status == discord.Status.offline: offline.append(
                f'**{i.name[0:1]}\u200b{i.name[1:len(i.name)]}**#{i.discriminator}')
            if i.status == discord.Status.idle: idle.append(
                f'**{i.name[0:1]}\u200b{i.name[1:len(i.name)]}**#{i.discriminator}')
            if i.status == discord.Status.dnd: dnd.append(
                f'**{i.name[0:1]}\u200b{i.name[1:len(i.name)]}**#{i.discriminator}')

        for i in helpers:
            if i.status == discord.Status.online: online.append(
                f'**{i.name[0:1]}\u200b{i.name[1:len(i.name)]}**#{i.discriminator}')
            if i.status == discord.Status.offline: offline.append(
                f'**{i.name[0:1]}\u200b{i.name[1:len(i.name)]}**#{i.discriminator}')
            if i.status == discord.Status.idle: idle.append(
                f'**{i.name[0:1]}\u200b{i.name[1:len(i.name)]}**#{i.discriminator}')
            if i.status == discord.Status.dnd: dnd.append(
                f'**{i.name[0:1]}\u200b{i.name[1:len(i.name)]}**#{i.discriminator}')
        e = discord.Embed(title=f"{ctx.guild} Staff!",
                          description="DM these people if you need help",
                          colour=discord.Colour.random(),
                          timestamp=datetime.utcnow())
        e.add_field(name=":green_circle:", value=f"{' | '.join(online) if online != [] else 'None'}", inline=False)
        e.add_field(name=":orange_circle:", value=f"{' | '.join(idle) if idle != [] else 'None'}", inline=False)
        e.add_field(name=":red_circle:", value=f"{' | '.join(dnd) if dnd != [] else 'None'}", inline=False)
        e.add_field(name=":zzz:", value=f"{' | '.join(offline) if offline != [] else 'None'}", inline=False)
        e.set_thumbnail(url=ctx.guild.icon_url_as(size=1024, format=None, static_format="png"))
        await ctx.send(embed=e)

    @commands.command(aliases=["ping", "p"],
                      help="Shows the bot latency from the discord websocket.")
    async def pping(self, ctx):
        e = discord.Embed(title="PP",
                          description=f"Your pp lasted `{self.bot.latency * 1000:.2f}ms`")
        await ctx.send(embed=e)

    @commands.command(help="Chooses between multiple choices.To denote multiple choices,you should use double quotes.",
                      pass_context=True)
    async def choose(self, ctx, *choices: commands.clean_content):
        if len(choices) < 2:
            return await ctx.send('Not enough choices to pick from.')

        await ctx.send(random.choice(choices))



def setup(bot):
    bot.add_cog(Misc(bot))
