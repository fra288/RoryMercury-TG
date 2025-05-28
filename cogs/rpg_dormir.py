from telegram.ext import CommandHandler, ContextTypes
from telegram import Update

class Dormir:
    def __init__(self):
        self.dormir_command = CommandHandler("dormir", self.dormir)

    async def dormir(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("😴 Has descansado en la posada y recuperaste toda tu energía.", reply_to_message_id=update.message.message_id)
        print("CMD | Comando /dormir ejecutado.")

def setup():
    return Dormir()