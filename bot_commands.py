""" 
Hey! Welcome to bot_commands.py!

Thanks for stopping by, if you are an experienced bot developer in python
this is probably not the best repo for you to be...

I don't usually comment my code, this is new to me.. if it is not the best, that's my reason.

Anyways, this has been Inf3xt, 👋. Have fun making a bot in python!
"""

# Imports and stuff
import discord
from discord.ext import commands

token = "" # This is not recommended, you should use json, database or an external file
command_prefix = "." # This is how to call the command(s).
# I honestly hope you know about variables...
# This can be anything...
bot = commands.Bot(command_prefix=command_prefix)

# Note:
# bot.event is VERY different to bot.command(), notice the ()
# bot.event is for events that are called when a user does something in particular
# bot.command() is for calling commands, hence the decorator <-- I REALLY HOPE YOU KNOW WHAT THAT IS.. woah *caps*

@bot.event
async def on_ready(): # This will be called when the bot connection is initiated
    print(f"You are connected to {bot.user.name}")
    # This will print to the console:
    # You are connected to <bot username>

@bot.command()
async def echo(ctx, arg1=""): # You can add parameters here, they can also be optional as seen below.
    if not arg1:
        await ctx.send("Please enter an arguement to repeat!")
    else:
        await ctx.send(f"You said: {arg1}") # God I hope you know about f strings.

@bot.command()
async def echo2(ctx, arg1=""):
    if not arg1:
        arg1 = "Hey there" # If not specified, this command will make arg1 "Hey there"
    await ctx.send(f"You said: {arg1}")

try:
    bot.run(token) # This will initialise the bot connection to discord
except discord.errors.LoginFailure:
    print("That token does not work!")
    exit(0) # Ends the program if failure.
