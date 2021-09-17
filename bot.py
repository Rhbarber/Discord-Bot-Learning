import discord
import os

from dotenv import load_dotenv

# Load Token from .env file.
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Set up Client.
client = discord.Client()


# Startup event.
@client.event
async def on_ready():
    print('{0.user} is ready!'.format(client))


# Message Events
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!hello'):
        await message.channel.send("Hello!")


# Run bot.
client.run(TOKEN)
