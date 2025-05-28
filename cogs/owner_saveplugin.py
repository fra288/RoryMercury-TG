from telegram import Update, MessageEntity
from telegram.ext import CommandHandler, ContextTypes
import os
import json

OWNER_ID = 6768174513

class SavePlugin:
    def __init__(self):
        self.owner_id = self.load_owner_id()

    def load_owner_id(self):
        with open("config.json", "r") as f:
            config = json.load(f)
        return int(OWNER_ID)

    async def saveplugin_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user_id = update.effective_user.id
        if user_id != self.owner_id:
            return await update.message.reply_text("Solo el dueño puede usar este comando.")

        if len(context.args) == 0:
            return await update.message.reply_text("Uso correcto: /saveplugin nombre_del_plugin.py (responde con el archivo o código)")

        filename = context.args[0]
        if not filename.endswith(".py"):
            return await update.message.reply_text("El nombre del archivo debe terminar en .py")

        reply = update.message.reply_to_message
        if not reply:
            return await update.message.reply_text("Responde este comando a un mensaje que contenga el código o el archivo del plugin.")

        if reply.text:
            code = reply.text
        elif reply.document:
            if reply.document.mime_type not in ["text/plain", "text/x-python"]:
                return await update.message.reply_text("El archivo debe ser .txt o .py")
            file = await reply.document.get_file()
            code = await file.download_as_bytearray()
            code = code.decode("utf-8")
        else:
            return await update.message.reply_text("El mensaje respondido no contiene código válido.")

        try:
            os.makedirs("cogs", exist_ok=True)
            with open(f"cogs/{filename}", "w", encoding="utf-8") as f:
                f.write(code)
            await update.message.reply_text(f"Plugin `{filename}` guardado correctamente en la carpeta cogs.")
        except Exception as e:
            await update.message.reply_text(f"Error al guardar el plugin: {e}")

def setup():
    sp = SavePlugin()
    return SavePluginHandler(sp)

class SavePluginHandler:
    def __init__(self, instance):
        self.saveplugin_command = CommandHandler("saveplugin", instance.saveplugin_command)
