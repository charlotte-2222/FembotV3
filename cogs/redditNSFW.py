import sys
from datetime import datetime
import random

import discord
from discord.ext import commands
import praw
from utilityFunction.config import *

reddit = praw.Reddit(client_id=redditC,
                     client_secret=redditCS,
                     user_agent=redditU_A)


class RedditNSFW(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def destiny34(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('rule34destiny').new()
            post_to_pick = random.randint(1, 50)
            for i in range(0, post_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)
        await ctx.message.delete()
        print(f"{ctx.author} is asking for d34 porn")

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def r34(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('rule34').new()
            post_to_pick = random.randint(1, 50)
            for i in range(0, post_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)
        await ctx.message.delete()
        print(f"{ctx.author} is asking for r34 porn")

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def gw(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('gonewild').new()
            post_to_pick = random.randint(1, 50)
            for i in range(0, post_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)
        await ctx.message.delete()
        print(f"{ctx.author} is asking for gw porn")

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def shefuckshim(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('shefuckshim').new()
            post_to_pick = random.randint(1, 50)
            for i in range(0, post_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)
        await ctx.message.delete()
        print(f"{ctx.author} is asking for shefuckshim porn")

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def rfem(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('FemBoys').new()
            post_to_pick = random.randint(1, 50)
            for i in range(0, post_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)
        await ctx.message.delete()
        print(f"{ctx.author} is asking for femboy porn")

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def cock(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('massivecock').new()
            post_to_pick = random.randint(1, 50)
            for i in range(0, post_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)
        await ctx.message.delete()
        print(f"{ctx.author} is asking for cock porn")

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def red(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('redheads').new()
            post_to_pick = random.randint(1, 50)
            for i in range(0, post_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)
        await ctx.message.delete()
        print(f"{ctx.author} is asking for redhead porn")

    # porninfifteenseconds

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def p15(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('porninfifteenseconds').new()
            post_to_pick = random.randint(1, 50)
            for i in range(0, post_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)
        await ctx.message.delete()
        print(f"{ctx.author} is asking for porninfifteenseconds porn")

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def cum_sluts(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('cumsluts').new()
            post_to_pick = random.randint(1, 50)
            for i in range(0, post_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)
        await ctx.message.delete()
        print(f"{ctx.author} is asking for cumslut porn")

    @commands.command()
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def bdsm(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('bdsm').new()
            post_to_pick = random.randint(1, 50)
            for i in range(0, post_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.send(submission.url)
        await ctx.message.delete()
        print(f"{ctx.author} is asking for bdsm porn")

    @commands.command(help="Posts guys in sweatpants, nsfw only commands")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def sweats(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('guysinsweatpants').new()
            posts_to_pick = random.randint(1, 50)
            for i in range(0, posts_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.reply(submission.url)
        await ctx.message.delete()
        print(f"{ctx.author} is asking for sweats porn")

    @commands.command(help="Femboy hentai")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def femboy_hentai(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('FemboyHentai').new()
            posts_to_pick = random.randint(1, 50)
            for i in range(0, posts_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.reply(submission.url)
        await ctx.message.delete()

    @commands.command(help="Gayming to the EXTREME")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def ggw(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('gaymersgonewild').new()
            posts_to_pick = random.randint(1, 50)
            for i in range(0, posts_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.reply(submission.url)
        await ctx.message.delete()

    @commands.command(help="Another command similar to cum sluts")
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def cum_fet(self, ctx):
        try:
            author = ctx.message.author
            if not ctx.channel.is_nsfw():
                await ctx.author.send("```not an nsfw channel```")
                sys.stderr = object
        except:
            print('exception unhandled')
        if ctx.channel.is_nsfw():
            submissions = reddit.subreddit('cumfetish').new()
            posts_to_pick = random.randint(1, 50)
            for i in range(0, posts_to_pick):
                submission = next(x for x in submissions if not x.stickied)

        await ctx.reply(submission.url)
        await ctx.message.delete()


def setup(bot):
    bot.add_cog(RedditNSFW(bot))
