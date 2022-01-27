import asyncio
import random
from datetime import datetime
import discord
from discord import guild
from discord.ext import commands


class OnMessCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):

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
        if "catalyst" in content:
            feesh=self.bot.get_user(549292136147845140)
            #await message.reply(f"Oh no! <@!549292136147845140> didn't tell you that was a bad word..."
                               # f"\nI'll make sure to DM her so that this is cleared up... :)")
            await feesh.send('Feeesh! You should tell people not to say your ***slur!***')


        with open('text_dir/badwords.txt', 'r') as f:
            words = f.read()
            badwords = words.splitlines()
            for word in badwords:
                if word in content:
                    try:
                        await message.delete()
                        await asyncio.sleep(1)
                        await message.channel.send(
                            f"Woah! {message.author.mention}, you just said a bad word!"
                            f"\n You can't do that :(\n")
                        await asyncio.sleep(1)
                        await author.send(f"Word you said: {word}....\n"
                                          f"**Our ToS:** https://bit.ly/BreakfastTOS")
                        print(f"{message.author} said {word} in {message.channel}")
                    except:
                        print('Did not warn/delete a badword --- moving on')
                else:
                    continue


def setup(bot):
    bot.add_cog(OnMessCog(bot))
