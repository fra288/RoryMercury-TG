from telegram.ext import MessageHandler, ContextTypes, filters
from telegram import Update

class UnknownCommand:
    def __init__(self):
        # Este handler captura todos los comandos desconocidos
        self.unknown_command = MessageHandler(filters.COMMAND, self.unknown)

    async def unknown(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("❌ Comando no reconocido. Usa /menu para ver la lista de comandos disponibles.")
        print("SYS | Sistema Unknown ejecutado.")

def setup():
    return UnknownCommand()