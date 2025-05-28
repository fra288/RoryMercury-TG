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

def init_user(user_id):
    data = load_economy()
    if str(user_id) not in data:
        data[str(user_id)] = {
            "trabajo": "Desempleado"
        }
        with open(ECONOMY_FILE, "w") as f:
            json.dump(data, f, indent=2)
    return data[str(user_id)]

class WorkPerfil:
    def __init__(self):
        self.workperfil_command = CommandHandler("workperfil", self.workperfil)

    async def workperfil(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        user = init_user(user_id)

        trabajo = user.get("trabajo", "Desempleado")
        await update.message.reply_text(f"💼 Tu trabajo actual es: {trabajo}")

def setup():
    return WorkPerfil()
