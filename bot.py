import discord                        
import os                             
import sqlite3                        
from dotenv import load_dotenv        
from discord.ext import commands      
load_dotenv()                         

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")   

autorizacoes = discord.Intents.default()     
autorizacoes.message_content = True         
autorizacoes.members = True                  

bot = commands.Bot(command_prefix="$", intents=autorizacoes)
apelidos = ["mega", "trontron","meguinha","megatron", "tron","palhaçao"] 

                   
banco = sqlite3.connect("tarefas.db") 
cursor = banco.cursor()  # cria o cursor (a "caneta") que executa os comandos SQL dentro do banco
cursor.execute("CREATE TABLE IF NOT EXISTS tarefas (descricao TEXT)")

@bot.event                            
async def on_message(msg):            

    if msg.author == bot.user:        # se quem mandou a mensagem foi o próprio bot...
        return                        # ...para aqui (pra ele não responder a si mesmo)

    texto = msg.content.lower()       
    palavras = texto.split()          
    for item in palavras:             
        if item in apelidos:          
            await msg.channel.send("MEGATRON? ONDE? QUEM? *procura por si mesmo* AH, SOU EU! HAHAHAHA!")  # responde no
            break                     

    await bot.process_commands(msg)   
@bot.command()                        
async def risos(ctx):                 
    await ctx.send("A desenvolvedora nº 197-0i00 me pediu pra rir uma última vez antes de... enfim. HAHAHAHAHA. Em memória dela.")  

@bot.command()                        
async def tarefa(ctx,*,descricao):    # $tarefa; o *, faz "descricao" pegar a frase TODA (com espaços)
    cursor.execute("INSERT INTO tarefas (descricao) VALUES (?)", (descricao,))   # insere a tarefa na tabela
    banco.commit()                    # confirma e grava no disco de verdade
    await ctx.send(descricao)

@bot.command()                        
async def tarefas(ctx):  
    cursor .execute("SELECT descricao FROM tarefas")
    resultado = cursor.fetchall()   
    resposta = ""
    for linha in resultado:     
            resposta = resposta + "- " + linha[0] + "\n" 
    await ctx.send(resposta)     

bot.run(DISCORD_TOKEN)                
