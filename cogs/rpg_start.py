from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

application = ApplicationBuilder().token("TOKEN").build()

class Start:
    def __init__(self):
        self.start_command = CommandHandler("start", self.start)

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        print("CMD | Comando /start ejecutado.")
        await update.message.reply_text("Hola, ya estoy activada, que podemos hacer ahora?", reply_to_message_id=update.message.message_id)

def setup():
    return Start()