import os
from datetime import datetime
from zoneinfo import ZoneInfo
import discord
from discord.ext import tasks
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

CHANNEL_NAME = "iracing-discussion"

INTRO_TEXT = "Don't forget - racing schedule for the following week! Here is what is on the schedule this week"

SERIES = [
    {
        "Name": "Tater's Summer Menu",
        "Day": "Tuesdays",
        "Details": [
            "Practice 7:00pm EST.",
            "Lone Qualifying: 15 minute @ 8:00pm EST.",
            "Race: After Qualifying.",
        ],
        "Races": [
                ("8/4", "Indianapolis Motor Speedway (Road course)"),
                ("8/11", "Charlotte Motor Speedway (You guessed it)"),  
        ],
    },
    {
        "Name": "Radical SR8 Cup",
        "Day": "Wednesdays",
        "Details": [
            "Practice 7:00pm EST. ",
            "Lone Qualifying: 15 minute @ 8:00pm EST. ",
            "Race: 45 minute after Qualifying."
        ],
        "Races": [
            ("8/5", "Mid Ohio Raceway"),
            ("8/12", "Rudskogen"),
            ("8/19", "Laguna Seca"),
            ("8/26", "Imola"),
        ],
    },
    # To add another series, copy this shape and fill in real data:
    # {
    #     "name": "GT3 Sprint Series",
    #     "day": "Saturdays",
    #     "details": "Practice 6:00pm EST. Qualifying: 10 minutes. Race: 30 minutes.",
    #     "races": [
    #         ("6/28", "Spa"),
    #         ("7/5", "Monza"),
    #     ],
    # },
]


def build_reminder_message():
    sections = [INTRO_TEXT]
    for series in SERIES:
        header = f"\n**{series['Name']}** ({series['Day']})"
        details = "\n".join(series["Details"])
        races = "\n".join(f"{date}: {track}" for date, track in series["Races"])
        block = f"{header}\n{details}\n\n{races}"
        sections.append(block)
    return "\n\n".join(sections)


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    check_time.start()


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content == "!ping":
        await message.channel.send("Pong! (I will come down there and make it look like an accident Larry)")


@tasks.loop(minutes=1)
async def check_time():
    now = datetime.now(ZoneInfo("America/New_York"))
    if now.weekday() == 6 and now.hour == 20 and now.minute == 00:
        message = build_reminder_message()
        for guild in client.guilds:
            channel = discord.utils.get(guild.text_channels, name=CHANNEL_NAME)
            if channel:
                await channel.send(message)


client.run(TOKEN)