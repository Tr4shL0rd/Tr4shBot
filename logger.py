# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
This module contains the Logger class, which is used to log various events that occur in a Discord chat.

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
    def __init__(self) -> None:
        self.chat_log_file = open("logs/chatlog.log", "a+", encoding=("utf-8"))
        self.sys_log_file  = open("logs/syslog.log", "a+", encoding=("utf-8"))
        self.current_time  = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    def log_boilerplate(self,message,event:str):
        return f"[{event.upper()}][{message.created_at}] [{message.author.name}#{message.author.discriminator} -> {message.channel.name}]:"

    def close_chat_file(self):
        self.chat_log_file.close()

    def close_sys_file(self):
        self.sys_log_file.close()

    def close_files(self):
        self.close_chat_file()
        self.close_sys_file()

    def chat_log(self, message) -> str:
        msg = f"{self.log_boilerplate(message, 'CHAT')} {message.content}"
        self.chat_log_file.write(f"{msg}\n") 
        self.chat_log_file.flush()
        return msg

    def chat_edit_log(self,message_before,message_after) -> str:
        msg = f"[EDIT][{message_before.created_at}] [{message_before.author.name}#{message_before.author.discriminator} -> {message_before.channel.name}]: {message_before.content} => {message_after.content}"
        self.chat_log_file.write(f"{msg}\n")        
        self.chat_log_file.flush()
        return msg

    def chat_delete_log(self,message) -> str:
        msg = f"{self.log_boilerplate(message, 'delete')} {message.content}"
        self.chat_log_file.write(f"{msg}\n")
        self.chat_log_file.flush()
        return msg

    def sys_log(self,message):
        msg = f"[SYS][{self.current_time}]: {message}"
        self.sys_log_file.write(f"{msg}\n")
        self.sys_log_file.flush()
        return msg
    
    
