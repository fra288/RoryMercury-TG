import os
from telegram.ext import CommandHandler, ContextTypes
from telegram import Update, InputFile

OWNER_ID = 6768174513

class GetPluginCommand:
    def __init__(self):
        self.getplugin_command = CommandHandler("getplugin", self.getplugin)

    async def getplugin(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        print("CMD | Comando /getplugin ejecutado.")
        
        user_id = update.effective_user.id
        if user_id != OWNER_ID:
            await update.message.reply_text("❌ Este comando solo puede usarlo el owner.")
            return

        if not context.args:
            await update.message.reply_text("❌ Uso inválido. Ejemplo: /getplugin rpg_xp")
            return

        plugin_name = context.args[0]
        plugin_path = f"cogs/{plugin_name}.py"

        if not os.path.exists(plugin_path):
            await update.message.reply_text("❌ El plugin especificado no existe.")
            return

        await update.message.reply_text("📦 Enviando plugin en un momento...")

        try:
            with open(plugin_path, "rb") as f:
                await context.bot.send_document(
                    chat_id=update.effective_chat.id,
                    document=InputFile(f, filename=f"{plugin_name}.py"),
                    caption=f"📁 Plugin: `{plugin_name}`",
                    parse_mode="Markdown"
                )
        except Exception as e:
            await update.message.reply_text(f"❌ No se pudo enviar el plugin.\nError: {e}")

def setup():
    return GetPluginCommand()