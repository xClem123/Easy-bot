from Commands.Config.Config import *

import colorama
import discord
import datetime
from discord.ext import commands
import sys
import os

color = colorama.Fore
red = color.RED
white = color.WHITE
reset = color.RESET
command = f"{red}[{white}>{red}] |"
info = f"{red}[{white}!{red}] |"
error = f"{red}[{white}x{red}] |"

def command_logs(command_name):
    print(f"{red}{command} Command: {white}{command_name}{red}{reset}")

def error_logs(e):
    print(f"{red}{error} Error: {white}{e}{red}{reset}")

def error_message(e):
    message = f"""# Error:
```{e}```"""
    return message

def Clear():
    if sys.platform.startswith("win"):
        "WINDOWS"
        os.system("cls")
    elif sys.platform.startswith("linux"):
        "LINUX"
        os.system("clear")