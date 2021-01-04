from discord.ext.commands import Context
from discord.utils import get

from modules.commands.base import BaseCommand
from modules.commands.utils import get_bits_server
from modules.database.masterData import MasterData


class LoginEmail(BaseCommand):

    def __init__(self, context: Context, client):
        super().__init__(context)
        self.client = client
        self.guild = get_bits_server(self.client)
        self.author = get(self.guild.members, id=context.author.id)

    async def apply(self):
        data = MasterData.getInstance()
        texts = data.get_logged_emails()
        if not texts:
            await self.author.send("No one is logged in")
        else:
            lines = texts.split("\n")
            text_to_send = ""
            i = 0
            for line in lines:
                if i <= 5:
                    text_to_send += (line + "\n")
                    i += 1
                else:
                    await self.author.send(text_to_send)
                    text_to_send = ""
                    i = 0
            if i != 0:
                await self.author.send(text_to_send)
