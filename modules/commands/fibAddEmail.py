from discord.ext.commands import Context
from discord.utils import get

from get_enviroment import UNIVERSITY_EMAIL
from modules.commands.base import BaseCommand
from modules.commands.utils import get_bits_server
from modules.database.masterData import MasterData


class FIBAddEmail(BaseCommand):
    email = ""

    def __init__(self, context: Context, email, client):
        super().__init__(context)
        self.email = email
        self.client = client
        self.guild = get_bits_server(self.client)
        self.author = get(self.guild.members, id=context.author.id)

    async def apply(self):
        data = MasterData.getInstance()
        user = data.get_user_dc(self.author.id)
        if user.is_fib():
            await self.ctx.send("Your email is already added")
        elif UNIVERSITY_EMAIL in self.email:
            user.add_fib_mail(self.email)
            await self.ctx.send("UPC email added!")
        else:
            await self.ctx.send("Wrong UPC email format")
