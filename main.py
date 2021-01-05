### READ ME: ###
# Script developed by MemeSkeleton. If you want to help with developing, debugging, etc., 
# please contact me at MemeSkeleton#3775 on Discord.
# Also developed with the assistance of Ghost Cray.

# INFO:
# For any commands that have "while True:" in the code, do not use those more than one of those commands
# at a time. It will break the bot.
# As of 5 Janurary 2021, there is no way to stop any looping commands. Simply stop the script to reset it.
# This script has only been tested on self botted accounts. It is unknown if it will work on actual bots.
# This script was deisgned for use on the online IDE Repl.it . Please contact me if you know how to get it running on other IDEs,
# or if it can run on other IDEs at all.
# If you are going to use the Repl.it IDE, and wish to have the script run 24/7 in
# the background, please contact me for instructions on how to do so.



# Imports necessary modules.
import discord
from discord.ext import commands
from discord.ext import tasks, commands
import asyncio
import time
import keep_alive
import os

# Reports in the terminal when the bot is ready to be ready. Also sets the command prefix to ~ ( a tilde.)
client = commands.Bot(command_prefix='~', self_bot=True)
@client.event
async def on_ready():
  print("Automation online. Trigger to start.")

# Automatically does "pls beg" in a server with Dank Memer. 
# Activated by sending "~trigger" using the automated account.
# Only works in a server with dankmemer.
@client.command(pass_context=True)
async def dankmemer(ctx):
      print("Dankmemer automation triggered.")
      while True:
        time.sleep(46)
        await ctx.send("pls beg")
        
# Bumps a server every 2 hours on Disboard.
# Activated by sending ~autobump using the automated account.
# Only works on a server with Disboard.
async def autobump(ctx):
     while True:
        time.sleep(7250)
        await ctx.send("!d bump")
















client.run("token", bot=False)



















































































# SCRIPT CODE ARCHIVE -- CODE CUT FROM SCRIPT BUT MAY POSSIBLY BE REINSERTED LATER
# <# Insert the self botted user's token in "token". Watch this video if you want to find your token. 
# # Follow its instructions but use the Google Chrome browser. DO NOT SHARE YOUR TOKEN WITH ANYBODY.
# keep_alive.keep_alive()> [code went above client.run("token", bot=False) ]