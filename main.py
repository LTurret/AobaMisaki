import json, os

import discord
from discord.ext import commands

with open("./config/token.json", mode="r") as token:
    token = json.load(token)

intents = discord.Intents.default()
intents.members = True

Misaki = commands.Bot(command_prefix="+", intents=intents)
Misaki.remove_command("help")

@Misaki.event
async def on_ready():
    await Misaki.change_presence(status = discord.Status.online, activity = discord.Game("偶像大師 百萬人演唱會！ 劇場時光"))
    os.system("clear")
    print(f"Uptime")

for filename in os.listdir("./cogs/command"):
    if filename.endswith(".py"):
        print(f"Loading commands extension: {filename}")
        Misaki.load_extension(f"cogs.command.{filename[:-3]}")

print("Booting...")

Misaki.run(token["token"])