from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import time

application = ApplicationBuilder().token("TOKEN").build()

class Ping:
    def __init__(self):
        self.ping_command = CommandHandler("ping", self.ping)
        
    async def ping(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        print("CMD | Comando /ping ejecutado")
        start = time.time()
        message = await update.message.reply_text("✰ ¡Pong!\nCalculando Tiempo...")
        end = time.time()
        latency = (end - start) * 1000
        await message.edit_text(f"✰ ¡Pong!\nTiempo ⴵ {latency:.2f}ms", parse_mode="Markdown")

def setup():
    return Ping()