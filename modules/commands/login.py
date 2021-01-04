import discord
from discord.ext.commands import Context
from discord.utils import get

from modules.commands.base import BaseCommand
from modules.commands.utils import get_bits_server, create_team
from modules.database.masterData import MasterData


class LoginCommand(BaseCommand):
    email = ""

    def __init__(self, context: Context, email, client):
        super().__init__(context)
        self.email = email
        self.client = client
        self.guild = get_bits_server(self.client)
        self.author = get(self.guild.members, id=context.author.id)

    async def apply(self):
        data = MasterData.getInstance()
        user = data.get_user_email(self.email)
        if user is None:
            await self.ctx.send("Whoops, the email is wrong. Are you sure you used this email to register to "
                                "BitsxLaMaratò?")
        elif user.is_logged():
            await self.ctx.send("You were already logged in")
        else:
            data.login(self.author.id, user)
            data.save_data()
            hacker_role = get(self.guild.roles, name='Hackers')
            await self.author.add_roles(hacker_role)
            await self.ctx.send(("Hi %s, you have registered BitsxLaMaratò!" % user.name))
            if user.is_fib():
                await self.ctx.send("UPC email detected!")
            else:
                await self.ctx.send("Are you studying at FIB UPC? Register now your university email with the "
                                    "command: bits!FIBAddEmail example@estudiantat.upc.edu")
            if user.has_team:
                await self.ctx.send(("Team detected! Joining %s" % user.team))
                team_role = get(self.guild.roles, name=user.team)
                if team_role is not None:
                    await self.author.add_roles(team_role)
                else:
                    team_role = await create_team(guild=self.guild, team=user.team)

                    await self.author.add_roles(team_role)

                    await self.ctx.send("You are ready to go")
            else:
                await self.author.send("You have no team. :(\nYou can go and take a look at the #search_team channel")

