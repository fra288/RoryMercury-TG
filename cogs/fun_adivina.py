from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
import random

class Adivina:
    def __init__(self):
        self.adivina_command = CommandHandler("adivina", self.adivina)

    async def adivina(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        numero = random.randint(1, 10)
        await update.message.reply_text("Estoy pensando en un número del 1 al 10, intenta adivinarlo con /intenta <numero>", reply_to_message_id=update.message.message_id)
        print("CMD | Comando /adivina ejecutado.")
        context.chat_data["numero_secreto"] = numero

def setup():
    return Adivina()