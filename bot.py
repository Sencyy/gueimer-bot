import discord
import os
import random
from dotenv import load_dotenv
from discord.ext import commands


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Conectado como {self.user} (ID: {self.user.id})")
    
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!gueime'):
            await message.reply("vose ser muito gueime", mention_author=True)

load_dotenv()
  
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True


client = MyClient(intents=intents)

bot = commands.Bot(command_prefix='>', intents=intents)



client.run(token)