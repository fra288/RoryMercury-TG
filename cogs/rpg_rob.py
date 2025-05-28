from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
import random, json, os

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

class Rob:
    def __init__(self):
        self.rob_command = CommandHandler("rob", self.rob)

    async def rob(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not update.message.reply_to_message:
            await update.message.reply_text("💀 Debes responder al usuario que quieres robar.")
            return

        ladron_id = update.effective_user.id
        victima_id = update.message.reply_to_message.from_user.id

        if ladron_id == victima_id:
            await update.message.reply_text("🤨 No puedes robarte a ti mismo.")
            return

        data = load_economy()
        ladron = init_user(ladron_id)
        victima = init_user(victima_id)

        if victima["oro"] < 50:
            await update.message.reply_text("👀 El usuario no tiene suficiente oro para ser robado.")
            return

        exito = random.choice([True, False])
        cantidad = random.randint(30, 80)

        if exito:
            victima["oro"] -= cantidad
            ladron["oro"] += cantidad
            data[str(ladron_id)] = ladron
            data[str(victima_id)] = victima
            save_economy(data)
            await update.message.reply_text(f"🔫 Robaste exitosamente {cantidad} de oro a {update.message.reply_to_message.from_user.mention_html()}.", parse_mode="HTML")
        else:
            perdida = random.randint(20, 50)
            ladron["oro"] = max(0, ladron["oro"] - perdida)
            data[str(ladron_id)] = ladron
            save_economy(data)
            await update.message.reply_text(f"🚨 Fallaste en robar y perdiste {perdida} de oro en el intento.")

def setup():
    return Rob()