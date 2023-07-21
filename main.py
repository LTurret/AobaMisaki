from os import getenv
from os import listdir
from os import system

from dotenv import load_dotenv

from interactions import listen
from interactions import Activity
from interactions import Client
from interactions import Intents

load_dotenv()

arisa = Client(
    intents = Intents.ALL,
    activity = Activity(
        name = "⛔擔當申請目前無法使用"
    )
)

@listen()
async def on_startup():
    system("clear")
    print(f"MLTD 啟動！！！")

for filename in listdir("./cogs"):
    if filename.endswith(".py"):
        print(f"Loading extension: {filename}")
        arisa.load_extension(f"cogs.{filename[:-3]}")

print("Starting...")

arisa.start(getenv("BOT_TOKEN"))