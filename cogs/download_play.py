# cogs/play.py
from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
import yt_dlp
import tempfile
import os

class Play:
    def __init__(self):
        self.play_command = CommandHandler("play", self.play)

    async def play(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not context.args:
            await update.message.reply_text("Por favor, envía el nombre de la canción o video.", reply_to_message_id=update.message.message_id)
            return

        query = " ".join(context.args)
        await update.message.reply_text(f"Buscando y descargando '{query}'", reply_to_message_id=update.message.message_id)

        with tempfile.TemporaryDirectory() as tmpdir:
            ydl_opts = {
                'format': 'bestaudio/best',
                'outtmpl': os.path.join(tmpdir, 'audio.%(ext)s'),
                'quiet': True,
                'noplaylist': True,
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    info = ydl.extract_info(f"ytsearch:{query}", download=True)['entries'][0]
                filepath = os.path.join(tmpdir, 'audio.mp3')
                with open(filepath, 'rb') as f:
                    await update.message.reply_audio(audio=f, title=info.get('title', 'Audio'), reply_to_message_id=update.message.message_id)
            except Exception as e:
                await update.message.reply_text(f"Error al descargar audio: {e}", reply_to_message_id=update.message.message_id)

def setup():
    return Play()