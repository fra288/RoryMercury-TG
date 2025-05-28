from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
import random

class Dado:
    def __init__(self):
        self.dado_command = CommandHandler("dado", self.dado)

    async def dado(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        numero = random.randint(1, 6)
        await update.message.reply_text(f"🎲 Has lanzado el dado y salió: {numero}", reply_to_message_id=update.message.message_id)
        print("CMD | Comando /dado ejecutado.")

def setup():
    return Dado()