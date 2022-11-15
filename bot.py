import discord
import os
import random
import datetime
from dotenv import load_dotenv

import cmd_pergunta
import cmd_roll


load_dotenv()

token = os.getenv("TOKEN")
bot = discord.Bot()

print("GueimerBot 2.0 alpha")
print("Conectando-se aos servidores do Discord...")

@bot.event
async def on_ready():
    print(f"Conectado como {bot.user}!")

@bot.command(description="Envia a latência do bot.")
async def ping(ctx):
    await ctx.respond(f"Pong! A latência do bot é {bot.latency}")

@bot.command(description="Gueime")
async def gueime(ctx):
    await ctx.respond("vose ser um gueime")

@bot.command(description="Mostra a data e hora no momento em que o comando foi acionado")
async def time(ctx):
    await ctx.respond(f"A data e hora é: {datetime.datetime.now()}")

@bot.command(description="Faz uma pergunta ao bot.")
async def pergunta(ctx, pergunta: discord.Option(str)):
    await ctx.respond(f"{ctx.author.name} perguntou: {pergunta}")
    await ctx.respond(f"Eu acho que {cmd_pergunta.pergunta()}")

@bot.command(description="Rola o dado em um número de 0 à 100.")
async def roll(ctx):
    await ctx.respond(f"{ctx.author.name} rolou {cmd_roll.roll()}")



bot.run(token)