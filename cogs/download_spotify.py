from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
import subprocess
import tempfile
import os

class Spotify:
    def __init__(self):
        self.spotify_command = CommandHandler("spotify", self.spotify)

    async def spotify(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not context.args:
            await update.message.reply_text("Por favor, envía un enlace de Spotify después del comando.", reply_to_message_id=update.message.message_id)
            return
        url = context.args[0]
        await update.message.reply_text("Descargando canción de Spotify...", reply_to_message_id=update.message.message_id)

        with tempfile.TemporaryDirectory() as tmpdir:
            outpath = os.path.join(tmpdir, 'song.mp3')
            try:
                subprocess.run(['spotdl', url, '--output', outpath], check=True)
                with open(outpath, 'rb') as f:
                    await update.message.reply_audio(audio=f, reply_to_message_id=update.message.message_id)
            except Exception as e:
                await update.message.reply_text(f"Error al descargar de Spotify: {e}", reply_to_message_id=update.message.message_id)

def setup():
    return Spotify()