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

class Upgrade:
    def __init__(self):
        self.upgrade_command = CommandHandler("upgrade", self.upgrade)

    async def upgrade(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        data = load_economy()
        user = init_user(user_id)

        costo = user["nivel"] * 500

        if user["oro"] < costo:
            await update.message.reply_text(f"❌ Necesitas {costo} de oro para subir al siguiente nivel.")
            return

        user["oro"] -= costo
        user["nivel"] += 1
        data[str(user_id)] = user
        save_economy(data)

        await update.message.reply_text(f"🔼 ¡Felicidades! Has subido al nivel {user['nivel']}.")

def setup():
    return Upgrade()