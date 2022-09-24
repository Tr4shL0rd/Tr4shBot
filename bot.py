# -*- coding: utf-8 -*-
import os
import discord
from discord import Intents
from logger import Logger
from dotenv import load_dotenv
load_dotenv()

logger = Logger()
    
TOKEN = os.getenv("TOKEN")
GUILD = os.getenv("GUILD")
client = discord.Client(intents=Intents.all())


@client.event
async def on_connect():
    print("Bot Is Connected!")

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
            f"{client.user} is ready on following servers:\n"
            f"{guild.name}(ID: {guild.id})"
        )
    gMembers = "\n - ".join([member.name for member in guild.members])
    print(f"Guild Member:\n - {gMembers}")
    
@client.event
async def on_message(message):
    print(logger.chat_log(message=message))
    logger.close_chat_file()
@client.event
async def on_message_edit(before,after):
    print(logger.chat_edit_log(before,after))
    logger.close_chat_file()

@client.event
async def on_error():
    logger.close_chat_file()
    print("STOPPING BOT...")
try:
    client.run(TOKEN)
except RuntimeError:
    print(logger.sys_log("STOPPING BOT"))
    logger.close_files()
