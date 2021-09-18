import asyncio
import discord
import os
import random

from dotenv import load_dotenv

# Load Token from .env file.
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('GUILD_ID')

# Set up Client.
client = discord.Client()


# Startup and Status change loop.
@client.event
async def on_ready():
    print('{0.user} is ready!'.format(client))

    while True:
        # Coding Status
        await client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="Rhbarber suffering while coding me",
                                      url="https://rhbarber.com"))
        await asyncio.sleep(10)

        # Guild Online Members Status.
        guild = client.get_guild(int(GUILD))  # Server ID got from .ENV file.
        if len(guild.members) == 1:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                                   name=f"{len(guild.members)} user."))
            await asyncio.sleep(10)
        else:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                                   name=f"{len(guild.members)} users."))
            await asyncio.sleep(10)

        # Random Member Watching Status.
        chosen = random.choice(guild.members)
        chosen = chosen.name
        await client.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name=f"{chosen} 👀"))
        await asyncio.sleep(10)


# Message Events
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send("Hello!")


# Run bot.
client.run(TOKEN)
