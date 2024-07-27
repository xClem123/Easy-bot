from Commands.Config.Config import *
from Commands.Config.Util import *

try:
    import discord
    from discord.ext import commands
    import datetime

    class Command(commands.Cog):
        def __init__(self, bot):
            self.bot = bot

        @commands.command(aliases=['invite', 'link', 'add', 'discord', 'server', 'github', 'website', 'site', 'tool', 'addme', 'telegram', 'canal'])
        async def links(self, ctx):
            command_logs("links")
            try:
                    embed = discord.Embed(
                        title = "Links",
                        description = f"""
- <:links_logo_red:1193987708113141830> [Discord Server](https://{discord_server})
- <:website_logo_red:1188140372879216801> [Website](https://{website})
- <:telegram_logo_red:1227740512824332310> [Telegram](https://{telegram})
- <:github_logo_red:1188139048393506837> [Tool Github](https://{github_tool})""",
                        color = discord.Color(int(f"0x{EMBED_COLOR}", 16)),
                        timestamp = datetime.datetime.utcnow()
                    )
                    await ctx.send(embed=embed)
            except Exception as e:
                    await ctx.send(error_message(e))

    def setup(bot):
        bot.add_cog(Command(bot))
except Exception as e:
    error_logs(e)