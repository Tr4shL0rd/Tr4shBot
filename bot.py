# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
This module contains a Discord bot that responds to commands with various functions, such as:\n
            - returning a greeting.
            - a dog or cat fact.
            - weather information.
The bot is implemented using the Discord API,
and can be run on a Discord server by providing a valid token and the name of the target guild.

The module contains a Commands class with methods for accessing lists of different types of
commands, and several event handlers for responding to different events that can occur
within a Discord server, such as a user sending a message or the bot connecting to the server.
The module also utilizes the Logger, DogFact, CatFact, and helper modules for various functions.

Attributes:
---
    logger: An instance of the Logger class for logging system messages.
    dog_fact: An instance of the DogFact class for retrieving random dog facts from an online API.
    cat_fact: An instance of the CatFact class for retrieving random cat facts from an online API.
    TOKEN: A string containing the Discord API token for the bot.
    GUILD: A string containing the name of the target Discord guild for the bot.
    client: An instance of the discord.Client class for connecting to and
    interacting with a Discord server.

Methods:
---
    - on_connect(): A function that runs when the bot connects to the Discord server.
        Prints a message to the console indicating that the bot is connected.
    - on_ready(): A function that runs when the bot is ready to interact with the Discord server.
        Prints a message to the console indicating the bot's readiness and
        lists the members of the guild.
    - on_message(message): An event handler function that runs when a message is sent on the
        Discord server. Prints a message to the console and responds to the message with
        various functions depending on the content of the message.
"""
import os
from typing import List
import discord
from discord import Intents
from dotenv import load_dotenv
from logger import Logger
from animal_fact import DogFact
from animal_fact import CatFact
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

    The class has methods for accessing lists of greetings and dog facts,
    as well as a method for accessing all commands.
    """

    def __init__(self) -> None:
        """
        Initializes the Commands class.
        """

    def greets(self) -> List[str]:
        """
        Returns a list of greetings.

        Returns:
        ---
            list: A list of greetings.
        """
        return helper.fix_command(
            ["hello", "hey", "hi", "hiya", "greetings", "yo", "sup", "wassup", "howdy"]
        )

    def dog_facts(self) -> List[str]:
        """
        Returns a list of commands for requesting dog facts.

        Returns:
        ---
            list: A list of commands for requesting dog facts.
        """
        return helper.fix_command(["dogfact", "dog-fact"])

    def cat_facts(self) -> List[str]:
        """
        Returns a list of commands for requesting cat facts.

        Returns:
        ---
            list: A list of commands for requesting cat facts.
        """
        return helper.fix_command(["catfact", "cat-fact"])

    def weather_commands(self) -> List[str]:
        """
        Returns a list of commands for requesting weather information.

        Returns:
        ---
            List[str]: A list of commands for requesting weather information.
        """
        return helper.fix_command(["weather", "w"])

    def help(self) -> List[str]:
        """
        Returns a list of commands for accessing help information.

        Returns:
        ---
            List[str]: A list of commands for accessing help information.
        """
        return helper.fix_command(["help", "h", "?"])

    def all_commands(self) -> List[str]:
        """
        Returns a tuple containing lists of all commands.

        Returns:
        ---
            tuple: A tuple containing lists of all commands, including greetings and commands for
            requesting dog facts.
        """
        return (self.greets(), self.dog_facts(), self.weather_commands(), self.help())


@client.event
async def on_connect():
    """
    Event for when the bot connects to Discord.

    Prints a system log message indicating that the bot has connected.
    """
    print(logger.sys_log("Bot Is Connected!"))


@client.event
async def on_ready():
    """
    Event for when the bot is ready to receive messages.
    Prints the bot's status and list of guild members.
    """
    guild = None
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(f"{client.user} is ready on following servers:\n{guild.name}(ID: {guild.id})")

    g_members = "\n - ".join([member.name for member in guild.members])
    print(f"Guild Member:\n - {g_members}")

###### MESSAGE HANDLING ######
@client.event
async def on_message(message):
    """
    Handles messages sent in the Discord server.

    Args:
    ---
        message (discord.Message): The message sent in the Discord server.
    """
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

    elif message.content.lower().split()[0] in commands.weather_commands():
        city_name = message.content.lower().split(" ")
        weather_class = weather_file.Weather(
            city="esbjerg" if len(city_name) < 2 else city_name[-1]
        )
        await message.channel.send(weather_class.weather())

    elif message.content.lower() in commands.help():
        help_text = "**Available commands:**\n"
        help_text += (
            f"**{', '.join(commands.greets()[0:3])}**: Send a greeting to the user\n"
        )
        help_text += f"**{', '.join(commands.dog_facts())}**: Get a random dog fact\n"
        help_text += f"**{', '.join(commands.cat_facts())}**: Get a random cat fact\n"
        help_text += f"**{', '.join(commands.weather_commands())} [city]**: Get weather information for a city\n"  # pylint: disable=line-too-long

        await message.channel.send(help_text)

@client.event
async def on_message_edit(before, after):
    """
    Logs any edits made to a message in a Discord server.

    This event handler is triggered when a message is edited in a Discord server.
    It prints the original and edited versions of the message to the console.

    Args:
    ---
        before (discord.Message): The original version of the message.
        after (discord.Message): The edited version of the message.

    Returns:
    ---
        None
    """
    print(logger.chat_edit_log(before, after))


@client.event
async def on_message_delete(before):
    """
    Logs the deletion of a message in a Discord server.

    Args:
    ---
        before: The message that was deleted.

    Returns:
    ---
        None
    """
    print(logger.chat_delete_log(before))

###### REACTION HANDLING ######
@client.event
async def on_raw_reaction_add(payload):
    reaction = payload.emoji.name
    user = f"{payload.member.name}#{payload.member.discriminator}"
    print(f"{user} reacted with {reaction} to a message")

@client.event
async def on_raw_reaction_remove(payload):
    #print(payload)
    reaction = payload.emoji.name
    print(f"{reaction} removed from a message")

@client.event
async def on_raw_reaction_clear(payload):
    print(payload)

###### MEMBER HANDLING ######
@client.event
async def on_member_join(member):
    print(member)

@client.event
async def on_member_remove(member):
    print(member)

@client.event
async def on_member_update(member_befor, member_after):
    print(member_befor, member_after)

@client.event
async def on_member_ban(guild,user):
    print(guild,user)

@client.event
async def on_member_unban(guild,user):
    print(guild,user)

###### THREAD HANDLING ######
@client.event
async def on_thread_create(thread):
    print(thread)

@client.event
async def on_thread_join(thread):
    print(thread)

@client.event
async def on_thread_update(thread_before,thread_after):
    print(thread_before,thread_after)

@client.event
async def on_thread_remove(thread):
    print(thread)

@client.event
async def on_thread_delete(thread):
    print(thread)




if __name__ == "__main__":
    try:
        client.run(TOKEN)
    except RuntimeError:
        print("STOPPING BOT")
        logger.close_files()
