import discord, os, telegram
from discord.ext import commands

class PyChat():
    
    def __init__(self, discord_token=None, telegram_token=None, messenger_token=None, messenger_verify=None, wechat_token=None):
        self.discord_token = discord_token
        self.telegram = telegram
        self.messenger_token = messenger_token
        self.messenger_verify = messenger_verify
        self.WeChat_token = wechat_token
        return True

    class DiscordClient(self, Token=self.discord_token):
        
        def __init__(self):
            self.client = discord.Client()
        
    class TelegramClient(self, TOKEN = self.telegram_token):
        pass
        
    class MessengerClient(self, TOKEN=self.messenger_token, VERIFY = self.messenger_verify):
        pass
        
    class WeChatClient(self, TOKEN = self.WeChat_token):
        pass

if __name__ == '__main__':
    Bot = PyChat().Discord
    print(Bot)
