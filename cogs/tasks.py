import time
from datetime import datetime

import discord
from discord.ext import commands, tasks


class TaskCog(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot
        self.mom.start()
        self.meds.start()

    # @tasks.loop(hours=1)
    # async def ping_zumi(self):
    #     channel = self.bot.get_channel(700153052769943582)
    #     zumi = self.bot.get_user(526479281615011850)
    #     try:
    #         await zumi.send(f'Messaging you every hour\n '
    #                            )
    #         await zumi.send(
    #             'https://cdn.discordapp.com/attachments/880300669741989948/886796999561707560/rmtmhhmhmhhh-1-1.mp4')
    #     except:
    #         await channel.send(f'Could not dm <@!526479281615011850>, or complete loop - so im doing it here.\n'
    #                            f'https://cdn.discordapp.com/attachments/880300669741989948/886796999561707560/rmtmhhmhmhhh-1-1.mp4')
    #         print(time.strftime(f"Loop that was created at:\n"
    #                             "%H:%M:%S\n"
    #                             "%m/%d/%Y\n"
    #                             "failed (Successfully)"))

    @tasks.loop(hours=12)
    async def meds(self):
        me = self.bot.get_user(384459643545583627)
        img = 'https://i.imgur.com/55gjxL9.png'
        e = discord.Embed(title=":pill: | Medication Reminder!",
                          description="**Hey Charlotte! Make sure to take your meds.**\n",
                          colour=discord.Colour.random(),
                          timestamp=datetime.utcnow())
        e.add_field(name="Meds:",
                    value="x1 Keppra (Levetiracetam) - 500mg\n"
                          "x3 Zonisamide - 100mg/capsule\n"
                          "x1 Lamictal (Lamotrigine) - 150mg"
                    )
        e.set_thumbnail(url=img)

        try:
            await me.send(embed=e)
        except:
            print(time.strftime(f"Loop that was created at:\n"
                                "%H:%M:%S\n"
                                "%m/%d/%Y\n"
                                "failed (Successfully)\n"
                                "---Take your meds---"))

    @tasks.loop(hours=32)
    async def mom(self):
        me = self.bot.get_user(384459643545583627)
        e = discord.Embed(title="Send mom a meme",
                          description="**Hey Carlotte - send your mother a meme so that she stays off your back!**\n",
                          colour=discord.Colour.random(),
                          timestamp=datetime.utcnow())
        e.add_field(name="Optimal:",
                    value="discord.gg/memes\n"
                          "https://imgur.com/t/memes\n"
                          "https://inspirobot.me/"
                    )
        e.add_field(name="At some point:",
                    value="Call her, and talk for a while. Try *not* to facetime."
                          "\n**Attempt to facetime on Sundays so you can be ready to take your makeup off**")

        try:
            await me.send(embed=e)
        except:
            print(time.strftime(f"Loop that was created at:\n"
                                "%H:%M:%S\n" 
                                "%m/%d/%Y\n"
                                "failed (Successfully)\n"
                                "---call mom or something---"))


def setup(bot):
    bot.add_cog(TaskCog(bot))
