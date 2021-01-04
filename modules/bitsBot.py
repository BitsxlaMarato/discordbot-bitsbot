from asyncio import sleep

import discord
from discord.ext import commands
from discord.ext.commands import cooldown

from get_enviroment import TOKEN, COMMAND_PREFIX, MEMES_CHANNEL, RANDOM_CHANNEL, ORGANIZER_CHANNEL


class BitsBot:

    prefix = ""
    client = None
    token = ""

    def __init__(self) -> None:
        self.prefix = COMMAND_PREFIX
        intents = discord.Intents.default()
        intents.members = True
        self.client = commands.Bot(self.prefix, guild_subscriptions=True, self_bot=False, intents=intents)
        self.token = TOKEN
        self.client.remove_command('help')

        @self.client.command()
        async def login(ctx, arg):
            from modules.commands.login import LoginCommand
            await LoginCommand(context=ctx, email=arg, client=self.client).apply()

        @self.client.command()
        async def FIBAddEmail(ctx, arg):
            from modules.commands.fibAddEmail import FIBAddEmail
            await FIBAddEmail(context=ctx, email=arg, client=self.client).apply()

        @self.client.event
        async def on_member_join(member):
            from modules.commands.welcome import Welcome
            await Welcome(member=member).apply()

        @self.client.command()
        async def createTeam(ctx, arg):
            from modules.commands.createTeam import CreateTeam
            await CreateTeam(context=ctx, team=arg, client=self.client).apply()

        @self.client.command()
        async def addToTeam(ctx, arg):
            from modules.commands.addToTeam import AddToTeam
            await AddToTeam(context=ctx, user=arg, client=self.client).apply()

        @self.client.command()
        @cooldown(1, 10, commands.BucketType.user)
        async def parrot(ctx):
            from modules.commands.parrot import Parrot
            await Parrot(context=ctx, client=self.client).apply()

        @self.client.command()
        @cooldown(1, 10, commands.BucketType.user)
        async def cat(ctx):
            from modules.commands.cat import Cat
            await Cat(context=ctx, client=self.client).apply()

        @self.client.command()
        @cooldown(1, 10, commands.BucketType.user)
        async def dog(ctx):
            from modules.commands.dog import Dog
            await Dog(context=ctx, client=self.client).apply()

        @self.client.command()
        @cooldown(1, 10, commands.BucketType.user)
        async def joke(ctx):
            from modules.commands.joke import Joke
            await Joke(context=ctx, english=1).apply()

        @self.client.command()
        @cooldown(1, 10, commands.BucketType.user)
        async def proJoke(ctx):
            from modules.commands.joke import Joke
            await Joke(context=ctx, english=0).apply()

        @self.client.command()
        @cooldown(1, 10, commands.BucketType.user)
        async def parJoke(ctx):
            from modules.commands.joke import Joke
            await Joke(context=ctx, english=2).apply()

        @self.client.command()
        async def help(ctx):
            from modules.commands.help import Help
            await Help(context=ctx, client=self.client).apply()

        @self.client.command()
        async def biene(ctx):
            if ctx.channel.name == MEMES_CHANNEL or ctx.channel.name == RANDOM_CHANNEL or ctx.channel.name == ORGANIZER_CHANNEL:
                await ctx.send("Biene!")

        @self.client.command()
        async def ping(ctx):
            if ctx.channel.name == MEMES_CHANNEL or ctx.channel.name == RANDOM_CHANNEL or ctx.channel.name == ORGANIZER_CHANNEL:
                await ctx.send("pong")

        @self.client.command()
        @commands.has_role("Organizers")
        async def info(ctx, arg):
            from modules.commands.info import Info
            await Info(context=ctx, client=self.client, user_id=arg).apply()

        @self.client.command()
        @commands.has_role("Organizers")
        async def email(ctx, arg):
            from modules.commands.email import Email
            await Email(context=ctx, client=self.client, user_id=arg).apply()

        @self.client.command()
        @commands.has_permissions(administrator=True)
        async def clearYesImSure(ctx):
            deleted = await ctx.channel.purge(limit=10000)
            msg = await ctx.send('purged %d messages' % len(deleted))
            await sleep(2)
            await msg.delete()

        @self.client.command()
        @commands.has_permissions(administrator=True)
        async def loginEmails(ctx):
            from modules.commands.loginEmail import LoginEmail
            await LoginEmail(context=ctx, client=self.client).apply()

        @self.client.command()
        @commands.has_permissions(administrator=True)
        async def user(ctx, arg):
            from modules.commands.user import User
            await User(context=ctx, client=self.client, email=arg).apply()

    def start(self):
        print("Starting modules!")
        self.client.run(self.token)
