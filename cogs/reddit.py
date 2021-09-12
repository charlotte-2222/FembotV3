from datetime import datetime
import random

import discord
from discord.ext import commands
import praw
from utilityFunction.config import *

reddit = praw.Reddit(client_id=redditC,
                     client_secret=redditCS,
                     user_agent=redditU_A)


class Reddit(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="Get a random meme from the hottest r/memes of the day",
                      aliases=["memes"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def meme(self, ctx):
        submissions = reddit.subreddit('memes').hot()
        post_to_pick = random.randint(1, 20)
        for i in range(0, post_to_pick):
            submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)

    @commands.command(help="Get a random post from r/gaming, sorted by hottest",
                      aliases=["game"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def gaming(self, ctx):
        submissions = reddit.subreddit('gaming').hot()
        post_to_pick = random.randint(1, 20)
        for i in range(0, post_to_pick):
            submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)

    @commands.command(help="Get a random hot post from r/halo")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def halo(self, ctx):
        submissions = reddit.subreddit('halo').hot()
        post_to_pick = random.randint(1, 20)
        for i in range(0, post_to_pick):
            submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)

    @commands.command(help="Destiny memes, sorted by hotest",
                      aliases=["destiny", "destiny memes", "destiny_memes"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def dmemes(self, ctx):
        submissions = reddit.subreddit('destinymemes').hot()
        post_to_pick = random.randint(1, 20)
        for i in range(0, post_to_pick):
            submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)

    @commands.command(help="Get a random duck")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def duck(self, ctx):
        submissions = reddit.subreddit('duck').new()
        post_to_pick = random.randint(1, 50)
        for i in range(0, post_to_pick):
            submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)

    @commands.command(help="Get a random cat - that's yelling",
                      aliases=["yc", "yelling"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def yell_cat(self, ctx):
        submissions = reddit.subreddit('catswhoyell').hot()
        post_to_pick = random.randint(1, 20)
        for i in range(0, post_to_pick):
            submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)

    @commands.command(help="Check out some food ~ erotically ",
                      aliases=["fp"])
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def food_porn(self, ctx):
        submissions = reddit.subreddit('foodporn').hot()
        post_to_pick = random.randint(1, 30)
        for i in range(0, post_to_pick):
            submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)


def setup(bot):
    bot.add_cog(Reddit(bot))
