import discord
from discord.exe import commands
import os
import requests
import json
import random
from replit import db

#sets the prefix to all commands to "/"
client = commands.Bot(command_prefix = "/")

#tells us when the bot is ready
@client.event
async def on_ready():
  print("Bot is ready")

@client.command(aliases = ['hi', 'Hi', 'Hello', 'sup', 'hey', 'Hey', 'Sup', 'wassup', 'Wassup'])
async def hello(ctx):
  await ctx.send("Hey there! How are you doing?")

#add more aliases
@client.command(aliases = ['Good', 'great', 'Great'])
async def good(ctx):
  await ctx.send("That's great! I wish you the best!")

@client.command(aliases = ['Bad'])
async def bad(ctx):
  await ctx.send("Sorry to hear that :(! Hope it gets better!")

@client.command(aliases = ['Okay'])
async def okay(ctx):
  await ctx.send("That's nice! Stick around and your day is going to be better than ever!")

@client.command(aliases = ['anime'])
async def anime(ctx):
  await ctx.send("You like anime? Me too! Name a genre you want, and i'll reccomend you some animes in that genre! All you have to do is type, /action, /romance, /horror, /mystery")

@client.command(aliases = ['action'])
async def action(ctx):
  await ctx.send("Some action animes are: One Piece, Naruto, Jujutsu Kaisen, Dororo, Demon Slayer, Hunter x Hunter, Attack on Titan, Tokyo Ghoul, Assasination Classroom")

#add to the list of commands
@client.command()
async def help(ctx):
  await ctx.send("Here are a list of some things you can ask me or command me to do: ")
  await ctx.send("/hello (or other greetings)")
  await ctx.send("/good, /bad - generic responses to 'How are you doing?'")



#add connection to the discord bot