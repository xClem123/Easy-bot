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

@bot.command(name="kick", description="Expulser un membre du serveur")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    """
    Expulser un membre du serveur.

    Args:
        ctx (discord.Context): Le contexte de la commande.
        member (discord.Member): Le membre à expulser.
        reason (str, optional): La raison de l'expulsion. Defaults to None.
    """
    try:
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} a été expulsé du serveur.")
    except discord.Forbidden:
        await ctx.send("Je n'ai pas les permissions pour expulser ce membre.")
    except discord.HTTPException as e:
        await ctx.send(f"Erreur : {e.text}")