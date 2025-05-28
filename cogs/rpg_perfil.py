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

class Perfil:
    def __init__(self):
        self.perfil_command = CommandHandler("perfil", self.perfil)

    async def perfil(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        user_data = init_user(user.id)

        perfil_msg = (
            f"👤 Perfil de {user.first_name}\n"
            f"💰 Oro: {user_data['oro']}\n"
            f"🏦 Banco: {user_data['banco']}\n"
            f"⭐ Nivel: {user_data['nivel']} (XP: {user_data['xp']})\n"
            f"❤️ Esposo/a: {user_data['pareja'] or 'Ninguno'}\n"
            f"🧰 Trabajo: {user_data['trabajo']}"
        )
        await update.message.reply_text(perfil_msg)

def setup():
    return Perfil()