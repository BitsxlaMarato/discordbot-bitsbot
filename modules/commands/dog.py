import random

from discord import Embed
from discord.ext.commands import Context
from discord.utils import get

from get_enviroment import MEMES_CHANNEL, RANDOM_CHANNEL
from modules.commands.base import BaseCommand
from modules.commands.utils import get_bits_server


class Dog(BaseCommand):

    def __init__(self, context: Context, client):
        super().__init__(context)
        self.client = client
        self.guild = get_bits_server(self.client)
        self.author = get(self.guild.members, id=context.author.id)

    async def apply(self):
        if self.ctx.channel.name == MEMES_CHANNEL or self.ctx.channel.name == RANDOM_CHANNEL:
            embed = Embed()
            embed.set_image(url="https://placedog.net/%d" % random.uniform(100, 500))
            await self.ctx.send(embed=embed)
