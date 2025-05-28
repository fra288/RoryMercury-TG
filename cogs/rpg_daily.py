from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
import json, os, random, datetime

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

class Daily:
    def __init__(self):
        self.daily_command = CommandHandler("daily", self.daily)

    async def daily(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        data = load_economy()
        user = init_user(user_id)
        now = datetime.datetime.now().strftime("%Y-%m-%d")

        if user["último_daily"] == now:
            await update.message.reply_text("⛔ Ya recibiste tu daily hoy.")
            return

        oro = random.randint(200, 500)
        data[str(user_id)]["oro"] += oro
        data[str(user_id)]["último_daily"] = now
        save_economy(data)

        await update.message.reply_text(f"🗓️ Has recibido {oro} monedas de oro como recompensa diaria.")

def setup():
    return Daily()