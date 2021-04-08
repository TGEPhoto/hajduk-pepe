  
import aiohttp
import discord
import os
from keys import bot as BOT_TOKEN
from discord.ext import commands

bot = commands.Bot(command_prefix=".", owner_ids=[611540017000480773])