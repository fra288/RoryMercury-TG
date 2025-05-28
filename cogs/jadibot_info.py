from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
import json
import os

SUBBOTS_FILE = "jadibots/subbots.json"

class JadiList:
    def __init__(self):
        self.bots_command = CommandHandler("bots", self.list_bots)

    async def list_bots(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        print("CMD | Comando /bots ejecutado.")
        if not os.path.exists(SUBBOTS_FILE):
            await update.message.reply_text("⚠️ No hay subbots registrados.", reply_to_message_id=update.message.message_id)
            return

        with open(SUBBOTS_FILE, "r") as f:
            try:
                bots = json.load(f)
            except json.JSONDecodeError:
                await update.message.reply_text("⚠️ Error al leer el archivo de subbots.", reply_to_message_id=update.message.message_id)
                return

        if not bots:
            await update.message.reply_text("⚠️ No hay subbots activos.", reply_to_message_id=update.message.message_id)
            return

        text = "╔━━━━━ JADIBOT - LIST\n"
        for i, bot in enumerate(bots, start=1):
            nombre = bot.get("name", "Desconocido")
            token = bot.get("token", "???" * 10)
            hora = bot.get("hora", "??:??")
            text += f"✦ {i}. {nombre}\n✧ Token: {token[:10]}\n✦ Hora: {hora}\n╚━━━━━━━━━━━━━━"

        await update.message.reply_text(text, reply_to_message_id=update.message.message_id)

def setup():
    return JadiList()