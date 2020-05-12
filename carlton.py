# carlton.py
import os
import discord
import requests
from libs import secrets
from libs import aws
from libs import giphy
from libs import custom_messages as cm

DISCORD_TOKEN = secrets.get_secret('DISCORD_TOKEN')

# All discord related functionality below here
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    elif message.content.startswith('$help'):
        # return message to channel with supported commands
        pass

    elif message.content.startswith('$hello'):
        # export this into a custom message module?
        greeting = cm.get_greeting()
        image = giphy.get_first_gif('carlton dance')
        await message.channel.send(greeting)
        await message.channel.send(image)

    elif message.content.startswith('$start'):
        image = giphy.get_first_gif('you got it')
        await message.channel.send(image)
        # probably should return the IP address of the new minecraft server
        server_state = aws.start_minecraft_server()
        await message.channel.send('Minecraft bedrock server started. Here\'s the server information')
        await message.channel.send(server_state)

    elif message.content.startswith('$stop'):
        image = giphy.get_first_gif('halt')
        await message.channel.send(image)
        aws.stop_minecraft_server()
        await message.channel.send('Minecraft server stopped.')

    elif message.content.startswith('$status'):
        # TODO: Implement messsage parsing
        resp = aws.check_minecraft_server_status()
        await message.channel.send(resp)

client.run(DISCORD_TOKEN)
