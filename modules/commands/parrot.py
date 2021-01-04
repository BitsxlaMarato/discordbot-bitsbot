import json
import random

from discord import Embed
from discord.ext.commands import Context
from discord.utils import get

from get_enviroment import PARROTS, RANDOM_CHANNEL, MEMES_CHANNEL, ORGANIZER_CHANNEL
from modules.commands.base import BaseCommand
from modules.commands.utils import get_bits_server


class Parrot(BaseCommand):

    def __init__(self, context: Context, client):
        super().__init__(context)
        self.client = client
        self.guild = get_bits_server(self.client)
        self.author = get(self.guild.members, id=context.author.id)

    async def apply(self):
        if self.ctx.channel.name == MEMES_CHANNEL or self.ctx.channel.name == RANDOM_CHANNEL or \
                self.ctx.channel.name == ORGANIZER_CHANNEL:
            with open('files/parrots.json', 'w') as fp:
                json.dump(PARROTS, fp)
            parrot = random.choice(PARROTS)
            embed = Embed()
            embed.set_image(url="https://cultofthepartyparrot.com/parrots/hd/%s" % parrot)
            await self.ctx.send(embed=embed)
