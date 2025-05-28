import json
import os
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

OWNER_ID = 6768174513
ECONOMIA_PATH = "data/economia.json"

class SoyOP:
    def __init__(self):
        self.soyop_command = CommandHandler("soyop", self.soyop)

    async def soyop(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = str(update.effective_user.id)
        if update.effective_user.id != OWNER_ID:
            await update.message.reply_text("❌ Este comando solo puede usarlo el owner.")
            return

        if not os.path.exists(ECONOMIA_PATH):
            with open(ECONOMIA_PATH, "w") as f:
                f.write("{}")

        with open(ECONOMIA_PATH, "r") as f:
            data = json.load(f)

        if user_id not in data:
            data[user_id] = {
                "oro": 0,
                "banco": 0,
                "xp": 0,
                "nivel": 1,
                "trabajo": "",
                "inventario": [],
                "pareja": None,
                "ultima_claim": "",
                "ultima_daily": "",
                "ultimo_work": ""
            }

        # Hacer al usuario OP
        data[user_id]["oro"] = 9999999
        data[user_id]["banco"] = 9999999
        data[user_id]["xp"] = 9999999
        data[user_id]["nivel"] = 100
        data[user_id]["inventario"] = [
            "espada_infinita",
            "armadura_mitica",
            "pocion_curacion_total",
            "anillo_del_caos",
            "vara_legendaria"
        ]

        with open(ECONOMIA_PATH, "w") as f:
            json.dump(data, f, indent=4)

        await update.message.reply_text("💥 Te has convertido en un ser omnipotente del RPG. ¡Aplasta con poder infinito!")

def setup():
    return SoyOP()