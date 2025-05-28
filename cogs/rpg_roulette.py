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

class Roulette:
    def __init__(self):
        self.roulette_command = CommandHandler("roulette", self.roulette)

    async def roulette(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not context.args:
            await update.message.reply_text("🎰 Usa: /roulette <cantidad>")
            return

        try:
            apuesta = int(context.args[0])
        except ValueError:
            await update.message.reply_text("❌ La cantidad debe ser un número.")
            return

        user_id = update.effective_user.id
        data = load_economy()
        user = init_user(user_id)

        if apuesta <= 0 or apuesta > user["oro"]:
            await update.message.reply_text("❌ Apuesta inválida o no tienes suficiente oro.")
            return

        resultado = random.choice(["ganas", "pierdes"])
        if resultado == "ganas":
            ganancia = apuesta * 2
            user["oro"] += apuesta
            mensaje = f"🎉 ¡Ganaste la ruleta! Ahora tienes +{apuesta} oro."
        else:
            user["oro"] -= apuesta
            mensaje = f"💀 Perdiste la apuesta. Se descontaron {apuesta} de oro."

        data[str(user_id)] = user
        save_economy(data)

        await update.message.reply_text(mensaje)

def setup():
    return Roulette()