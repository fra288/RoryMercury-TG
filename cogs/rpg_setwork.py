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

TRABAJOS_VALIDOS = ["Minero", "Pescador", "Cazador", "Granjero", "Herrero", "Empresario", "Jefe de Mafia"]

class SetWork:
    def __init__(self):
        self.setwork_command = CommandHandler("setwork", self.setwork)

    async def setwork(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not context.args:
            await update.message.reply_text("💼 Usa /setwork <trabajo>. Trabajos disponibles: " + ", ".join(TRABAJOS_VALIDOS))
            return

        trabajo = context.args[0].capitalize()
        if trabajo not in TRABAJOS_VALIDOS:
            await update.message.reply_text(f"❌ Trabajo inválido. Trabajos disponibles: {', '.join(TRABAJOS_VALIDOS)}")
            return

        user_id = update.effective_user.id
        data = load_economy()
        user = init_user(user_id)
        uid = init_user(user_id)

        user["trabajo"] = trabajo
        data[str(user_id)] = user
        save_economy(data)

        await update.message.reply_text(f"✅ Has cambiado tu trabajo a: {trabajo}.")

def setup():
    return SetWork()