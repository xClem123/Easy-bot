from Commands.Config.Config import *
from Commands.Config.Util import *

try:
    import discord
    from discord.ext import commands
    import datetime
    import phonenumbers
    from phonenumbers import geocoder, carrier, timezone

    class Command(commands.Cog):
        def __init__(self, bot):
            self.bot = bot

        @commands.command(aliases=['numbergeo', 'geonumber'])
        async def numberinfo(self, ctx, *, phone_number: str = None):
            command_logs("numberinfo")

            if phone_number is None:
                await ctx.send(f"{ctx.author.mention}: **Invalid Number.** \nExample: +33612345678")
                return
            
            try:
                parsed_number = phonenumbers.parse(phone_number, None)
                if phonenumbers.is_valid_number(parsed_number):
                    if phone_number.startswith("+"):
                        country_code = "+" + phone_number[1:3]
                    else:
                        country_code = "None"
                    operator = carrier.name_for_number(parsed_number, "en")
                    type_number = "Mobile" if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE else "Fixed"
                    timezones = timezone.time_zones_for_number(parsed_number)
                    timezone_info = timezones[0] if timezones else None
                    country = phonenumbers.region_code_for_number(parsed_number)
                    region = geocoder.description_for_number(parsed_number, "en")
                    formatted_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.NATIONAL)
                    status = "Valid"

                    embed = discord.Embed(
                        title=f"Info: \"{phone_number}\":", 
                        color=discord.Color(int(f"0x{EMBED_COLOR}", 16)),
                        timestamp=datetime.datetime.utcnow()
                    )
                    embed.add_field(name="****Phone:****", value=f"```{phone_number}```", inline=True)
                    embed.add_field(name="****Formatted:****", value=f"```{formatted_number}```", inline=True)
                    embed.add_field(name="****Status:****", value=f"```{status}```", inline=True)
                    embed.add_field(name="****Country Code:****", value=f"```{country_code}```", inline=True)
                    embed.add_field(name="****Country:****", value=f"```{country}```", inline=True)
                    embed.add_field(name="****Region:****", value=f"```{region}```", inline=True)
                    embed.add_field(name="****Timezone:****", value=f"```{timezone_info}```", inline=True)
                    embed.add_field(name="****Operator:****", value=f"```{operator}```", inline=True)
                    embed.add_field(name="****Type Number:****", value=f"```{type_number}```", inline=True)
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(f"{ctx.author.mention}: **Invalid Number.** \nExample: +33612345678")
            except Exception as e:
                error_message(e)

    def setup(bot):
        bot.add_cog(Command(bot))

except Exception as e:
    error_logs(e)
