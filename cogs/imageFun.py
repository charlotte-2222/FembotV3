from datetime import datetime

from typing import Union


import aiohttp
import random
import discord
import requests
from discord.ext import commands
from imgurpython import ImgurClient
import numpy as np


from utilityFunction.config import *

imgur = ImgurClient(imgurC, ImgurL)

code = "```py\n{0}\n```"


def get_deep_text(element):
    try:
        text = element.text or ''
        for subelement in element:
            text += get_deep_text(subelement)
        text += element.tail or ''
        return text
    except:
        return ''


def posnum(num):
    if num < 0:
        return - (num)
    else:
        return num


def find_coeffs(pa, pb):
    matrix = []
    for p1, p2 in zip(pa, pb):
        matrix.append([p1[0], p1[1], 1, 0, 0, 0, -p2[0] * p1[0], -p2[0] * p1[1]])
        matrix.append([0, 0, 0, p1[0], p1[1], 1, -p2[1] * p1[0], -p2[1] * p1[1]])
    A = np.matrix(matrix, dtype=np.float)
    B = np.array(pb).reshape(8)
    res = np.dot(np.linalg.inv(A.T * A) * A.T, B)
    return np.array(res).reshape(8)


class ImageFunCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="See a member's avatar")
    async def avatar(self, ctx, *, user: Union[discord.Member, discord.User] = None):
        user = user or ctx.author
        avatar = user.avatar_url_as(static_format='png')

        e = discord.Embed(title="Here you go!",
                          description=f"uwu i'm just doing my job...awwe yew pwoud? :flushed:",
                          colour=discord.Colour.magenta())
        e.set_author(name=str(user), url=avatar)
        e.set_image(url=avatar)
        await ctx.send(embed=e)

    @commands.command(help="Try it and see",
                      pass_context=True)
    @commands.cooldown(1, 4, commands.BucketType.user)  # allows users to test the response of the bot from Discord
    async def tias(self, ctx):
        st = ['images/TIAS.jpg',
              'images/haveGoogle.png',
              'images/didYouEvenTry.png',
              'images/googleDie.png']
        await ctx.send(file=discord.File(random.choice(st)))
        await ctx.message.delete()

    @commands.command(help="Go ahead, fight me",
                      pass_context=True)
    @commands.cooldown(1, 4, commands.BucketType.user)  # allows users to test the response of the bot from Discord
    async def fightme(self, ctx):
        st = 'images/'
        await ctx.send(file=discord.File(st + 'rollupbitch.png'))
        await ctx.message.delete()

    @commands.command(help="Damn bro",
                      pass_context=True)
    @commands.cooldown(1, 4, commands.BucketType.user)  # allows users to test the response of the bot from Discord
    async def damn(self, ctx):
        st = 'images/'
        await ctx.send(file=discord.File(st + 'damnbro.jpg'))
        await ctx.message.delete()

    @commands.command(help="Indeed",
                      aliases=["z", "vuvu", "zaza"],
                      pass_context=True)
    @commands.cooldown(1, 4, commands.BucketType.user)  # allows users to test the response of the bot from Discord
    async def blueman(self, ctx):
        varEmbed = discord.Embed(title='Zavala...')
        varEmbed.add_field(name='Whether we wanted it or not....',
                           value="***.... we've stepped into a war with the Cabal on Mars. So let's get to taking out "
                                 "their command, one by one. Valus Ta'aurc. From what I can gather, he commands the "
                                 "Siege Dancers from an Imperial Land Tank just outside of Rubicon. He's well "
                                 "protected, but with the right team, we can punch through those defenses, "
                                 "take this beast out, and break their grip on Freehold.***")
        varEmbed.color = discord.Color.orange()
        varEmbed.set_image(url='https://i.imgur.com/0Aqdhln.jpg')
        await ctx.send(embed=varEmbed)
        await ctx.message.delete()

    @commands.command(help="Tell your homies goodmorning",
                      aliases=["goodmorning"],
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def gm(self, ctx):
        r = requests.get(f"https://api.imgur.com/3/album/88Jc9ru/images?client_id={imgurC}").json()
        author = ctx.author
        fU = str(author)
        x = fU.index("#")
        fU = fU[0:x]
        em = discord.Embed(title=str(fU) + " said: Good morning everyone ☕", timestamp=datetime.utcnow())
        em.set_footer(text="Remind ya girl Charlotte to run the thicc command!")
        indexmax = len(r['data']) - 1
        size = random.randrange(0, indexmax, 1)
        em.set_image(url=str(r['data'][size]['link']))
        em.color = discord.Color.magenta()
        try:
            await ctx.send(embed=em)
            await ctx.message.delete()
        except:
            await ctx.send(str(r['data'][size]['link']))

    @commands.command(help="Tell your homies goodnight",
                      aliases=["goodnight"],
                      pass_context=True)
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def gn(self, ctx):
        author = ctx.author
        fU = str(author)
        x = fU.index("#")
        fU = fU[0:x]
        r = requests.get(f"https://api.imgur.com/3/album/3fy68kJ/images?client_id={imgurC}").json()
        em = discord.Embed(title=str(fU) + " said: Goodnight everyone🌙", timestamp=datetime.utcnow())
        em.set_footer(text="You guys are the best and I love you all!")
        indexmax = len(r['data']) - 1
        size = random.randrange(0, indexmax, 1)
        em.set_image(url=str(r['data'][size]['link']))
        em.color = discord.Color.magenta()
        try:
            await ctx.send(embed=em)
            await ctx.message.delete()
        except:
            await ctx.send(str(r['data'][size]['link']))

    @commands.command(help="This is the bean commands, here you are...")
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def beans(self, ctx):
        # e = discord.Embed(title="Beans.",
        #                   description="https://youtu.be/Yw1TFl4qJ9s",
        #                   color=discord.Color.magenta(),
        #                   timestamp=datetime.utcnow())
        # e.set_thumbnail(url="https://images.heb.com/is/image/HEBGrocery/000120104")
        # e.set_footer(text="Fuckin' beans")
        await ctx.send("https://youtu.be/Yw1TFl4qJ9s")
        await ctx.message.delete()

    @commands.command(help="distorts an image, use with a URL to distort `^magik url`",
                      aliases=["magic", "magikify", "distort"], pass_context=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def magik(self, ctx, image: str, intensity: int = 2):
        """Actual working magik command - used an api, but is what it is"""
        emoji = "<:9154_PogU:712671828291747864>"

        await ctx.message.delete()

        message = await ctx.send(f"{emoji} — **Processing the image please wait!**")
        await message.delete(delay=3)

        async with aiohttp.ClientSession() as cs:
            async with cs.get(f"https://nekobot.xyz/api/imagegen?type=magik&image={image}&intensity={intensity}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.magenta(),
                    title="uwu cooooool"
                )
                embed.set_image(url=res["message"])
                await ctx.send(embed=embed)

    @commands.command(help="deepfries an image, use with a URL to distort `^deepfry url`",
                      aliases=["fry", "deep", "df"], pass_context=True)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def deepfry(self, ctx, image: str, intensity: int = 5):
        """Deepfry - works alongside magik. """
        emoji = "<:9154_PogU:712671828291747864>"
        await ctx.message.delete()
        message = await ctx.send(f"{emoji} — **Processing the image please wait!**")
        await message.delete(delay=3)
        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                    f"https://nekobot.xyz/api/imagegen?type=deepfry&image={image}&intensity={intensity}") as r:
                res = await r.json()
                embed = discord.Embed(
                    color=discord.Color.magenta(),
                    title="uwu :flushed:"
                )
                embed.set_image(url=res["message"])
                await ctx.send(embed=embed)

    @commands.command(pass_context=True)
    async def rip(self, ctx, name: str = None, *, text: str = None):
        try:
            if name is None:
                name = ctx.message.author.name
            if len(ctx.message.mentions) >= 1:
                name = ctx.message.mentions[0].name
            if text != None:
                if len(text) > 22:
                    one = text[:22]
                    two = text[22:]
                    url = "http://www.tombstonebuilder.com/generate.php?top1=R.I.P&top3={0}&top4={1}&top5={2}".format(
                        name,
                        one,
                        two).replace(
                        " ", "%20")
                else:
                    url = "http://www.tombstonebuilder.com/generate.php?top1=R.I.P&top3={0}&top4={1}".format(name,
                                                                                                             text).replace(
                        " ", "%20")
            else:
                if name[-1].lower() != 's':
                    name += "'s"
                url = "http://www.tombstonebuilder.com/generate.php?top1=R.I.P&top3={0}&top4=Hopes and Dreams".format(
                    name).replace(" ", "%20")
            b = await ctx.send(url)
            await ctx.send(file=b)
        except Exception as e:
            pass

    @commands.command(pass_context=True)
    async def bezos(self, ctx, *, text: str=None):
        bezos = "https://static.independent.co.uk/s3fs-public/thumbnails/image/2020/08/27/14/jeff-bezos-net-worth.jpg?width=982&height=726&auto=webp&quality=75"
        t = text.replace(" ", "%20")
       # p=random.choice(bezos)
        url = f"https://textoverimage.moesif.com/image?image_url={bezos}&text={t}"#"&text_color=ffcd00ff"
        e=discord.Embed(title="Jeff Bezos has a message",
                        colour=discord.Colour.random()
                        )
        e.set_image(url=url)
        await ctx.send(embed=e)
        await ctx.message.delete()




def setup(bot):
    bot.add_cog(ImageFunCog(bot))
