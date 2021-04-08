import aiohttp
import discord
import os
from keys import bot as BOT_TOKEN
from discord.ext import commands

bot = commands.Bot(command_prefix=".", owner_ids=[611540017000480773])

@bot_event
async def onready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('koristi &help'))
    print('Bot je online')

@bot.command()
@commands.is_owner()
async def load(ctx, extension):
    bot.load_extension(f'cogs.{extension}')
    await ctx.send('\N{WHITE HEAVY CHECK MARK}')

@bot.command()
@commands.is_owner()
async def unload(ctx, extension):
    bot.unload_extension(f'cogs.{extension}')
    await ctx.send('\N{WHITE HEAVY CHECK MARK}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run(BOT_TOKEN)