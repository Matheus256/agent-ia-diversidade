import telebot
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=".env")                       # Carrega o arquivo com as variáveis de ambiente - (TOKEN DO BOT)
TOKEN = os.getenv("BOT_TOKEN")

if not TOKEN:
    raise ValueError("TOKEN environment variable not found")

bot = telebot.TeleBot(TOKEN)

# Import dos handlers após o bot ser criado
import handlers