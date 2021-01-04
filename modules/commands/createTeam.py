from discord.ext.commands import Context
from discord.utils import get

from modules.commands.base import BaseCommand
from modules.commands.utils import get_bits_server, create_team
from modules.database.masterData import MasterData


class CreateTeam(BaseCommand):
    team = ""

    def __init__(self, context: Context, team, client):
        super().__init__(context)
        self.team = team
        self.client = client
        self.guild = get_bits_server(self.client)
        self.author = get(self.guild.members, id=context.author.id)

    async def apply(self):
        data = MasterData.getInstance()
        user = data.get_user_dc(self.author.id)
        if get(self.guild.roles, name=self.team) is not None:
            await self.ctx.send("This team already exists")
        elif user.has_team:
            await self.ctx.send("You already have a team")
        else:
            user.add_team(self.team)
            team_role = await create_team(guild=self.guild, team=user.team)
            await self.author.add_roles(team_role)
            data.save_data()
            await self.ctx.send("Team %s created" % self.team)
