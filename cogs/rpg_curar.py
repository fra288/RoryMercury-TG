import random
from telegram.ext import CommandHandler, ContextTypes
from telegram import Update

class Curar:
    def __init__(self):
        self.curar_command = CommandHandler("curar", self.curar)

    async def curar(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        vida = random.randint(10, 30)
        await update.message.reply_text(f"💊 Usaste una poción y recuperaste {vida} puntos de vida.", reply_to_message_id=update.message.message_id)
        print("CMD | Comando /curar ejecutado.")

def setup():
    return Curar()