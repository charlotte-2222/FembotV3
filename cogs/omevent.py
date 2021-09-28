import asyncio
import random
from datetime import datetime
from utilityFunction.convert import *
import discord
from discord.ext import commands


class OnMessCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

        EMOJI_REGEX = re.compile(r"(<(a)?:[a-zA-Z0-9\_]+:([0-9]+)>)")

        dream_peen = open('text_dir/dream.txt').read().splitlines()
        e = discord.Embed(title=random.choice(dream_peen),
                          description='',
                          color=discord.Color.green(),
                          timestamp=datetime.utcnow())
        e.set_thumbnail(
            url="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT72G1sug35cD5yqvVRKzns3Dux03zuOoDVLQ&usqp=CAU")
        e.set_footer(text="god i wanna die")
        author = message.author
        if message.author.bot:
            return  # ignore all bots
        content = message.content.casefold()
        if "dream" in content:
            await message.reply(embed=e)
        if 'skill issue' in content:
            await message.reply(f'This just in! {message.author.mention} is a MASSIVE virgin!')
        if "fuck you fembot" in content:
            await message.reply(f"fuck you {message.author.mention}")

        if message.channel.id == 886621065554575413:
            if content.startswith(':'):
                await message.reply('Thanks!')
                pass
            elif content is message.attachments:
                await message.reply('Thanks!')
                pass
            elif not content.startswith(':'):
                await asyncio.sleep(1)
                await message.delete()

    #if "trials" in content:
       # await message.add_reaction("<:no:795350056151941120>")
    #     # if "pog" in content:
    #     #     await message.add_reaction("<:cringe:800461449968353290>")
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
