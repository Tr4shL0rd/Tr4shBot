# -*- coding: utf-8 -*-
from datetime import datetime

class Logger:
    def __init__(self) -> None:
        self.chat_log_file = open("logs/chatlog.log", "a", encoding=("utf-8"))
        self.sys_log_file  = open("logs/syslog.log", "a", encoding=("utf-8"))
        self.current_time  = datetime.now().strftime("%Y/%m/%d %H:%M:%S")

    def close_chat_file(self):
        self.chat_log_file.close()

    def close_sys_file(self):
        self.sys_log_file.close()
    
    def close_files(self):
        self.close_chat_file()
        self.close_sys_file()
        
    def chat_log(self, message) -> str:
        msg = f"[CHAT][{message.created_at}] [{message.author.name}#{message.author.discriminator} -> {message.channel.name}]: {message.content}"
        self.chat_log_file.write(f"{msg}\n") 
        return msg

    def chat_edit_log(self,message_before,message_after) -> str:
        msg = f"[EDIT][{message_before.created_at}] [{message_before.author.name}#{message_before.author.discriminator} -> {message_before.channel.name}] {message_before.content} => {message_after.content}"
        self.chat_log_file.write(f"{msg}\n")        
        return msg
    
    def sys_log(self,message):
        msg = f"[SYS][{self.current_time}]: {message}"
        self.sys_log_file.write(f"{msg}\n")
        return msg
    
    
