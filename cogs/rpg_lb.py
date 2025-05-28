from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
import json, os

ECONOMY_FILE = "data/economia.json"

def ensure_economy():
    if not os.path.exists(ECONOMY_FILE):
        with open(ECONOMY_FILE, "w") as f:
            json.dump({}, f)

def load_economy():
    ensure_economy()
    with open(ECONOMY_FILE, "r") as f:
        return json.load(f)

class Lb:
    def __init__(self):
        self.lb_command = CommandHandler("lb", self.lb)

    async def lb(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        data = load_economy()
        top = sorted(data.items(), key=lambda x: x[1].get("oro", 0), reverse=True)[:10]

        texto = "🏆 Top 10 más ricos:\n"
        for i, (uid, info) in enumerate(top, start=1):
            nombre = f"[Usuario {uid}]"  # Aquí puedes usar fetch_user si tienes acceso
            texto += f"{i}. {nombre} - 💰 {info.get('oro', 0)} oro\n"

        await update.message.reply_text(texto)

def setup():
    return Lb()