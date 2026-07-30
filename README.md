# Mëgatrøn

Bot de Discord feito em Python para estudo de lógica de programação e redes.

## O que ele faz

- Responde quando é chamado por um dos seus apelidos no chat.
- Guarda tarefas em um banco de dados SQLite (persistem mesmo depois de reiniciar).
- Mantém um diário (log) de quem usou cada comando e quando.
- Conta XP silenciosamente para cada pessoa a cada mensagem e calcula o nível.
- Busca uma imagem aleatória de gato em uma API externa.

## Comandos

| Comando | O que faz |
| --- | --- |
| `$risos` | O bot dá uma risada. |
| `$tarefa <texto>` | Salva uma tarefa no banco de dados. |
| `$tarefas` | Lista todas as tarefas salvas. |
| `$xp` | Mostra seus pontos de XP e seu nível atual. |
| `$gato` | Envia uma foto aleatória de um gato. |

## Como rodar

1. Instale as dependências:

   ```
   pip install -r requirements.txt
   ```

2. Crie um arquivo `.env` na pasta do projeto com o token do bot:

   ```
   DISCORD_TOKEN=seu_token_aqui
   ```

3. Rode o bot:

   ```
   python bot.py
   ```

## Tecnologias

- [discord.py](https://discordpy.readthedocs.io/) — conexão com o Discord
- SQLite — banco de dados
- aiohttp — requisições à API externa
- python-dotenv — carregar o token do arquivo `.env`
