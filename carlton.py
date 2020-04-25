# carlton.py
import os

import discord
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$help'):
        # return message to channel with supported commands
        pass

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$start-server'):
        # sends command to lambda endpoint to start the EC2 instance
        pass

    if message.content.startwith('$stop-server'):
        # sends commands to manually stop server
        pass

    if message.content.startswith('$')

client.run(TOKEN)
