import discord
import os
import random
import datetime
from dotenv import load_dotenv

import cmd_pergunta
import cmd_roll
import cmd_calc
import cmd_escolha


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
async def gueime(ctx, pessoa: discord.Option(str)):
    await ctx.respond(f"{pessoa} ser um gueime")
    print(f"{datetime.datetime.now()}: Gueime solicitado!")

@bot.command(description="Mostra a data e hora no momento em que o comando foi acionado")
async def time(ctx):
    await ctx.respond(f"A data e hora é: {datetime.datetime.now()}")
    print(f"{datetime.datetime.now()}: Data solicitada!")

@bot.command(description="Faz uma pergunta ao bot.")
async def pergunta(ctx, pergunta: discord.Option(str)):
    await ctx.respond(f"{ctx.author.name} perguntou: {pergunta}")
    await ctx.send(f"Eu acho que {cmd_pergunta.pergunta(pergunta)}")
    print(f"{datetime.datetime.now()}: Pergunta solicitada!")

@bot.command(description="Rola o dado em um número de 0 à 100.")
async def roll(ctx):
    await ctx.respond(f"{ctx.author.name} rolou {cmd_roll.roll()}")
    print(f"{datetime.datetime.now()}: Rola solicitada!")

    
@bot.command(description="Faz o L")
async def fazol(ctx):
    with open("img/fazol.png", "rb") as fh:
        f = discord.File(fh, filename="img/fazol.png")
    await ctx.respond(file=f)
    print(f"{datetime.datetime.now()}: Faz o L!")

@bot.command(description="Faz calculos matemáticos.")
async def calc(ctx, num1: discord.Option(int), op: discord.Option(str), num2: discord.Option(int)):
    await ctx.respond(f"{num1} {op} {num2} = {cmd_calc.calc(num1, op, num2)}")
    print(f"{datetime.datetime.now()}: Calculo solicitado!")

@bot.command(description="Escolhe uma de duas opções")
async def escolha(ctx, opc1: discord.Option(str), opc2: discord.Option(str)):
    await ctx.respond(f"Entre {opc1} e {opc2}")
    await ctx.send(f"eu escolho {cmd_escolha.escolha(opc1, opc2)}")
    print(f"{datetime.datetime.now()}: Escolha solicitada!")



bot.run(token)