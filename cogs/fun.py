import asyncio
import time
from typing import Union

import aiohttp
import discord
import requests
from discord.ext import commands

from imgurpython import ImgurClient
from utilityFunction.config import *
from utilityFunction import lists
from utilityFunction.CommandFunc import *
from datetime import datetime

# imgur = ImgurClient(imgurC, ImgurL)


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Measure your friend's dick",
                      aliases=["dick", "penis"],
                      pass_context=True)
    async def dong(self, ctx, user:discord.Member = None):
        """Detects user's dong length"""
        mem = user or ctx.author
        state = random.getstate()
        random.seed(mem)
        dong = "8{}D".format("=" * random.randint(0, 30))
        random.setstate(state)
        girth = random.randint(1, 10)
        girth_cm = 2.54 * girth
        em = discord.Embed(title="How big is your dong?",
                           description='\n',
                           colour=discord.Colour.random())
        em.add_field(name="{}'s Dong Size".format(mem), value="Size: " + dong)
        em.add_field(name="Girth:",
                     value=f"**{girth} inches**\n"
                           f"And for you bastards that use centimeters:\n **{girth_cm} Centimeters**",
                     inline=False)
        await ctx.send(embed=em)

    @commands.command(aliases=['roll'])
    async def roll_die(self, ctx, dice_options: Union[str, int] = 6):
        max_dices = 20
        max_sides = 120

        try:
            dice_options = dice_options.split("d")

            # User gave only sides
            if len(dice_options) == 1:
                sides = int(dice_options[0])
                rolls = 1
            # User gave either RPG dice notation or invalid format
            elif len(dice_options) == 2:
                sides = int(dice_options[1])
                rolls = int(dice_options[0])
            else:
                raise IndexError()
        except AttributeError:
            sides = dice_options
            rolls = 1
        except (ValueError, IndexError):
            await ctx.send("Die info was given in invalid format.")
            return

        if sides > 120:
            await ctx.send(f"The die can only have maximum of {max_sides} sides.")
            return
        elif rolls > max_dices:
            await ctx.send(f"You can throw at most {max_dices} dice at once.")
            return
        elif sides < 1:
            await ctx.send("The die must have at least 1 sides.")
            return
        elif rolls < 1:
            await ctx.send("The die must be thrown at least once.")
            return

        roll_results = [random.randint(1, sides) for _ in range(rolls)]
        if rolls > 1:
            results = ", ".join(str(_int) for _int in roll_results)
            msg = f"{sides}-sided die roll results: `{results}`\n\n:game_die: Total sum: {sum(roll_results)}"
        else:
            msg = roll_results[0]

        await ctx.send(msg)

    @commands.command(help="Lyrics of the cumzone, selected randomly",
                      aliases=["cs"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def cumscript(self, ctx):
        cum = open('text_dir/cumscript.txt').read().splitlines()
        e = discord.Embed(title="<:6291_Anna_lewd:708017347201597501> | Welcome to the cumzone ",
                          description=random.choice(cum),
                          color=discord.Color.magenta(),
                          timestamp=datetime.utcnow())
        e.set_thumbnail(url="https://i.imgur.com/KeJ5hVY.jpg")
        e.set_footer(text="cummy wummies uwu")
        await ctx.send(embed=e)
        await ctx.message.delete()

    @commands.command(help="Lyrics of ram ranch, selected randomly",
                      aliases=["rr"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def ram(self, ctx):
        cum = open('text_dir/ramRanch.txt').read().splitlines()
        e = discord.Embed(title=":cowboy: | Ram Ranch.... ",
                          description=random.choice(cum),
                          color=discord.Color.magenta(),
                          timestamp=datetime.utcnow())
        e.set_thumbnail(url="https://i.imgur.com/RdF7BsM.jpg")
        e.set_footer(text="uwu femboy > cowboy")
        await ctx.send(embed=e)
        await ctx.message.delete()

    @commands.command(help="Find a random cat",
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def cat(self, ctx):
        response = requests.get('https://aws.random.cat/meow').json()
        data = response
        embed = discord.Embed(
            title='🐈',
            description='A random cat, from the interwebs',
            colour=discord.Colour.random()
        )
        embed.set_image(url=data['file'])
        embed.set_footer(text="")
        await ctx.send(embed=embed)

    # @commands.command(help="Find a random dog"
    #     , pass_context=True)
    # @commands.cooldown(1, 3, commands.BucketType.user)
    # async def dog(self, ctx):
    #     r = requests.get(f"https://api.imgur.com/3/gallery/vgW1p/images?client_id={imgurC}").json()
    #     try:
    #         em = discord.Embed(title="The goodest of bois")
    #         indexmax = len(r['data']) - 1
    #         size = random.randrange(0, indexmax, 1)
    #         em.set_image(url=str(r['data'][size]['link']))
    #         em.color = discord.Color.magenta()
    #         await ctx.send(embed=em)
    #         await ctx.message.delete()
    #     except:
    #         await ctx.send(str(r['data'][size]['link']))
    #
    # @commands.command(help="Find a random bird",
    #                   aliases=["bird"],
    #                   pass_context=True)
    # @commands.cooldown(1, 3, commands.BucketType.user)
    # async def birb(self, ctx):
    #     r = requests.get(f"https://api.imgur.com/3/gallery/QWmIV/images?client_id={imgurC}").json()
    #     em = discord.Embed(title="birb")
    #     indexmax = len(r['data']) - 1
    #     size = random.randrange(0, indexmax, 1)
    #     em.set_image(url=str(r['data'][size]['link']))
    #     em.color = discord.Color.magenta()
    #     try:
    #         await ctx.send(embed=em)
    #         await ctx.message.delete()
    #     except:
    #         await ctx.send(str(r['data'][size]['link']))
    #
    # @commands.command(help="Find a random otter",
    #                   pass_context=True)
    # @commands.cooldown(1, 3, commands.BucketType.user)
    # async def otter(self, ctx):
    #     r = requests.get(f"https://api.imgur.com/3/gallery/BZA8d/images?client_id={imgurC}").json()
    #     em = discord.Embed(title="Otters :D")
    #     indexmax = len(r['data']) - 1
    #     size = random.randrange(0, indexmax, 1)
    #     em.set_image(url=str(r['data'][size]['link']))
    #     em.color = discord.Color.magenta()
    #     try:
    #         await ctx.send(embed=em)
    #         await ctx.message.delete()
    #     except:
    #         await ctx.send(str(r['data'][size]['link']))
    #
    # @commands.command(help="Find a random platapuss",
    #                   aliases=["platapussy",
    #                            "platty",
    #                            "platt",
    #                            "plt"],
    #                   pass_context=True)
    # @commands.cooldown(1, 3, commands.BucketType.user)
    # async def plat(self, ctx):
    #     r = requests.get(f"https://api.imgur.com/3/album/kWZ6JNv/images?client_id={imgurC}").json()
    #     em = discord.Embed(title="Platypussssss!!!!!! :D")
    #     indexmax = len(r['data']) - 1
    #     size = random.randrange(0, indexmax, 1)
    #     em.set_image(url=str(r['data'][size]['link']))
    #     em.color = discord.Color.magenta()
    #     try:
    #         await ctx.send(embed=em)
    #         await ctx.message.delete()
    #     except:
    #         await ctx.send(str(r['data'][size]['link']))
    #
    # @commands.command(help="Find some random buns",
    #                   aliases=["rabbit",
    #                            "bunny"],
    #                   pass_context=True)
    # @commands.cooldown(1, 3, commands.BucketType.user)
    # async def bun(self, ctx):
    #     r = requests.get(f"https://api.imgur.com/3/gallery/FQsx8/images?client_id={imgurC}").json()
    #     em = discord.Embed(title="buns :D")
    #     indexmax = len(r['data']) - 1
    #     size = random.randrange(0, indexmax, 1)
    #     em.set_image(url=str(r['data'][size]['link']))
    #     em.color = discord.Color.magenta()
    #     try:
    #         await ctx.send(embed=em)
    #         await ctx.message.delete()
    #     except:
    #         await ctx.send(str(r['data'][size]['link']))

    @commands.command(help="generate a random insult",
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def insult(self, ctx):
        """random insult"""
        lines = open('text_dir/insults.txt').read().splitlines()
        await ctx.send(random.choice(lines))
        await ctx.message.delete()

    @commands.command(help="Ask the 8Ball a question",
                      aliases=["8ball",
                               "8b",
                               "eb"],
                      pass_context=True)
    async def eightball(self, ctx, *, question: commands.clean_content):
        """ Consult 8ball to receive an answer """
        answer = random.choice(lists.ballresponse)
        await ctx.send(f"🎱 **Question:** {question}\n**Answer:** {answer}")

    @commands.command(help="Get a random dad joke",
                      aliases=["dad"])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def daddy(self, ctx):
        author = ctx.author
        async with aiohttp.ClientSession() as session:
            async with session.get("https://dadjoke-api.herokuapp.com/api/v1/dadjoke") as r:
                data = await r.json()
                d = discord.Embed(title=f":milk: Hey, I found the milk", description=data['joke'],
                                  color=discord.Color.magenta()
                                  , timestamp=datetime.utcnow())
                await ctx.send(embed=d)

    @commands.command(help="Get a random history fact",
                      aliases=["hist", "rh", "randhist"],
                      pass_context=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def history(self, ctx):
        await ctx.message.delete()
        author = ctx.message.author
        shit = await ctx.send(f"Fetching History for {ctx.author.mention}!")
        await shit.delete(delay=6)
        async with aiohttp.ClientSession() as cs:
            async with cs.get('http://numbersapi.com/random/date?json') as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.magenta(),
                    title="Random History! :books:",
                    description=f":point_down:**Fact**:point_down:\n\n {res['text']}\n"
                                f"\n:point_right: Year: {res['year']}"
                )
                await asyncio.sleep(1)
                await ctx.send(embed=embed)

    @commands.command(help="Uwuify text. I can\'t uwuify text over 2000 characters.",
                      aliases=["owoify", "uwu", "uwuize"],
                      pass_context=True)
    async def owo(self, ctx, *, text: str):
        text += " uwu"
        await ctx.send(text.replace("r", "w").replace("l", "w").replace("a", "aw"))
        await ctx.message.delete()

    @commands.command(help="say:clap: some :clap: words :clap:",
                      pass_context=True)
    async def clap(self, ctx, *, mm: str):
        await ctx.send(mm.replace(" ", ":clap:"))
        await ctx.message.delete()

    @commands.command(help="make some biggy",
                      pass_contex=True,
                      aliases=["big"])
    async def BEEEG(self, ctx, *, text: str):
        await ctx.message.delete()
        await ctx.send(
            getattr("", "join")(
                [
                    getattr(":regional_indicator_{}:", "format")(i)
                    if i in getattr(__import__("string"), "ascii_lowercase")
                    else getattr("{}\N{combining enclosing keycap}", "format")(i)
                    if i in getattr(__import__("string"), "digits")
                    else "\U00002757"
                    if i == "!"
                    else "\U000025c0"
                    if i == "<"
                    else "\U000025b6"
                    if i == ">"
                    else "\U00002753"
                    if i == "?"
                    else i
                    for i in getattr(text, "lower")()
                ]
            )
        )

    @commands.command(help="bonk",
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def bonk(self, ctx, member: discord.Member, *, reason=""):
        if member is not ctx.message.author:
            embed = discord.Embed(
                title=f"{ctx.message.author} bonked {member.name} {reason}",
                description='',
                colour=discord.Colour.random()
            )
            tickle = "https://i.imgur.com/T4bGX43.jpeg"
            embed.set_image(url=tickle)
            await ctx.send(embed=embed)
            await ctx.message.delete()

        if member is ctx.message.author:
            embed = discord.Embed(
                title=f"{ctx.message.author} bonked themselves {reason}",
                description='',
                colour=discord.Colour.random()
            )
            tickle = "https://img-comment-fun.9cache.com/media/aPYzMmG/aVlE0ZLW_700w_0.jpg"
            embed.set_image(url=tickle)
            await ctx.send(embed=embed)
            await ctx.message.delete()

    @commands.command(name="gayrate", aliases=["howgay"], brief="Rates your gayness")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def gayrate(self, ctx, member: discord.Member = None):
        """Rate your gayness or another users gayness. 1-100% is returned"""
        gay = round(random.uniform(0, 100), 1)
        str(gay)
        user = member.name + " is" if member else "You are"
        e = discord.Embed(
            title="let's see the gay power level...",
            description=f"{user} {gay}% gay 🌈",
            color=discord.Color.random(),
        )
        if gay >= 85:
            e.set_footer(text="Thats pretty gay lol")
        if gay <= 25:
            e.set_footer(text="Thats kinda straight smh")
        await ctx.send(embed=e)

    @commands.command()
    async def enlarge(self, ctx, emoji: discord.PartialEmoji = None):
        if not emoji:
            await ctx.send("You need to provide a custom emoji!")
        else:
            await ctx.message.delete()
            await ctx.send(emoji.url)

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def marry(self, ctx, member: discord.Member = None):
        """random marriage command"""
        user = member.name + " will now" if member else "You are going to"
        count = len(open('text_dir/thiccNames.txt').readlines())
        with open('text_dir/thiccNames.txt', 'w') as f:
            for member in ctx.guild.members:
                try:
                    print(f'{member.name}', file=f)
                except:
                    print(f"Unable to write an ID... continuing")
                    continue
        print(f"done printing names\nCount: {count}")
        thicc = open('text_dir/thiccNames.txt').read().splitlines()
        thiccy = random.choice(thicc)
        e = discord.Embed(title=f"🎉 {user} marry {thiccy}! 🎉",
                          colour=discord.Color.random())
        await ctx.message.reply(embed=e)

    @commands.command(help="Get a counter of phrases uttered over the past 800 messages",
                      aliases=["phrase",
                               "wc",
                               "words",
                               "pc"],
                      pass_context=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def word_count(self, ctx, *, word=""):
        counter = 0
        async with ctx.channel.typing():
            try:
                async for message in ctx.channel.history(limit=800):
                    if word.casefold() == message.author.bot:
                        return
                    elif word.casefold() in message.content:
                        counter += 1

                e = discord.Embed(title=f"Recent {word} count for this channel",
                                  description=f'{word} has been said {counter} time(s) in recent memory.\n'
                                              f'Thank you for using my counter.',
                                  colour=discord.Color.random())
                e.set_thumbnail(url=self.bot.user.avatar_url)

                await ctx.message.reply(embed=e)
            except:
                await ctx.send(f'```Unable to find the phrase: {word}```, '
                               f'or there was an error in my processing of this command.',
                               delete_after=10)

    @commands.command(help="baja blast a homie",
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def baja(self, ctx, member: discord.Member, *, reason=""):
        embed = discord.Embed(
            title=f"The stars have aligned...",
            description=f'',
            colour=discord.Colour.random()
        )
        baja = "https://i.imgur.com/EpwGbns.png"

        embed.add_field(name=f'{ctx.message.author} baja blasted {member.name}',
                        value=f'\n{reason}')

        embed.set_image(url=baja)
        if member.avatar:
            embed.set_thumbnail(url=member.avatar_url)

        await ctx.send(embed=embed)
        await ctx.message.delete()


    # @commands.command()
    # async def rand_sent(self, ctx):


def setup(bot):
    bot.add_cog(Fun(bot))
