from Commands.Config.Config import *
from Commands.Config.Util import *

try:
    import discord
    from discord.ext import commands
    import datetime

    intents = discord.Intents.default()
    intents.messages = True
    intents.guilds = True

    bot = commands.Bot(command_prefix=PREFIX, intents=intents, help_command=None)

    class Command(commands.Cog):
        def __init__(self, bot):
            self.bot = bot

        @commands.command()
        async def help(self, ctx):
            command_logs("help")
            try:
                    embed = discord.Embed(
                        title = "Help", 
                        color = discord.Color(int(f"0x{EMBED_COLOR}", 16)),
                        timestamp = datetime.datetime.utcnow()
                    )
                    embed.add_field(name=f"{PREFIX}links", value=f"Allows you to see all of the owner links.", inline=False)
                    embed.add_field(name=f"{PREFIX}userinfo `[id]`", value=f"Allows you to retrieve information about a user.", inline=False)
                    embed.add_field(name=f"{PREFIX}ipinfo `[ip]`", value=f"Allows you to retrieve information from an IP.", inline=False)
                    embed.add_field(name=f"{PREFIX}numberinfo `[number]`", value=f"Allows you to retrieve information from a phone number.", inline=False)
                    embed.add_field(name=f"{PREFIX}cryptoprice `[CRYPTO]/[MONEY]`", value=f"Allows you to retrieve the price of a cryptocurrency.", inline=False)
                    embed.add_field(name=f"{PREFIX}ban `[User]/[Raison]`", value=f"Allows you to ban a user.", inline=False)
                    embed.add_field(name=f"{PREFIX}kick `[User]/[Raison]`", value=f"Allows you to kick a user.", inline=False)
                    embed.add_field(name=f"{PREFIX}ping ", value=f"Allows you to see the ping of the bot.", inline=False)
                    await ctx.send(embed=embed)
            except Exception as e:
                    await ctx.send(error_message(e))

    def setup(bot):
        bot.add_cog(Command(bot))

except Exception as e:
    error_logs(e)
