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

def save_economy(data):
    with open(ECONOMY_FILE, "w") as f:
        json.dump(data, f, indent=2)

def init_user(user_id):
    data = load_economy()
    if str(user_id) not in data:
        data[str(user_id)] = {
            "oro": 0,
            "banco": 0,
            "xp": 0,
            "nivel": 1,
            "trabajo": "Desempleado",
            "inventario": [],
            "pareja": None,
            "ultima_claim": "",
            "ultima_daily": "",
            "ultimo_work": ""
        }
        save_economy(data)
    return data[str(user_id)]

class Divorce:
    def __init__(self):
        self.divorce_command = CommandHandler("divorce", self.divorce)

    async def divorce(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        data = load_economy()
        user = init_user(user_id)

        if not user["esposo"]:
            await update.message.reply_text("💔 No estás casado con nadie.")
            return

        esposo_id = str(user["pareja"])
        user["pareja"] = None
        if esposo_id in data:
            data[esposo_id]["pareja"] = None

        data[str(user_id)] = user
        save_economy(data)

        await update.message.reply_text("💔 Te has divorciado exitosamente.")

def setup():
    return Divorce()