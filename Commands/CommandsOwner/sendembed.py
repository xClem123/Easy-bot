from Commands.Config.Config import *
from Commands.Config.Util import *

try:

    import discord
    from discord.ext import commands
    import time
    import datetime
    import re

    class Command(commands.Cog):
        def __init__(self, bot):
            self.bot = bot

        @commands.command()
        async def sendembed(self, ctx, *, args: str):
            if ctx.author.id != CREATOR_ID:
                await ctx.send("**You are not authorized to use this command.**")
                return

            command_logs("sendembed")
            try:
                title_match = re.search(r'TITLE=="""(.*?)"""', args, re.DOTALL)
                description_match = re.search(r'DESCRIPTION=="""(.*?)"""', args, re.DOTALL)
                image_match = re.search(r'IMAGE=="""(.*?)"""', args, re.DOTALL)
                thumbnail_match = re.search(r'THUMBNAIL=="""(.*?)"""', args, re.DOTALL)

                embed = discord.Embed(
                    color=discord.Color(int(f"0x{EMBED_COLOR}", 16)),
                    timestamp=datetime.datetime.utcnow()
                )

                if title_match:
                    title = title_match.group(1).strip()
                    embed.title = title

                if description_match:
                    description = description_match.group(1).strip()
                    embed.description = description

                if image_match:
                    image_url = image_match.group(1).strip()
                    embed.set_image(url=image_url)
                
                if thumbnail_match:
                    thumbnail_url = thumbnail_match.group(1).strip()
                    embed.set_thumbnail(url=thumbnail_url)
                
                await ctx.send(embed=embed)
            except Exception as e:
                await ctx.send(error_message(e))

    def setup(bot):
        bot.add_cog(Command(bot))

except Exception as e:
    error_logs(e)