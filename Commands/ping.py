import discord
from discord.ext import commands
from Commands.Config.Config import *

class Command(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", description="Afficher le ping du bot")
    async def ping(self, ctx):
        """
        Afficher le ping du bot.

        Args:
            ctx (discord.Context): Le contexte de la commande.
        """
        try:
            embed = discord.Embed(title="Pong !", color=discord.Color.green())
            embed.add_field(name="Mon ping est de", value=f"{self.bot.latency * 1000:.2f} ms", inline=False)
            await ctx.send(embed=embed)
        except discord.HTTPException as e:
            await ctx.send(f"Erreur HTTP : {e}")
        except Exception as e:
            await ctx.send(f"Erreur inconnue : {e}")

def setup(bot):
    bot.add_cog(Command(bot))