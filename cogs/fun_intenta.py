from telegram.ext import CommandHandler, ContextTypes
from telegram import Update

class Intenta:
    def __init__(self):
        self.intenta_command = CommandHandler("intenta", self.intenta)

    async def intenta(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if "numero_secreto" not in context.chat_data:
            await update.message.reply_text("Primero usa /adivina para iniciar el juego.", reply_to_message_id=update.message.message_id)
            print("CMD | Comando / ejecutado.")
            return
        if not context.args or not context.args[0].isdigit():
            await update.message.reply_text("Usa: /intenta <numero>", reply_to_message_id=update.message.message_id)
            return

        intento = int(context.args[0])
        secreto = context.chat_data["numero_secreto"]

        if intento == secreto:
            await update.message.reply_text("🎉 ¡Correcto! Adivinaste el número.", reply_to_message_id=update.message.message_id)
            del context.chat_data["numero_secreto"]
        else:
            await update.message.reply_text("❌ No es el número, intenta de nuevo.", reply_to_message_id=update.message.message_id)

def setup():
    return Intenta()