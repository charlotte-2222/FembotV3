from datetime import datetime
import random
from imgurpython import ImgurClient

from utilityFunction.config import *
import discord
import requests
from discord.ext import commands

import nekos
import sys

imgur = ImgurClient(imgurC, ImgurL)


class NekosCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Shaxx porn")
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def shaxx(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            r = requests.get(f"https://api.imgur.com/3/album/OVCCqqa/images?client_id={imgurC}").json()
            em = discord.Embed(title="uwu shaxxy-waxxie's thicc cock")
            indexmax = len(r['data']) - 1
            size = random.randrange(0, indexmax, 1)
            em.set_image(url=str(r['data'][size]['link']))
            em.color = discord.Color.magenta()
        try:
            await ctx.send(embed=em)
            await ctx.message.delete()
            print(f"{ctx.author} is asking for shaxx porn")
        except:
            await ctx.send(str(r['data'][size]['link']))

    @commands.command(help="Foot hentai")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def feet(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title='feet doe :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        feet = nekos.img("feet")

        embed.set_image(url=feet)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    # YURI
    @commands.command(help="I'm pretty sure this is a fancy term for 'Lesbian Porn'")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def yuri(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title='yuri doe :flushed:',
                description='',
                colour=discord.Color.magenta()
            )
        yur1 = nekos.img("yuri")

        embed.set_image(url=yur1)

        await ctx.send(embed=embed)
        await ctx.message.delete()


    @commands.command(help="Femboy porn")
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def femboy(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            author = ctx.message.author
            embed = discord.Embed(
                title='mmmm uwu....',
                description='',
                colour=discord.Colour.magenta()
            )
        trap = nekos.img("trap")
        embed.set_image(url=trap)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="Futa porn",
                      aliases=["futa"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def futanari(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title='futanari doe :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        futanari = nekos.img("futanari")

        embed.set_image(url=futanari)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="Gif of (supposedly) someone alone, likely masturbation - idk")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def solo_gif(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=':flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        solog = nekos.img("solog")

        embed.set_image(url=solog)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="This isn't cum, it's actually Elmers Glue.")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def cum(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title='cum :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        cum = nekos.img("cum")

        embed.set_image(url=cum)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="Cat girl porn - in motion")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def nsfw_neko_gif(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=' :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        nsfw_neko_gif = nekos.img("nsfw_neko_gif")
        embed.set_image(url=nsfw_neko_gif)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="Masturbation i think")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def solo(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=' :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        solo = nekos.img("solo")

        embed.set_image(url=solo)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="what what? In the butt - of course.")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def anal(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=' :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        anal = nekos.img("anal")

        embed.set_image(url=anal)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="just hentai")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def hentai(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=' :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        hentai = nekos.img("hentai")

        embed.set_image(url=hentai)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="it's like feet, but more erotic")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def erofeet(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=' :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        erofeet = nekos.img("erofeet")

        embed.set_image(url=erofeet)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="it's a cat or something")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def pussy(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=' :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        pussy = nekos.img("pussy")

        embed.set_image(url=pussy)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="isn't this a bird?")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def tits(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=' :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        tits = nekos.img("tits")

        embed.set_image(url=tits)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="wish i were someone's waifu",
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def waifu(self, ctx):
        embed = discord.Embed(
            title=' :flushed:',
            description='',
            colour=discord.Colour.magenta()
        )
        waifu = nekos.img("waifu")

        embed.set_image(url=waifu)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="Self explanatory")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def boobs(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=':flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        boobs = nekos.img("boobs")

        embed.set_image(url=boobs)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="Pat someone's head",
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def pat(self, ctx, member: discord.Member, *, reason=""):
        embed = discord.Embed(
            title=f"{ctx.message.author} patted {member.name}",
            description='',
            colour=discord.Colour.magenta()
        )
        pat = nekos.img("pat")

        embed.set_image(url=pat)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="Kiss someone",
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def kiss(self, ctx, member: discord.Member, *, reason=""):
        embed = discord.Embed(
            title=f"{ctx.message.author} kissed {member.name} {reason}",
            description='',
            colour=discord.Colour.magenta()
        )
        kiss = nekos.img("kiss")

        embed.set_image(url=kiss)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="Erotically spank your homie",
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def spank(self, ctx, member: discord.Member, *, reason=""):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                    title=f"{ctx.message.author} spanked {member.name} {reason}",
                    description='',
                    colour=discord.Colour.magenta()
                )
            spank = nekos.img("spank")

            embed.set_image(url=spank)

            await ctx.send(embed=embed)
            await ctx.message.delete()

    @commands.command(help="Cuddle your homie",
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def cuddle(self, ctx, member: discord.Member, *, reason=""):
        embed = discord.Embed(
            title=f"{ctx.message.author} cuddled {member.name} {reason}",
            description='',
            colour=discord.Colour.magenta()
        )
        cuddle = nekos.img("cuddle")

        embed.set_image(url=cuddle)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="Hug your homie",
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def hug(self, ctx, member: discord.Member, *, reason=""):
        embed = discord.Embed(
            title=f"{ctx.message.author} hugged {member.name} {reason}",
            description='',
            colour=discord.Colour.magenta()
        )
        hug = nekos.img("hug")

        embed.set_image(url=hug)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="It's a fox girl, you furry")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def fox_girl(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=':flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
            fox_girl = nekos.img("fox_girl")

            embed.set_image(url=fox_girl)

            await ctx.send(embed=embed)
            await ctx.message.delete()

    @commands.command(help="Well... it's a NekosLife ")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def neko(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=' nekos | :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        neko = nekos.img("neko")

        embed.set_image(url=neko)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="Tickle your homie",
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def tickle(self, ctx, member: discord.Member, *, reason=""):
        embed = discord.Embed(
            title=f"{ctx.message.author} tickled {member.name} {reason}",
            description='',
            colour=discord.Colour.magenta()
        )
        tickle = nekos.img("tickle")

        embed.set_image(url=tickle)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="it's not like i wanted to do any of this... really")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def baka(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title='b-baka! :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        baka = nekos.img("baka")

        embed.set_image(url=baka)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="nsfw avatar creation")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def nsfw_avatar(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=' :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        nsfw_avatar = nekos.img("nsfw_avatar")

        embed.set_image(url=nsfw_avatar)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="makes a wallpaper, I've seen non-NSFW")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def wallpaper(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title='wallpaper :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        wallpaper = nekos.img("wallpaper")

        embed.set_image(url=wallpaper)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="Get pegged 4 hed")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def femdom(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title='domination... :flushed:',
                description='',
                colour=discord.Colour.magenta()
            )
        femdom = nekos.img("femdom")
        embed.set_image(url=femdom)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="You're feeding a user")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def feed(self, ctx, member: discord.Member):
        # if not ctx.channel.is_nsfw():
        #     author = ctx.message.author
        #     await ctx.author.send("```not an nsfw channel```")
        #     sys.stderr = object
        embed = discord.Embed(
                title=f"{ctx.author.name} fed {member.name} like widdle baby uwu",
                description='',
                colour=discord.Colour.magenta()
        )
        feed = nekos.img("feed")
        embed.set_image(url=feed)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="Kuni is to eat another out")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def kuni(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                    title=f'lemme eat you out, {ctx.author.name}!',
                    description='',
                    colour=discord.Colour.magenta()
            )
        kuni = nekos.img("kuni")
        embed.set_image(url=kuni)

        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="random fact")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def fact(self, ctx):
        embed = discord.Embed(
                title='Random Fact from NekosLife',
                description='',
                colour=discord.Colour.magenta()
        )
        fact = nekos.img("/fact")
        embed.set_image(url=fact)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="Holoero | Fox girl")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def holoero(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=f'Holoero uwu',
                description='',
                colour=discord.Colour.magenta()
            )
        holoero = nekos.img("holoero")
        embed.set_image(url=holoero)
        await ctx.send(embed=embed)
        await ctx.message.delete()

    @commands.command(help="Woof | Dog Girl")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def woof(self, ctx):
        if not ctx.channel.is_nsfw():
            author = ctx.message.author
            await ctx.author.send("```not an nsfw channel```")
            sys.stderr = object
        if ctx.channel.is_nsfw():
            embed = discord.Embed(
                title=f'Woof uwu',
                description='',
                colour=discord.Colour.magenta()
            )
        woof = nekos.img("woof")
        embed.set_image(url=woof)
        await ctx.send(embed=embed)
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(NekosCog(bot))
