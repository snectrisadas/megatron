import discord
import os
import sqlite3
import logging
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

autorizacoes = discord.Intents.default()
autorizacoes.message_content = True
autorizacoes.members = True

bot = commands.Bot(command_prefix="$", intents=autorizacoes)
apelidos = ["mega", "trontron", "meguinha", "megatron", "tron", "palhaçao"]

logging.basicConfig(filename="diario.log", level=logging.INFO)

banco = sqlite3.connect("tarefas.db")
cursor = banco.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS tarefas (descricao TEXT)")
cursor.execute("CREATE TABLE IF NOT EXISTS usuarios (id_usuario INTEGER PRIMARY KEY, xp INTEGER)")


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

    cursor.execute("INSERT INTO usuarios (id_usuario, xp) VALUES (?, 1) ON CONFLICT(id_usuario) DO UPDATE SET xp = xp + 1", (msg.author.id,))
    banco.commit()

    await bot.process_commands(msg)


@bot.command()
async def risos(ctx):
    logging.info(f"{ctx.author} usou o comando risos")
    await ctx.send("A desenvolvedora nº 197-0i00 me pediu pra rir uma última vez antes de... enfim. HAHAHAHAHA. Em memória dela.")


@bot.command()
async def tarefa(ctx, *, descricao):
    cursor.execute("INSERT INTO tarefas (descricao) VALUES (?)", (descricao,))
    banco.commit()
    logging.info(f"{ctx.author} usou o comando tarefa")
    await ctx.send(descricao)


@bot.command()
async def tarefas(ctx):
    cursor.execute("SELECT descricao FROM tarefas")
    resultado = cursor.fetchall()
    resposta = ""
    for linha in resultado:
        resposta = resposta + "- " + linha[0] + "\n"
    logging.info(f"{ctx.author} usou o comando tarefas")
    await ctx.send(resposta)


bot.run(DISCORD_TOKEN)
