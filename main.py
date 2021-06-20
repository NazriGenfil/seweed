import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("TOKEN")

client = commands.Bot(command_prefix='_')


@client.event
async def on_ready():
    print("THE BOT IS READY")


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')
    print('load ' + extension)


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    print('unload ' + extension)


@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')
    print('reload ' + extension)


# for filename in os.listdir('./cogs'):
#     if filename.endswith('.py'):
#         client.load_extension(f'cogs.{filename[:-3]}')
#         print(filename[:-3])

client.run(TOKEN)
