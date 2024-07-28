import os
import discord
from Commands.Config.Config import *
from Commands.Config.Util import *
from discord.ext import commands

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True 
intents.members = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

@bot.event
async def on_ready():
    Clear()
    await bot.change_presence(activity=discord.Game(name=f"Prefix: {PREFIX}"))
    print(f"""
{red}> Invite   : {white}https://discord.com/oauth2/authorize?client_id={bot.user.id}&scope=bot&permissions=8{red}
{red}> Username : {white}{bot.user.name}{red}
{red}> Tag      : {white}#{bot.user.discriminator}{red}
{red}> Id       : {white}{bot.user.id}{red}
{red}> Prefix   : {white}{PREFIX}{red}

{red}Logs:{reset}""")
    print(f'{color.RED}{info} Bot online.{color.RESET}')

try:
    bot.load_extension("Commands.help")
    bot.load_extension("Commands.links")
    bot.load_extension("Commands.userinfo")
    bot.load_extension("Commands.ipinfo")
    bot.load_extension("Commands.numberinfo")
    bot.load_extension("Commands.cryptoprice")
    bot.load_extension("Commands.ban")
    bot.load_extension("Commands.kick")
    bot.load_extension("Commands.ping")
    bot.load_extension("Commands.CommandsOwner.helpowner")
    bot.load_extension("Commands.CommandsOwner.sendmpmessage")
    bot.load_extension("Commands.CommandsOwner.sendembed")
    bot.run(TOKEN)
except Exception as e:
    print(f"Error: {e}")
