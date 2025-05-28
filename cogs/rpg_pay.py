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

class Pay:
    def __init__(self):
        self.pay_command = CommandHandler("pay", self.pay)

    async def pay(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not context.args or len(context.args) < 1:
            await update.message.reply_text("💸 Usa: /pay <cantidad> respondiendo al usuario.")
            return

        if not update.message.reply_to_message:
            await update.message.reply_text("💸 Debes responder al mensaje del usuario al que quieres pagar.")
            return

        try:
            cantidad = int(context.args[0])
        except ValueError:
            await update.message.reply_text("❌ La cantidad debe ser un número.")
            return

        if cantidad <= 0:
            await update.message.reply_text("❌ La cantidad debe ser positiva.")
            return

        pagador_id = update.effective_user.id
        receptor_id = update.message.reply_to_message.from_user.id

        data = load_economy()
        pagador = init_user(pagador_id)
        receptor = init_user(receptor_id)

        if pagador["oro"] < cantidad:
            await update.message.reply_text("💰 No tienes suficiente oro.")
            return

        pagador["oro"] -= cantidad
        receptor["oro"] += cantidad

        data[str(pagador_id)] = pagador
        data[str(receptor_id)] = receptor
        save_economy(data)

        await update.message.reply_text(f"💸 Le diste {cantidad} de oro a {update.message.reply_to_message.from_user.mention_html()}.", parse_mode="HTML")

def setup():
    return Pay()