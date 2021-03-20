""" 
Hey! Welcome to bot_commands.py!
Thanks for stopping by, if you are an experienced bot developer in python
this is probably not the best repo for you to be...

I don't usually comment my code, this is new to me.. if it is not the best, that's my reason.

Anyways, this has been Inf3xt, but I'm out. Have fun making a bot in python!
"""
# Imports and stuff
import discord
from discord.ext import commands

token = "" # This is not recommended, you should use json, database or an external file
command_prefix = "." # This is how to call the command(s).
# I honestly hope you know about variables...
# This can be anything...
bot = commands.Bot(command_prefix=command_prefix)

# This is the more confusing way to do commands... in my opinion.

@bot.event
async def on_ready(): # This will be called when the bot connection is initiated
    print(f"You are connected to {bot.user.name}")
    # This will print to the console:
    # You are connected to <bot username>

@bot.event
async def on_message(message): # From what I know, this *should* be message as the function parameter
    if message.author.id == bot.user.id: # To check if the message is what the bot said, if so, it will not respond to it.
        return

    # Using message.content.lower() is better...
    # I hope you know what it does. If not, I suggest you learn basic python strings
    # Also you must use message.content, using message by itself, will throw an error, please try it, experience the world of errors! 

    if message.content.lower() == "hey!":
        await message.channel.send("Hey back to you!") # When the user says "hey!", the bot will reply back with "Hey back to you!" but you can change this if you want to.

    if message.content.lower() == "bye!":
        await message.channel.send("Bye!") # I mean same here, I thought that was obvious...

    await bot.process_commands(message) # This is to use other bot.command() commands aswell as on_message, this evidently uses the command_prefix. For more info, look at bot_commands.py :D

try:
    bot.run(token) # This will initialise the bot connection to discord
except discord.errors.LoginFailure:
    print("That token does not work!")
    exit(0) # Ends program if failure.