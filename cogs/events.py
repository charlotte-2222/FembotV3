import asyncio
import random
from datetime import datetime
import time

import discord
from discord.ext import tasks, commands


class EventsCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("Fembot online\n")
        print(f"Logged in as {self.bot.user} - {self.bot.user.id}\n")
        print("--------------")
        print(time.strftime(f"Time at start:\n"
                            "%H:%M:%S\n"
                            "%m/%d/%Y\n"))

        while True:
            await self.bot.change_presence(
                activity=discord.Activity(type=discord.ActivityType.watching, name="the downfall of humanity"))
            await asyncio.sleep(45)
            await self.bot.change_presence(status=discord.Status.online, activity=discord.Game('with code'))
            await asyncio.sleep(45)
            await self.bot.change_presence(
                activity=discord.Activity(type=discord.ActivityType.watching, name="you..."))
            await asyncio.sleep(45)
            await self.bot.change_presence(
                activity=discord.Activity(type=discord.ActivityType.streaming, name="deez nuts"))
            await asyncio.sleep(45)
            await self.bot.change_presence(status=discord.Status.online,
                                           activity=discord.Game("breakfastclub.my.pebble.host"))
            await asyncio.sleep(45)
            await self.bot.change_presence(
                activity=discord.Activity(type=discord.ActivityType.watching, name="for help"))
            await asyncio.sleep(45)

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        a = ['A champion has appeared!',
             'Welcome to the club...',
             'The Eggs Have Expected You',
             'Ah yes, finally',
             "wait...you're here?",
             'oh no, more weirdos',
             'Prepare for cringe',
             "Make yourself at home",
             "Welcome! Don't lick the floor",
             "eeeeeeee",
             "~insect-like chattering~",
             "But what of the droid attack on the wookies?",
             "Do you have pizza?",
             "This is not a Wendy's",
             "If you're looking for Femboys, ohhh boi~",
             "~insert heartwarming welcome message here~"]
        b = random.choice(a)
        if member.bot:
            return  # ignore all bots
        print("\n--------------\n")
        print(time.strftime(f"{member} joined at:\n" + "%H:%M:%S\n"))
        welEmb = discord.Embed(title=f'{b}',
                               url="https://docs.google.com/document/d/1YTSSADP1NDr310eKNQJNfy-yWwgoRjdTOkBffzIMgD4/edit?usp=sharing",
                               description=f"Welcome to the server, {member.mention}!\n"
                                           "We're happy to add you to our little home\n"
                                           ":egg: :bread: :bacon:"
                               , timestamp=datetime.utcnow())
        welEmb.set_thumbnail(url=member.avatar_url)
        welEmb.set_footer(text="Click the link and read our ToS!")
        welEmb.color = discord.Color.random()
        wel_cum = self.bot.get_channel(698670684154363904)

        await wel_cum.send(embed=welEmb)



        await asyncio.sleep(30)

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):

        def format_date(dt):
            if dt is None:
                return 'N/A'
            return f'{dt:%A %d, %B %Y • %I:%M %p}'

        try:
            bitchChannel = self.bot.get_channel(806720572100444181)
            print("\n--------------\n")
            print(time.strftime(f"Member ({member.id}) left at:\n" + "%H:%M:%S\n"))
            bitch = discord.Embed(title="User Left:", description='', timestamp=datetime.utcnow())
            bitch.add_field(name="User Info", value=f"User: {member}\nID: {member.id}")
            bitch.set_thumbnail(url=member.avatar_url)
            bitch.add_field(name='Joined', value=format_date(getattr(member, 'joined_at', None)), inline=False)

            await bitchChannel.send(embed=bitch)
        except:
            bitchChannel = self.bot.get_channel(806720572100444181)
            print("\n--------------\n")
            print(time.strftime(f"Member ({member.id}) left at:\n" + "%H:%M:%S\n"))
            bitch = discord.Embed(title="User Left:", description='', timestamp=datetime.utcnow())
            bitch.add_field(name="User Info",
                            value=f"had a weird name, so here is an ID.\nID: {member.id}")
            bitch.color = discord.Color.magenta()
            await bitchChannel.send(embed=bitch)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        errorEm = discord.Embed(title="uwu Uh oh!",
                                description="OOPSIE WOOPSIE!! Uwu We make a fucky wucky!! A wittle fucko boingo! The "
                                            "code monkeys at our headquarters are working VEWY HAWD to fix this!",
                                colour=discord.Colour.magenta())
        errorEm.set_thumbnail(url=self.bot.user.avatar_url)
        errorEm.add_field(name="Error: ", value=error)
        errorEm.set_footer(text="uwu use tha hwelp cummand")
        if isinstance(error, discord.ext.commands.MemberNotFound):
            await ctx.send(embed=errorEm)
        elif isinstance(error, commands.BadArgument):
            await ctx.send(embed=errorEm)
        elif isinstance(error, commands.CommandNotFound):
            return
        else:
            await ctx.send(embed=errorEm)


def setup(bot):
    bot.add_cog(EventsCog(bot))
