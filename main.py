import json, os

import interactions, discord
from discord.ext import commands

with open("./config/token.json", mode="r") as token:
    token = json.load(token)

Interactions = interactions.Client(token=token["token"], intents=interactions.Intents.ALL)
Misaki = commands.Bot(command_prefix="+")
Misaki.remove_command("help")

@Misaki.event
async def on_ready():
    await Misaki.change_presence(status = discord.Status.online, activity = discord.Game("偶像大師 百萬人演唱會！ 劇場時光"))
    os.system("cls")
    print(f"Uptime")

for filename in os.listdir("./cogs/components"):
    if filename.endswith(".py"):
        print(f"Loading components/interactions extension: {filename}")
        Interactions.load(f"cogs.components.{filename[:-3]}")

for filename in os.listdir("./cogs/commands"):
    if filename.endswith(".py"):
        print(f"Loading commands extension: {filename}")
        Misaki.load_extension(f"cogs.commands.{filename[:-3]}")

print("Booting...")

Misaki.run(token["token"])