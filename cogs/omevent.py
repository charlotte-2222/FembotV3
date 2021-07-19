import asyncio
import random

import discord
from discord.ext import commands


class OnMessCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     author = message.author
    #     morning = open('text_dir/mornList.txt').read().splitlines()
    #     goodnight = open('text_dir/gnList').read().splitlines()
    #     dg = discord.Embed(title="uwu", description="",
    #                        colour=discord.Colour.magenta())
    #     dg.set_image(url="https://i.imgur.com/6hmvMu2.png")
    #     myfile = discord.File('images/video0(1).mp4')
    #     mincraft = discord.File('images/christianMinecraft.mp4')
    #     insane = discord.File('images/insane.mp4')
    #     beaners = discord.File('images/bean.mp4')
    #     if message.author.bot:
    #         return  # ignore all bots
    #     content = message.content.casefold()
    #     # if "pog" in content:
    #     #     await message.add_reaction("<:cringe:800461449968353290>")
    #     # if "trials" in content:
    #     #     await message.add_reaction("<:no:795350056151941120>")
    #     if "fuck you fembot" in content:
    #         await message.reply(f"fuck you {message.author.mention}")
    #     if "good morning" in content:
    #         await message.reply(random.choice(morning))
    #     if "goodnight" in content:
    #         await message.channel.send(random.choice(goodnight))
    #     # if "nerd" in content:
    #     #     await message.reply(file=myfile)
    #     #     await message.reply("nErD. Get fucked dumbass.")
    #     if "god is dead" in content:
    #         await message.reply(embed=dg)
    #     if "christian minecraft server" in content:
    #         await message.reply("Wait i gotta meme for this")
    #         await asyncio.sleep(1)
    #         await author.send("https://youtu.be/spi6yOS6zy4")
    #     # if "beans" in content:
    #     #     await message.reply("https://imgur.com/ChjcrdM")






"""got dem beans"""


def setup(bot):
    bot.add_cog(OnMessCog(bot))
