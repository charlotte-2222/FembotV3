import discord
from discord.ext import commands
import inspirobot


class InspiroCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Gives you an inspirational quote"
                           " for to help you throughout the day.",
                      aliases=["insp",
                               "spire",
                               "motivate"])
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def inspire(self, ctx):
        try:
            quote = inspirobot.generate()
            e = discord.Embed(title=":eye::lips::eye: | Inspiration :sparkles:",
                              colour=discord.Colour.random()
                              )
            e.set_image(url=quote.url)
            await ctx.reply(embed=e)
        except:
            pass

    @commands.command(aliases=["flow",
                               "fq",
                               "flow_quotes"],
                      help="offers inspirational flow quotes")
    async def flow_q(self, ctx):
        flow = inspirobot.flow()
        for quote in flow:
            await ctx.send(quote.text)


def setup(bot):
    bot.add_cog(InspiroCog(bot))
