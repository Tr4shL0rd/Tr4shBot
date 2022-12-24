# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
This module contains the Logger class, which is used to
log various events that occur in a Discord chat.

Attributes:
---
    chat_log_file: A file object for the chat log file.
    sys_log_file: A file object for the system log file.
    current_time: A string representing the current time.

Methods:
---
    init: Initializes the Logger object and opens the log files.
    close_chat_file: Closes the chat log file.
    close_sys_file: Closes the system log file.
    close_files: Closes both log files.
    chat_log: Logs a message in the chat log file.
    chat_edit_log: Logs an edited message in the chat log file.
    chat_delete_log: Logs a deleted message in the chat log file.
    sys_log: Logs a message in the system log file.
"""
from datetime import datetime


class Logger:
    """
    The Logger class is used to log events and messages to log files.
    It provides methods to log chat messages, deleted chat messages, edited chat messages,
    and system messages. It also provides methods to close the log files
    when the program is finished running.
    Attributes:
    ---
        - chat_log_file (file): The file object for the chat log file.
        - sys_log_file (file): The file object for the system log file.
        - current_time (str): The current time, formatted as a string.

    Methods:
    ---
        - log_boilerplate(self, message, event: str) -> str: Generates the standard prefix for a
                log message, including the event type, creation time, and information
                about the message's author and channel.
        - close_chat_file(self) -> None: Closes the chat log file.
        - close_sys_file(self) -> None: Closes the system log file.
        - close_files(self) -> None: Closes the chat log and system log files.
        - chat_log(self, message: discord.Message) -> str: Logs chat messages to a file
                and returns the logged message.
        - chat_edit_log(self, message_before: discord.Message,
                message_after: discord.Message) -> str:
                Logs edited chat messages to a file and returns the logged message.
        - chat_delete_log(self, message: discord.Message) -> str: Logs a deleted
                message to the chat log file and returns the logged message.
        - sys_log(self, message: str) -> str: Logs system messages to a file and
                returns the logged message.
    """

    def __init__(self) -> None:
        self.chat_log_file = open(
            "logs/chatlog.log", "a+", encoding=("utf-8")
        )  # pylint:disable=consider-using-with
        self.sys_log_file = open(
            "logs/syslog.log", "a+", encoding=("utf-8")
        )  # pylint:disable=consider-using-with
        self.current_time = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    def log_boilerplate(self, message, event: str):
        """
        Generates the standard prefix for a log message, including the event type,
        creation time, and information about the message's author and channel.

        Args:
        ---
            - message (discord.Message): The message being logged.
            - event (str): The type of event being logged, such as "CHAT" or "DELETE".

        Returns:
        ---
            - str: The prefix for the log message.
        """
        return f"[{event.upper()}][{message.created_at}] [{message.author.name}#{message.author.discriminator} -> {message.channel.name}]:"  # pylint:disable=line-too-long

    def close_chat_file(self):
        """
        Closes the chat log file.

        This method closes the chat log file,
        ensuring that all data is saved and the file is properly closed.
        """
        self.chat_log_file.close()

    def close_sys_file(self):
        """
        Close the system log file.

        This method closes the system log file, which is used to
        log system events such as bot connection and disconnection.
        """
        self.sys_log_file.close()

    def close_files(self):
        """
        Close the chat log and system log files.

        This method closes the file objects for the chat log and system log, and should
        be called before the program exits to ensure that all data is written to the log files.
        """
        self.close_chat_file()
        self.close_sys_file()

    def chat_log(self, message) -> str:
        """
        Logs chat messages to a file.

        Args:
        ---
            - message (discord.Message): The message to be logged.

        Returns:
        ---
            - str: The formatted message to be logged.
        """
        msg = f"{self.log_boilerplate(message, 'CHAT')} {message.content}"
        self.chat_log_file.write(f"{msg}\n")
        self.chat_log_file.flush()
        return msg

    def chat_edit_log(self, message_before, message_after) -> str:
        """
        Logs chat messages to a file and returns the logged message.

        Args:
        ---
            - message (discord.Message): The message object to be logged.

        Returns:
        ---
            - str: The logged message.
        """
        msg = f"[EDIT][{message_before.created_at}] [{message_before.author.name}#{message_before.author.discriminator} -> {message_before.channel.name}]: {message_before.content} => {message_after.content}"  # pylint:disable=line-too-long
        self.chat_log_file.write(f"{msg}\n")
        self.chat_log_file.flush()
        return msg

    def chat_reaction_log(self, reaction,user):
        pass#msg = f"{self.log_boilerplate()}"

    def chat_delete_log(self, message) -> str:
        """
        Logs a deleted message to the chat log file.

        Args:
        ---
            - message (discord.Message): The deleted message.

        Returns:
        ---
            - str: The log message.
        """
        msg = f"{self.log_boilerplate(message, 'delete')} {message.content}"
        self.chat_log_file.write(f"{msg}\n")
        self.chat_log_file.flush()
        return msg

    def sys_log(self, message):
        """
        Logs system messages to a file and returns the logged message.

        Args:
        ---
            - message (str): The message to log and return.

        Returns:
        ---
            - str: The logged message.
        """
        msg = f"[SYS][{self.current_time}]: {message}"
        self.sys_log_file.write(f"{msg}\n")
        self.sys_log_file.flush()
        return msg
