import json
import os
import time
from time import gmtime, strftime
from datetime import datetime
from TenorGrabber import tenorgrabber
import nextcord as discord
import asyncio
from dotenv import load_dotenv
from nextcord.ext import commands


load_dotenv()
channels = []
staff = []
owner = os.getenv("BOT_OWNER")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


def updatechannelsjson():
    with open("channels.json", "w", encoding="utf-8") as channelsfile:
        json.dump(channels, channelsfile, indent=2)
        print(channels)
        print("Updated channels.json")


def openchannelsjson():
    with open("channels.json", "r", encoding="utf-8") as channelsfile:
        channels = json.load(channelsfile)
        print("Loaded channels.json")


def updatestaffjson():
    with open("staff.json", "w", encoding="utf-8") as stafffile:
        if owner not in staff:
            staff.append(int(owner))
        print(staff)
        json.dump(staff, stafffile, indent=2)
        print("Updated staff.json")


def openstaffjson():
    with open("staff.json", "r", encoding="utf-8") as stafffile:
        if owner not in staff:
            staff.append(int(owner))
        staff = json.load(stafffile)
        print("Loaded staff.json")


@client.event
async def on_ready():
    server_count = len(client.guilds)
    await client.change_presence(
        activity=discord.Activity(
            type=discord.ActivityType.watching, name=f"{server_count} Servers"
        )
    )
    print("[ OK ] Logging in...")
    print(f"[ INFO ] Logged in as {client.user}.")
    for guilds in client.guilds:
        print(f"Server: {guilds.name}")


if not os.path.isfile("channels.json"):
    with open("channels.json", "w", encoding="utf-8") as channelsfile:
        json.dump(channels, channelsfile, indent=2)
        print("Created channels.json")
else:
    with open("channels.json", "r", encoding="utf-8") as channelsfile:
        print(f"[ .. ] Loading file 'channels.json'...")
        channels = json.load(channelsfile)
        print(f"[ OK ] Loading file 'channels.json'...")
if not os.path.isfile("staff.json"):
    with open("staff.json", "w", encoding="utf-8") as stafffile:
        if owner not in staff:
            staff.append(int(owner))
        json.dump(staff, stafffile, indent=2)
        print("Created staff.json")
else:
    with open("staff.json", "r", encoding="utf-8") as stafffile:
        print(f"[ .. ] Loading file 'staff.json'...")
        if owner not in staff:
            staff.append(int(owner))
        staff = json.load(stafffile)
        print(f"[ OK ] Loading file 'staff.json'...")
for script in os.listdir("src"):
    fulldir = os.path.join("src", script)
    if os.path.isfile(fulldir):
        with open(fulldir, "r", encoding="utf-8") as pyscript:
            print(f"[ .. ] Loading file '{pyscript.name}'...")
            exec(pyscript.read())
            print(f"[ OK ] Loading file '{pyscript.name}'...")

print("[ .. ] Logging in...")
client.run(os.getenv("DISCORD_TOKEN"))
