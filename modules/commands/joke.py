import random

from discord.ext.commands import Context

from get_enviroment import MEMES_CHANNEL, RANDOM_CHANNEL, ORGANIZER_CHANNEL
from modules.commands.base import BaseCommand
from modules.database.jokes_text_en import PRO_JOKES_EN, JOKES_EN


class Joke(BaseCommand):

    def __init__(self, context: Context, english):
        super().__init__(context)
        self.english = english

    async def apply(self):
        if self.ctx.channel.name == MEMES_CHANNEL or self.ctx.channel.name == RANDOM_CHANNEL or \
                self.ctx.channel.name == ORGANIZER_CHANNEL:
            if self.english == 0:
                text = random.choice(PRO_JOKES_EN)
            elif self.english == 1:
                text = random.choice(JOKES_EN)
            else:
                text = random.choice(JOKES_EN + PRO_JOKES_EN)
            await self.ctx.send(text)
