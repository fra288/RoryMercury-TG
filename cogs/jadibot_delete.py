from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
import json
import os
import signal

SUBBOTS_FILE = "jadibots/subbots.json"

OWNER_ID = 6768174513

class DelBot:
    def __init__(self):
        self.delbot_command = CommandHandler("delbot", self.delete_bots)

    async def delete_bots(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        print("CMD | Comando /delbot ejecutado.")
        if update.effective_user.id != OWNER_ID:
            await update.message.reply_text("❌ Solo mi creador puede usar este comando.", reply_to_message_id=update.message.message_id)
            return

        if not os.path.exists(SUBBOTS_FILE):
            await update.message.reply_text("⚠️ No hay subbots registrados.", reply_to_message_id=update.message.message_id)
            return

        with open(SUBBOTS_FILE, "r") as f:
            bots = json.load(f)

        if not bots:
            await update.message.reply_text("⚠️ No hay subbots activos.", reply_to_message_id=update.message.message_id)
            return

        for bot in bots:
            pid = bot.get("pid")
            if pid:
                try:
                    os.kill(pid, signal.SIGTERM)
                except Exception as e:
                    print(f"Error al terminar proceso {pid}: {e}")

        os.remove(SUBBOTS_FILE)
        await update.message.reply_text("✅ Todos los subbots han sido eliminados.", reply_to_message_id=update.message.message_id)

def setup():
    return DelBot()