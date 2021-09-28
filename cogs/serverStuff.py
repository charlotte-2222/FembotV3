import os
import urllib.request
from asyncio import sleep
import random
from datetime import datetime, time
from typing import Union

from pytz import timezone

import discord
from discord.ext import commands

from utilityFunction.timeConvert import convert

from mcstatus import MinecraftServer


def to_emoji(c):
    base = 0x1f1e6
    return chr(base + c)


class Server(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_guild_permissions(manage_roles=True)
    async def thicc(self, ctx):
        """Allows server owner to pick the next thicc"""
        count = len(open('text_dir/thiccNames.txt').readlines())
        with open('text_dir/thiccNames.txt', 'w')as f:
            for member in ctx.guild.members:
                try:
                    print(f'{member.name}', file=f)
                except:
                    print(f"Unable to write an ID... continuing")
                    continue

        await ctx.send("possible thiccs updated <:9154_PogU:712671828291747864>\n")
        print(f"done printing names\nCount: {count}")
        channel = self.bot.get_channel(806701505759019058)
        thicc = open('text_dir/thiccNames.txt').read().splitlines()
        thiccy = random.choice(thicc)
        await ctx.message.reply(f"The new daily thicc will be: {thiccy}", mention_author=True)
        await channel.edit(name=f"Thicc: {thiccy}")

    @commands.command(help="Get the weather for a city `^weather [city]`",
                      aliases=["wt"], hidden=False)
    async def weather(self, ctx, city: str = False):
        URL = f"http://wttr.in/{city}_2tnp_transparency=1000_lang=en.png"
        if not city:
            await ctx.send("Please enter a valid city / town")
        else:
            with urllib.request.urlopen(URL) as url:
                with open("temp.png", "wb") as f:
                    f.write(url.read())
            file = discord.File("temp.png", filename="weather.png")
            await ctx.trigger_typing()
            await ctx.send(file=file)
            os.remove("temp.png")

    @commands.command(help="Server information", aliases=['server'], hidden=False)
    async def serverinfo(self, ctx):
        guild = ctx.guild
        embed = discord.Embed(
            color=discord.guild.Colour.magenta(), timestamp=datetime.utcnow(),
            title=f":face_with_monocle:  Server Info For {guild.name}",
            description="\n— "
                        "\n➤ Shows all information about a guild."
                        "\n➤ The information will be listed below!"
                        "\n —"
        )
        regions = {
            "us_west": ":flag_us: — USA West",
            "us_east": ":flag_us: — USA East",
            "us_central": ":flag_us: — USA Central",
            "us_south": ":flag_us: — USA South",
            "sydney": ":flag_au: — Sydney",
            "eu_west": ":flag_eu: — Europe West",
            "eu_east": ":flag_eu: — Europe East",
            "eu_central": ":flag_eu: — Europe Central",
            "singapore": ":flag_sg: — Singapore",
            "russia": ":flag_ru: — Russia",
            "southafrica": ":flag_za:  — South Africa",
            "japan": ":flag_jp: — Japan",
            "brazil": ":flag_br: — Brazil",
            "india": ":flag_in: — India",
            "hongkong": ":flag_hk: — Hong Kong",
        }
        verifications = {
            "none": "<:white__circle:625695417782239234> — No Verification",
            "low": "<:green_circle:625541294525251643> — Low Verification",
            "medium": "<:yellow_circle:625540435820937225> — Medium Verification",
            "high": "<:orange_circle:625542217100165135> — High Verification",
            "extreme": "<:red__circle:625833379258040330> — Extreme Verification"
        }
        embed.set_thumbnail(url=guild.icon_url_as(size=1024, format=None, static_format="png"))
        embed.add_field(name="• Guild name: ", value=str(guild.name))
        embed.add_field(name="• Guild owner: ", value=guild.owner)
        embed.add_field(name="• Guild made in: ", value=guild.created_at.strftime("%A %d, %B %Y"))
        embed.add_field(name="• Channels count: ", value=len(guild.channels))
        embed.add_field(name="• Guild region: ", value=regions[guild.region.name])
        embed.add_field(name="• Guild verification: ", value=verifications[guild.verification_level.name])
        embed.add_field(name="• Member count: ", value=f"{guild.member_count}")
        embed.add_field(name="• Number of Nitro Boosts: ",
                        value=guild.premium_subscription_count or "hmmm... nothing here... :ghost:")
        embed.add_field(name="• Fembot Prefix ",
                        value="`^` •  `@Fembot`")

        await ctx.send(embed=embed)

    @commands.command(help='get the time')
    async def time(self, ctx, *timeZ):
        th = str(timeZ).upper()
        td = str(*timeZ)
        author = ctx.message.author
        e = discord.Embed(title=f":globe_with_meridians: ➤ **{ctx.author.name} asked for {td} time!**\n",
                          colour=discord.Color.magenta(),
                          timestamp=datetime.utcnow())
        e.color = discord.Color.magenta()
        e.set_thumbnail(url="https://i.imgur.com/F72Lc77.png")
        e.set_footer(text="Time now  ")

        if "GMT" in th:
            p = timezone('ETC/Greenwich')
            pg = datetime.now(p)
            e.add_field(name=f"GMT", value=pg.strftime(f'%I:%M:%S %p\n' +
                                                       f'%m/%d/%Y'))
        elif "EST" in th:
            p = timezone('US/Eastern')
            pg = datetime.now(p)
            e.add_field(name=f"EST", value=pg.strftime(f'%I:%M:%S %p\n' +
                                                       f'%m/%d/%Y'))
        elif "AU" in th:
            p = timezone('Australia/Sydney')
            pg = datetime.now(p)
            e.add_field(name=f"AU", value=pg.strftime(f'%I:%M:%S %p\n' +
                                                      f'%m/%d/%Y'))
        elif "CST" in th:
            p = timezone('America/Monterrey')
            pg = datetime.now(p)
            e.add_field(name=f"CST", value=pg.strftime(f'%I:%M:%S %p\n' +
                                                       f'%m/%d/%Y'))
        elif "MT" in th:
            p = timezone('America/Mazatlan')
            pg = datetime.now(p)
            e.add_field(name=f"Mountain Time", value=pg.strftime(f'%I:%M:%S %p\n' +
                                                                 f'%m/%d/%Y'))
        elif "PST" in th:
            p = timezone('America/Tijuana')
            pg = datetime.now(p)
            e.add_field(name=f"Pacific Time", value=pg.strftime(f'%I:%M:%S %p\n' +
                                                                f'%m/%d/%Y'))
        elif "NZ" in th:
            p = timezone('Pacific/Auckland')
            pg = datetime.now(p)
            e.add_field(name=f"New Zealand", value=pg.strftime(f'%I:%M:%S %p\n' +
                                                               f'%m/%d/%Y'))

        elif "Crimea" in th:
            p = timezone('Europe/Simferopol')
            pg = datetime.now(p)
            e.add_field(name=f"Crimea", value=pg.strftime(f'%I:%M:%S %p\n' +
                                                          f'%m/%d/%Y'))

        elif "SG" in th:
            p = timezone('Asia/Singapore')
            pg = datetime.now(p)
            e.add_field(name=f"Asia/Singapore", value=pg.strftime(f'%I:%M:%S %p\n' +
                                                                  f'%m/%d/%Y'))
        else:

            e.add_field(name=f"But.... {ctx.author.name} is dumb <:flop_laugh:833181636924669972> ",
                        value="No time zone argument was given, please go "
                              "fuck yourself.\n"
                              "https://www.timeanddate.com/worldclock/"

                        )
        e.add_field(name="Convert", value=f"https://bit.ly/ConvertTZ")
        await ctx.message.reply(embed=e)

    @commands.command(aliases=['ping_minecraft',
                               'minecraft_status',
                               'mc_status',
                               'mc_ping'],
                      hidden=False,
                      description="Pinging the RAD server for uptime / Availabilitity")
    # async def ping_mc_server(self, ctx):
    #     try:
    #         server = MinecraftServer(str("rad.craftersland.net"), port=25565)
    #         status = server.status()
    #         online = status.players.online
    #         max_players = status.players.max
    #         ping = round(status.latency)
    #         version = status.raw['version']['name']
    #         up = discord.Embed(title="`RAD 1 | Craftersland`",
    #                            description=f"Response time: {ping}\n"
    #                                        f"Online: :white_check_mark:\n"
    #                                        f"Version: {version}\n"
    #                                        f"Max Players: {max_players}",
    #                            colour=discord.Colour.green(),
    #                            timestamp=datetime.utcnow()
    #                            )
    #         up.add_field(name="Players Online Now", value=f"{online}\n")
    #         await ctx.send(embed=up)
    #     except (ConnectionRefusedError,
    #             OSError
    #             ) as e:
    #         offline = discord.Embed(
    #             title=":exclamation: The Server is offline :exclamation:",
    #             description="Sorry kids, the server is currently unavailable. "
    #                         "Check back later. It's possible that the server is either under maintenance,"
    #                         "or has briefly undergone a reset. Thank you for understanding.",
    #             colour=discord.Color.red(),
    #             timestamp=datetime.utcnow()
    #         )
    #         offline.add_field(name="Error:", value=f"{e}")
    #         await ctx.send(embed=offline)

    async def ping_mc_server(self, ctx):
        e = discord.Embed(
            title='~ Deprecated Command! ~',
            description='tl;dr\nMany servers have come and gone, we no longer have one.\n'
                        'Contact an admin if you want more info or wish to host one.',
            timestamp=datetime.utcnow()
        )
        await ctx.send(embed=e)

    @commands.command()
    async def info(self, ctx, *, user: Union[discord.Member, discord.User] = None):
        """Shows info about a user."""

        user = user or ctx.author
        e = discord.Embed()
        e.color = discord.Color.magenta()
        roles = [role.name.replace('<@&>', '<@&\u200b>') for role in getattr(user, 'roles', [])]
        e.set_author(name=str(user))

        def format_date(dt):
            if dt is None:
                return 'N/A'
            return f'{dt:%A %d, %B %Y • %I:%M %p}'

        e.add_field(name='ID', value=user.id, inline=False)
        e.add_field(name='Joined', value=format_date(getattr(user, 'joined_at', None)), inline=False)
        e.add_field(name='Created', value=format_date(user.created_at), inline=False)
        if roles:
            e.add_field(name='Roles', value='\n '.join(roles) if len(roles) < 10 else f'{len(roles)} roles',
                        inline=False)

        voice = getattr(user, 'voice', None)
        if voice is not None:
            vc = voice.channel
            other_people = len(vc.members) - 1
            voice = f'{vc.name} with {other_people} others' if other_people else f'{vc.name} by themselves'
            e.add_field(name='Voice', value=voice, inline=False)

        colour = user.colour
        if colour.value:
            e.colour = colour

        if user.avatar:
            e.set_thumbnail(url=user.avatar_url)

        if isinstance(user, discord.User):
            e.set_footer(text='This member is not in this server.')

        await ctx.send(embed=e)

    @commands.command(help="Displays info on Fembot",
                      aliases=["bi"])
    async def fem_info(self, ctx):
        e = discord.Embed(
            title="<:6876_BlobCatLove:708017303798939792> | Hi, i'm Fembot!",
            description="I'm <@384459643545583627> personal server bot, "
                        "she coded me using Python, "
                        "and even self-hosts me."
                        "\n\n\thttps://github.com/charlotte-2222/FembotV3/wiki",
            colour=discord.Colour.magenta()
        )
        e.set_image(url=self.bot.user.avatar_url)
        await ctx.send(embed=e)
        await ctx.message.delete()

    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def create_text(self, ctx, *, name=""):
        try:
            await ctx.guild.create_text_channel(f'{name}')
        except:
            await ctx.guild.create_text_channel(f'new-txt-chan')

    @commands.command()
    @commands.has_guild_permissions(kick_members=True)
    async def create_vc(self, ctx, *, name=""):
        try:
            await ctx.guild.create_voice_channel(f'{name}')
        except:
            await ctx.guild.create_voice_channel(f'new vc')


def setup(bot):
    bot.add_cog(Server(bot))
