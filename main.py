import discord
from discord.exe import commands
import os
import requests
import json
import random
from replit import db

#sets the prefix to all commands to "/"
client = commands.Bot(command_prefix = "/")
message_client = discord.Client()
command_list = ['/hello', '/help', '/good', '/bad', 'okay', 'anime']
check = False

#tells us when the bot is ready
@client.event
async def on_ready():
  print("Bot is ready")

@message_client.event
async def message_client_ready():
  print("Message client ready")

@client.command(aliases = ['hi', 'Hi', 'Hello', 'sup', 'hey', 'Hey', 'Sup', 'wassup', 'Wassup'])
async def hello(ctx):
  await ctx.send("Hey there! How are you doing?")
  check = True

#add more aliases
@client.command(aliases = ['Good', 'great', 'Great'])
async def good(ctx):
  await ctx.send("That's great! I wish you the best!")
  check = True

@client.command(aliases = ['Bad'])
async def bad(ctx):
  await ctx.send("Sorry to hear that :(! Hope it gets better!")
  check = True

@client.command(aliases = ['Okay'])
async def okay(ctx):
  await ctx.send("That's nice! Stick around and your day is going to be better than ever!")
  check = True

@client.command(aliases = ['Anime'])
async def anime(ctx):
  await ctx.send("You like anime? Me too! Name a genre you want, and i'll recommend you some animes in that genre! All you have to do is type, /action, /romance, /horror, /other")
  check = True

@client.command(aliases = ['Action'])
async def action(ctx):
  await ctx.send("Some action animes are: One Piece, Naruto, Jujutsu Kaisen, Black Clover, Dororo, Demon Slayer, Hunter x Hunter, Attack on Titan, Tokyo Ghoul, Assasination Classroom")
  check = True

@client.command(aliases = ['Romance'])
async def romance(ctx):
  await ctx.send("Some romance animes are: Rascal Does Not Dream of Bunny Girl Senpai, Silent Voice, Your Lie in April, Oregairu, Your Name, Fly Me To The Moon, FireWorks, Plastic Memories")
  check = True

@client.command(aliases = ['Horror'])
async def horror(ctx):
  await ctx.send("Some horror animes are: Beyond the Boundary, Blue Exorcist, Full Metal Alchemist, Another, The Promised Neverland")
  check = True

@client.command(aliases = ['Other'])
async def other(ctx):
  await ctx.send("Death Note, Code Geass: LeLouch of Rebellion, Dr.Stone, Tower of God, Classroom of Elite, Darling in the Franxx, Fairy Tail, Wise Mans Grandchild, Haikyuu!, Kuroko's Basketball")
  check = True

#add to the list of commands
@client.command()
async def help(ctx):
  await ctx.send("Here are a list of some things you can ask me or command me to do: ")
  check = True
  global check
  for command in command_list:
    await ctx.send(command)
  await ctx.sent("You can also say things similar to the words above.")

@message_client.event()
async def on_message(message):
  global check
  if message.author == client.user:
    return

  if check == True:
    check = False
  else:
    await message.channel.send("Sorry I don't understand. Please type '/help' for a list of things you can say to me!")
  
  

#add connection to the discord bot
client.run(os.environ['TOKEN'])
message_client.run(os.environ['TOKEN'])