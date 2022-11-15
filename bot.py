import discord
import os
import random
import datetime
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
  
token = os.getenv('TOKEN')

intents = discord.Intents.default()
intents.message_content = True


time = datetime.datetime.now()
bot = commands.Bot(command_prefix='>', intents=intents)
random.seed(None, 2)


class MyClient(discord.Client):
    async def on_ready(self):
        print(f"Conectado como {self.user} (ID: {self.user.id})")
    
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!gueime'):
            await message.reply("vose ser muito gueime", mention_author=True)
            print(f"{time}: Gueime solicitado!")

        if message.content.startswith('!datetime'):
            await message.reply(f'a data e hora são: {time}!')
            print(f"{time}: Data e hora solicitados!")

        if message.content.startswith('!roll'):
            await message.reply(f'sua rola é {random.randrange(1, 100)}!')
        
        if message.content.startswith('!pergunta'):
            tmpnum = random.randrange(0, 2)
            if tmpnum == 0:
                resposta = "não"
            if tmpnum == 1:
                resposta = "sim"
            await message.reply(f'Eu acho que {resposta}')
    

client = MyClient(intents=intents)








client.run(token)