from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
import random

class PPT:
    def __init__(self):
        self.ppt_command = CommandHandler("ppt", self.ppt)

    async def ppt(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        opciones = ["piedra", "papel", "tijera"]
        eleccion_bot = random.choice(opciones)
        if not context.args:
            await update.message.reply_text("Usa: /ppt piedra|papel|tijera", reply_to_message_id=update.message.message_id)
            return
        eleccion_usuario = context.args[0].lower()
        if eleccion_usuario not in opciones:
            await update.message.reply_text("Opción inválida. Usa: /ppt piedra|papel|tijera", reply_to_message_id=update.message.message_id)
            return

        resultado = "Empate"
        if eleccion_usuario != eleccion_bot:
            if (eleccion_usuario == "piedra" and eleccion_bot == "tijera") or \
               (eleccion_usuario == "papel" and eleccion_bot == "piedra") or \
               (eleccion_usuario == "tijera" and eleccion_bot == "papel"):
                resultado = "¡Ganaste!"
            else:
                resultado = "¡Perdiste!"

        await update.message.reply_text(f"Elegiste {eleccion_usuario}, yo elegí {eleccion_bot}. {resultado}", reply_to_message_id=update.message.message_id)
        print("CMD | Comando /ppt ejecutado.")

def setup():
    return PPT()