from Commands.Config.Config import *
from Commands.Config.Util import *

try:
    import discord
    from discord.ext import commands
    import datetime
    import requests

    class Command(commands.Cog):
        def __init__(self, bot):
            self.bot = bot

        @commands.command()
        async def cryptoprice(self, ctx, *, symbol: str = None):
            command_logs("cryptoprice")

            if symbol is None:
                await ctx.send(f"{ctx.author.mention}: **Invalid Symbol.** \nExample: BTC/USDT")
                return

            try:
                if not symbol.islower():
                    if "/" in symbol:
                        crypto, _, money = symbol.partition('/')
                        symbol = crypto + money
                    else:
                        await ctx.send(f"{ctx.author.mention}: **Invalid Symbol.** \nExample: BTC/USDT")
                        return
                else:
                    await ctx.send(f"{ctx.author.mention}: **Invalid Symbol.** \nExample: BTC/USDT")
                    return

                api_url = "https://api.binance.com/api/v3/ticker/price"
                params = {"symbol": symbol}
                response = requests.get(api_url, params=params)
                if response.status_code == 200:
                    data = response.json()
                    cryptoprice = float(data["price"])

                    embed = discord.Embed(
                        title="Crypto Price", 
                        color=discord.Color(int(f"0x{EMBED_COLOR}", 16)),
                        description=f"""**Crypto:** {crypto}
**Money:** {money}
**{crypto} Price:** {'{:.8f}'.format(cryptoprice)} {money}""",
                        timestamp=datetime.datetime.utcnow()
                    )

                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"{ctx.author.mention}: **Crypto cannot be found.**")
            except Exception as e:
                error_message(e)

    def setup(bot):
        bot.add_cog(Command(bot))
except Exception as e:
    error_logs(e)