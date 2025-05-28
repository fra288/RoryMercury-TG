import os
import importlib
from telegram import Update
from telegram.ext import ContextTypes, CommandHandler

OWNER_ID = 6768174513

class FixCommand:
    def __init__(self):
        self.fix_command = CommandHandler("fix", self.fix)

    async def fix(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if update.effective_user.id != OWNER_ID:
            await update.message.reply_text("❌ Solo el owner puede usar este comando.")
            return

        await update.message.reply_text("🔄 Recargando comandos...")

        try:
            # Eliminar todos los comandos actuales
            handlers = context.application.handlers
            for group in list(handlers.keys()):
                context.application.handlers[group].clear()

            # Recargar cogs
            cogs_path = "cogs"
            for filename in os.listdir(cogs_path):
                if filename.endswith(".py") and not filename.startswith("__"):
                    module_name = f"cogs.{filename[:-3]}"
                    if module_name in importlib.sys.modules:
                        importlib.reload(importlib.sys.modules[module_name])
                    else:
                        importlib.import_module(module_name)

                    module = importlib.import_module(module_name)
                    cog_instance = module.setup()

                    for attr in dir(cog_instance):
                        if attr.endswith("_command"):
                            handler = getattr(cog_instance, attr)
                            context.application.add_handler(handler)

            await update.message.reply_text("✅ Comandos actualizados correctamente.")
        except Exception as e:
            await update.message.reply_text(f"❌ Error al recargar comandos: {e}")

def setup():
    return FixCommand()