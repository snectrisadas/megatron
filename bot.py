import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

autorizacoes = discord.Intents.default()
autorizacoes.message_content = True
autorizacoes.members = True

bot = commands.Bot(command_prefix="$", intents=autorizacoes)
apelidos = ["mega", "trontron","meguinha","megatron", "tron","palhaçao"]

lista_tarefas = [] 

@bot.event
async def on_message(msg):
      
    if msg.author == bot.user:
        return

    texto = msg.content.lower()
    palavras = texto.split()
    for item in palavras:
        if item in apelidos:
            await msg.channel.send("MEGATRON? ONDE? QUEM? *procura por si mesmo* AH, SOU EU! HAHAHAHA!")
            break
        
    await bot.process_commands(msg)   

@bot.command()
async def risos(ctx):
    await ctx.send("A desenvolvedora nº 197-0i00 me pediu pra rir uma última vez antes de... enfim. HAHAHAHAHA. Em memória dela.")

@bot.command()
async def tarefa(ctx,*,descricao):
    lista_tarefas.append(descricao)
    await ctx.send(descricao)

@bot.command()       
async def tarefas(ctx):
    await ctx.send(lista_tarefas)

           

     
bot.run(DISCORD_TOKEN)
