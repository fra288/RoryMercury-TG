from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update
import time

START_TIME = time.time()
application = ApplicationBuilder().token("TOKEN").build()

def get_uptime():
    seconds = int(time.time() - START_TIME)
    h = seconds // 3600
    m = (seconds % 3600) // 60
    s = seconds % 60
    return f"{h}h {m}m {s}s"

class Uptime:
    def __init__(self):
        self.uptime_command = CommandHandler("uptime", self.uptime)

    async def uptime(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        print(f"CMD | Comando /uptime ejecutado, Activa: {get_uptime()}")
        await update.message.reply_text(f"Tiempo activa: {get_uptime()}", reply_to_message_id=update.message.message_id)

def setup():
    return Uptime()