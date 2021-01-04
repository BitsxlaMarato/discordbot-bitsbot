import discord
from discord.utils import get

from get_enviroment import SERVER_NAME


def get_bits_server(client):
    for guild in client.guilds:
        if guild.name == SERVER_NAME:
            return client.get_guild(guild.id)


async def create_team(guild, team):
    team_role = await guild.create_role(name=team)

    i = 0
    category = get(guild.categories, name="Hackers-%d" % i)
    while len(category.channels) >= 48:
        i += 1
        category = get(guild.categories, name="Hackers-%d" % i)

    voice_channel = await category.create_voice_channel(team.replace(" ", "-").lower())
    text_channel = await category.create_text_channel(team.replace(" ", "-").lower())

    overwrite_text = discord.PermissionOverwrite(read_messages=True, send_messages=True,
                                                 add_reactions=True)
    overwrite_voice = discord.PermissionOverwrite(connect=True, speak=True, stream=True, view_channel=True)
    await text_channel.set_permissions(team_role, overwrite=overwrite_text)
    await voice_channel.set_permissions(team_role, overwrite=overwrite_voice)

    return team_role
