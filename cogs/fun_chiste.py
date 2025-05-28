from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
import random

class Chiste:
    def __init__(self):
        self.chiste_command = CommandHandler("chiste", self.chiste)

    async def chiste(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chistes = [
            "¿Por qué los pájaros no usan Facebook? ¡Porque ya tienen Twitter!",
            "¿Cuál es el café más peligroso del mundo? El ex-preso.",
            "¿Qué hace una abeja en el gimnasio? ¡Zum-ba!"
        ]
        await update.message.reply_text(random.choice(chistes), reply_to_message_id=update.message.message_id)
        print("CMD | Comando /chiste ejecutado.")

def setup():
    return Chiste()