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

@bot.command(name="ban", description="Bannir un membre du serveur")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    """
    Bannir un membre du serveur.

    Args:
        ctx (discord.Context): Le contexte de la commande.
        member (discord.Member): Le membre à bannir.
        reason (str, optional): La raison du ban. Defaults to None.
    """
    try:
        await member.ban(reason=reason)
        await ctx.send(f"{member.mention} a été banni du serveur.")
    except discord.Forbidden:
        await ctx.send("Je n'ai pas les permissions pour bannir ce membre.")
    except discord.HTTPException as e:
        await ctx.send(f"Erreur : {e.text}")