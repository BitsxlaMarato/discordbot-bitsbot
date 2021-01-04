from discord.ext.commands import Context
from discord.utils import get

from modules.commands.base import BaseCommand
from modules.commands.utils import get_bits_server
from modules.database.masterData import MasterData


class Info(BaseCommand):

    def __init__(self, context: Context, client, user_id):
        super().__init__(context)
        i = 0
        for c in user_id:
            if c.isdigit():
                break
            else:
                i += 1
        self.user_id = int(user_id[i:-1])
        self.client = client
        self.guild = get_bits_server(self.client)
        self.author = get(self.guild.members, id=context.author.id)

    async def apply(self):
        data = MasterData.getInstance()
        user_author = data.get_user_dc(self.user_id)
        if user_author is None:
            await self.author.send("User not logged in")
        else:
            await self.author.send(
                ("Name: %s \n" % user_author.name) +
                ("Last Name: %s \n" % user_author.last_name) +
                ("Email: %s \n" % user_author.email) +
                (("UPC email: %s \n" % user_author.email_uni) if user_author.is_fib() else "") +
                ("Has team: %s \n" % ("Yes" if user_author.has_team else "No")) +
                (("Team: %s \n" % user_author.team) if user_author.has_team else "")
            )
