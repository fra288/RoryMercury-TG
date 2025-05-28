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
            "usuario": f"Usuario {uid}",
            "ultima_claim": "",
            "ultima_daily": "",
            "ultimo_work": ""
        }
        save_economy(data)
    return data[str(user_id)]

class Claim:
    def __init__(self):
        self.claim_command = CommandHandler("claim", self.claim)

    async def claim(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        data = load_economy()
        user = init_user(user_id)
        now = datetime.datetime.now().strftime("%Y-%m-%d")

        if user["último_claim"] == now:
            await update.message.reply_text("⛔ Ya reclamaste tu recompensa hoy.")
            return

        oro = random.randint(50, 150)
        data[str(user_id)]["oro"] += oro
        data[str(user_id)]["último_claim"] = now
        save_economy(data)

        await update.message.reply_text(f"🎁 Has reclamado {oro} monedas de oro.")

def setup():
    return Claim()