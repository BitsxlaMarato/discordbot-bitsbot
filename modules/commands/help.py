from discord.ext.commands import Context
from discord.utils import get

from modules.commands.base import BaseCommand
from modules.commands.utils import get_bits_server


class Help(BaseCommand):

    def __init__(self, context: Context, client):
        super().__init__(context)
        self.client = client
        self.guild = get_bits_server(self.client)
        self.author = get(self.guild.members, id=context.author.id)

    async def apply(self):
        commands = ("List of Random commands (They only work in random and memes channel):\n" +
                    "```" +
                    "bits!cat\n" +
                    "bits!dog\n" +
                    "bits!parrot\n" +
                    "bits!biene\n" +
                    "bits!ping\n" +
                    "bits!proJoke\n" +
                    "bits!parJoke\n" +
                    "bits!joke\n" +
                    "```\n"
                    )
        roles = [y.name.lower() for y in self.author.roles]
        if "hackers" in roles:
            commands += ("Please use this next commands wisely, any abuse of these commands will be banned.\n" +
                         "List of Hacker commands:\n" +
                         "```" +
                         "bits!login [RegisterEmail] -> Check in\n" +
                         "bits!createTeam [nameTeam] -> If you don't have a team and you want to create one\n" +
                         "bits!addToTeam [@personToAddToYourTeam] -> The user you want to add to the team must be " +
                         "logged in and with no team\n" +
                         "```\n")
        if "organizers" in roles:
            commands += ("List of Organizer commands:\n" +
                         "```" +
                         "bits!info [@personToGetInfo] -> Send a private message to you with the information of this " +
                         "user\n" +
                         "bits!email [@personToGetInfo] -> Send a private message to you with the email of this user\n" +
                         "bits!loginEmail -> Send a private message to you with all the emails logged in\n" +
                         "```\n")
        await self.author.send(commands)
