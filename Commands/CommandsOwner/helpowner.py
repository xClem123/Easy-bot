
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
        async def helpowner(self, ctx):
            if ctx.author.id != CREATOR_ID:
                await ctx.send("**You are not authorized to use this command.**")
                return
            
            command_logs("helpowner")
            try:
                    embed = discord.Embed(
                        title = "Help Owner", 
                        color = discord.Color(int(f"0x{EMBED_COLOR}", 16)),
                        timestamp = datetime.datetime.utcnow()
                    )
                    embed.add_field(name=f"{PREFIX}sendmpmessage `[message]`", value=f"Allows you to send a pm message to all server users.", inline=False)
                    embed.add_field(name=f'{PREFIX}sendembed `[description]     [title]`', value=f"Allows you to send an embed in the channel.", inline=False)
                    await ctx.send(embed=embed)
            except Exception as e:
                    await ctx.send(error_message(e))

    def setup(bot):
        bot.add_cog(Command(bot))
except Exception as e:
    error_logs(e)