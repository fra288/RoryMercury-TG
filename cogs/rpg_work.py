from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
import random, json, os
from datetime import datetime, timedelta

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

class Work:
    def __init__(self):
        self.work_command = CommandHandler("work", self.work)

    async def work(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        username = update.effective_user.first_name
        data = load_economy()
        user = init_user(user_id)

        now = datetime.now()
        last_time_str = user.get("último_work", "")
        if last_time_str:
            last_time = datetime.strptime(last_time_str, "%Y-%m-%d %H:%M:%S")
            if now - last_time < timedelta(minutes=5):
                restante = timedelta(minutes=5) - (now - last_time)
                await update.message.reply_text(f"🕐 Espera {restante.seconds // 60} minutos para trabajar de nuevo.")
                return

        trabajo = user.get("trabajo", "Sin trabajo")
        if trabajo == "Sin trabajo":
            await update.message.reply_text("❌ No tienes un trabajo. Usa /setwork para elegir uno.")
            return

        ganancias = random.randint(100, 300)
        user["oro"] += ganancias
        user["xp"] += random.randint(10, 30)
        user["último_work"] = now.strftime("%Y-%m-%d %H:%M:%S")

        data[str(user_id)] = user
        save_economy(data)

        await update.message.reply_text(f"🛠️ {username}, trabajaste como {trabajo} y ganaste {ganancias} de oro.")

def setup():
    return Work()