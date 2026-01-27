import os
import random

try:
  from telegram import Update
  from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
  from configReplay import menu_message,help_message
  from pyfiglet import figlet_format
  from dotenv import load_dotenv
except ModuleNotFoundError:
  print("[*]dowload depentencies please wait :3")
  os.system("pip install python-telegram-bot")
  os.system("pip install pyfiglet")
  os.system("pip install python-dotenv")

print(figlet_format("MACRO BOT"))
print("by nullbyte")
print("[*]bot iniciado com sucesso")

load_dotenv()

TOKEN = os.getenv("TOKEN")

COMMANDS = {}

def command(name):
  def wrapper(func):
     COMMANDS[name] = func
     return func
  return wrapper

@command("start")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
   username = update.effective_user.username or "null"
   await update.message.reply_text(f"ola {username} use o /menu para ver minhas funçãoes")

@command("menu")
async def menu(update:Update,context:ContextTypes.DEFAULT_TYPE):
    with open("media/icon.jpg","rb") as ft:
     await update.message.reply_photo(
        photo=ft,
        caption=menu_message
     )

@command("coin")
async def coin(update: Update, context: ContextTypes.DEFAULT_TYPE):
   res = random.choice(["cara","coroa"])
   await update.message.reply_text(res)

@command("help")
async def help(update:Update,context: ContextTypes.DEFAULT_TYPE):
 await update.message.reply_text(help_message)

app = ApplicationBuilder().token(TOKEN).build()

for cmd, func in COMMANDS.items():
    app.add_handler(CommandHandler(cmd, func))


app.run_polling()
