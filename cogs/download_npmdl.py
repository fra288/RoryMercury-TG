# cogs/npmdl.py
from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
import tempfile
import subprocess
import os

class Npmdl:
    def __init__(self):
        self.npmdl_command = CommandHandler("npmdl", self.npmdl)

    async def npmdl(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not context.args:
            await update.message.reply_text("Por favor, envía el nombre del paquete npm.", reply_to_message_id=update.message.message_id)
            return

        package = context.args[0]
        await update.message.reply_text(f"Descargando paquete npm '{package}'...", reply_to_message_id=update.message.message_id)

        with tempfile.TemporaryDirectory() as tmpdir:
            try:
                subprocess.run(['npm', 'pack', package], cwd=tmpdir, check=True)
                files = os.listdir(tmpdir)
                tg_file = None
                for file in files:
                    if file.endswith('.tgz'):
                        tg_file = os.path.join(tmpdir, file)
                        break
                if tg_file:
                    with open(tg_file, 'rb') as f:
                        await update.message.reply_document(document=f, reply_to_message_id=update.message.message_id)
                else:
                    await update.message.reply_text("No se encontró archivo para enviar.", reply_to_message_id=update.message.message_id)
            except Exception as e:
                await update.message.reply_text(f"Error al descargar paquete npm: {e}", reply_to_message_id=update.message.message_id)

def setup():
    return Npmdl()