from discord.ext.commands import Context
from discord.utils import get

from modules.commands.base import BaseCommand
from modules.commands.utils import get_bits_server
from modules.database.masterData import MasterData


class AddToTeam(BaseCommand):
    user_id = None

    def __init__(self, context: Context, user, client):
        super().__init__(context)
        i = 0
        for c in user:
            if c.isdigit():
                break
            else:
                i += 1
        self.user_id = int(user[i:-1])
        self.client = client
        self.guild = get_bits_server(self.client)
        self.author = get(self.guild.members, id=context.author.id)

    async def apply(self):
        data = MasterData.getInstance()
        user_author = data.get_user_dc(self.author.id)
        dc_user_target = get(self.guild.members, id=self.user_id)
        user_taget = data.get_user_dc(self.author.id)
        team_role = get(self.guild.roles, name=user_author.team)
        if user_author is None:
            await self.ctx.send("Log in into bitsxLaMaratò 2020")
        elif team_role is None:
            await self.ctx.send("You have no team, search one first or create it")
        elif dc_user_target is None:
            await self.ctx.send("The user is incorrect. You have to mention the user with @")
        elif user_taget.has_team:
            await self.ctx.send("The user you mentioned has already a team")
        else:
            user_taget.addTeam(user_author.team.name)
            data.save_data()
            await dc_user_target.add_roles(team_role)
            await self.ctx.send("Member joined the %s team successfully" % user_author.team.name)
