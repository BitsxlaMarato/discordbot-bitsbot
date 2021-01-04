from discord.ext.commands import Context
from discord.utils import get

from modules.commands.base import BaseCommand
from modules.commands.utils import get_bits_server
from modules.database.masterData import MasterData


class User(BaseCommand):

    def __init__(self, context: Context, client, email):
        super().__init__(context)
        self.email = email
        self.client = client
        self.guild = get_bits_server(self.client)
        self.author = get(self.guild.members, id=context.author.id)

    async def apply(self):
        data = MasterData.getInstance()
        user = data.get_user_email(self.email)
        if user is None:
            await self.author.send("User not logged in")
        else:
            await self.author.send("User logged in")
