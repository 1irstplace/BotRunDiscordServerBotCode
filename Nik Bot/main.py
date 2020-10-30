import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix='.')
token = open('Nik Bot/token.txt').read()
nikword = open('Nik Bot/nikword.txt').read()

@client.event
async def on_ready():
    print('ready')

@client.event
async def on_message(message):
    channel = message.channel
    chance = random.randint(1, 1000)
    nimrod_chance = random.randint(1, 100)
    if(message.author != client.user):
        if(chance <= 150 and nimrod_chance >= 6):
            await channel.send(nikword)
            await channel.send(nikword)
        elif(nimrod_chance <= 6):
            await channel.send('nimrod')
            await channel.send('nimrod')
        


client.run(token)