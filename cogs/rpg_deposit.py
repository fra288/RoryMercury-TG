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

class Deposit:
    def __init__(self):
        self.deposit_command = CommandHandler("deposit", self.deposit)

    async def deposit(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        args = context.args
        data = load_economy()
        user = init_user(user_id)

        if not args or not args[0].isdigit():
            await update.message.reply_text("❌ Debes ingresar una cantidad válida para depositar.")
            return

        cantidad = int(args[0])

        if cantidad > user["oro"]:
            await update.message.reply_text("❌ No tienes suficiente oro.")
            return

        user["oro"] -= cantidad
        user["banco"] += cantidad
        data[str(user_id)] = user
        save_economy(data)

        await update.message.reply_text(f"🏦 Has depositado {cantidad} monedas de oro en tu banco.")

def setup():
    return Deposit()