import discord
from discord.ext import commands
import hashlib
import sqlite3

from utilityFunction.config import token


def get_prefix(bot, message):
    prefixes = ['^']
    if not message.guild:
        return ['?', '^']
    return commands.when_mentioned_or(*prefixes)(bot, message)

# alteration of release on 5/9/22 (Charlotte Childers)

initial_extensions = ['cogs.admin',
                      'cogs.fun',
                      'cogs.imageFun',
                      'cogs.missc',
                      'cogs.owner',
                      'cogs.reddit',
                      'cogs.serverStuff',
                      'cogs.events',
                      'cogs.omevent',
                      'cogs.music',
                      'cogs.insp'
                      ]

bot = commands.Bot(command_prefix=get_prefix,
                   description="Your local femboy, Fembot!",
                   intents=discord.Intents.all(),
                   case_insensitive=True,
                   strip_after_prefix=True
                   )



class MyNewHelp(commands.MinimalHelpCommand):
    async def send_pages(self):
        destination = self.get_destination()
        for page in self.paginator.pages:
            emby = discord.Embed(description=page)
            emby.color = discord.Color.magenta()
            emby.set_thumbnail(url=bot.user.avatar_url)
           # emby.set_footer(text=f"Help requested by {self.discord.Member}")
            await destination.send(embed=emby)


bot.help_command = MyNewHelp(sort_commands=True,
                             no_category=':wave:',
                             )

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run(token,
        reconnect=True)
