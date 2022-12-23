# -*- coding: utf-8 -*-
import os
import discord
from discord import Intents
from logger import Logger
from dotenv import load_dotenv
from rich import print as rprint
from animal_fact import DogFact
from animal_fact import CatFact
#from weather_file import Weather
import weather_file
import helper
load_dotenv()

logger = Logger()
dog_fact = DogFact()
cat_fact = CatFact()
TOKEN = os.getenv("TOKEN")
GUILD = os.getenv("GUILD")
client = discord.Client(intents=Intents.all())

class Commands:
    """
    A class containing methods for accessing lists of commands.

    The class has methods for accessing lists of greetings and dog facts, as well as a method for accessing all commands.
    """
    def __init__(self) -> None:
        """
        Initializes the Commands class.
        """
        pass
    def greets(self):
        """
        Returns a list of greetings.

        Returns:
            list: A list of greetings.
        """
        return helper.fix_command(["hello", "hey", "hi", "hiya", "greetings"])
    def dog_facts(self):
        """
        Returns a list of commands for requesting dog facts.

        Returns:
            list: A list of commands for requesting dog facts.
        """
        return helper.fix_command(["dogfact", "dog-fact"]) 
    def cat_facts(self):
        """
        Returns a list of commands for requesting cat facts.
        
        Returns:
            list: A list of commands for requesting cat facts.
        """
        return helper.fix_command(["catfact", "cat-fact"])
    def weather_commands(self):
        #return Weather.weather("kolding")
            return helper.fix_command(["weather"])
    def all_commands(self):
        """
        Returns a tuple containing lists of all commands.

        Returns:
            tuple: A tuple containing lists of all commands, including greetings and commands for requesting dog facts.
        """
        return (self.greets(),self.dog_facts())

@client.event
async def on_connect():
    print(logger.sys_log("Bot Is Connected!"))

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(
            f"{client.user} is ready on following servers:\n"
            f"{guild.name}(ID: {guild.id})"
        )

    bot_accounts = [member for member in guild.members]
    for account in bot_accounts:
        if not account.bot:
            bot_accounts.remove(account)
    gMembers = "\n - ".join([member.name for member in guild.members])
    print(f"Guild Member:\n - {gMembers}")

@client.event
async def on_message(message):
    commands = Commands()
    print(logger.chat_log(message=message))
    if message.content.lower() == "ping":
        await message.channel.send("pong")
    elif message.content.lower() in commands.greets():
        await message.channel.send(helper.random_greeting(message.author.name))
    elif message.content.lower() in commands.dog_facts():
        await message.channel.send(dog_fact.random_fact())
    elif message.content.lower() in commands.cat_facts():
        await message.channel.send(cat_fact.random_fact())
    #elif message.content.lower() in commands.weather_commands():
    elif "!weather" in message.content.lower():
        city_name = message.content.split(" ")
        weather_class = weather_file.Weather(city="esbjerg" if len(city_name) <2 else city_name[-1])
        await message.channel.send(weather_class.weather())

@client.event
async def on_message_edit(before,after):
    print(logger.chat_edit_log(before,after))

@client.event
async def on_message_delete(before):
    print(logger.chat_delete_log(before))

if __name__ == "__main__":
    try:
        client.run(TOKEN)
    except RuntimeError:
        print(logger.sys_log("STOPPING BOT"))
        logger.close_files()
