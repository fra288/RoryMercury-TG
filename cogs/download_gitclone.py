# cogs/gitclone.py
from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
import tempfile
import git
import shutil

class GitClone:
    def __init__(self):
        self.gitclone_command = CommandHandler("gitclone", self.gitclone)

    async def gitclone(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not context.args:
            await update.message.reply_text("Por favor, envía la URL del repositorio Git.", reply_to_message_id=update.message.message_id)
            return

        url = context.args[0]
        await update.message.reply_text("Clonando repositorio...", reply_to_message_id=update.message.message_id)

        with tempfile.TemporaryDirectory() as tmpdir:
            try:
                repo_path = tmpdir + "/repo"
                git.Repo.clone_from(url, repo_path)
                await update.message.reply_text("Repositorio clonado correctamente. No puedo enviar carpetas por Telegram.", reply_to_message_id=update.message.message_id)
            except Exception as e:
                await update.message.reply_text(f"Error al clonar repositorio: {e}", reply_to_message_id=update.message.message_id)

def setup():
    return GitClone()