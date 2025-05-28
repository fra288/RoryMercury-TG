from telegram import Update, User
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

class Marry:
    def __init__(self):
        self.marry_command = CommandHandler("marry", self.marry)

    async def marry(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not context.args:
            await update.message.reply_text("💍 Menciona al usuario con el que te quieres casar: /marry @usuario")
            return

        if not update.message.reply_to_message:
            await update.message.reply_text("💍 Responde al mensaje del usuario con quien te quieres casar.")
            return

        user_id = update.effective_user.id
        target: User = update.message.reply_to_message.from_user
        target_id = target.id

        if user_id == target_id:
            await update.message.reply_text("💔 No puedes casarte contigo mismo.")
            return

        data = load_economy()
        user = init_user(user_id)
        pareja = init_user(target_id)

        if user["pareja"] or pareja["pareja"]:
            await update.message.reply_text("⚠️ Uno de los dos ya está casado.")
            return

        user["pareja"] = target_id
        pareja["pareja"] = user_id

        data[str(user_id)] = user
        data[str(target_id)] = pareja
        save_economy(data)

        await update.message.reply_text(f"💞 ¡Ahora estás casado con {target.mention_html()}!", parse_mode="HTML")

def setup():
    return Marry()