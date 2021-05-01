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

@client.command(aliases = ['hi', 'Hi', 'Hello', 'sup', 'hey', 'Hey', 'Sup', 'wassup', 'Wassup'])
async def hello(ctx):
  await ctx.send("Hey there! How are you doing?")
  check = True
  global check


#add more aliases
@client.command(aliases = ['Good', 'great', 'Great'])
async def good(ctx):
  await ctx.send("That's great! I wish you the best!")
  check = True
  global check

#add 'bad' command

#add more commands

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
client.run(os.getenv('TOKEN'))
message_client.run(os.getenv('TOKEN'))