# cogs/youtube.py
from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
import yt_dlp
import os
import tempfile

class Youtube:
    def __init__(self):
        self.youtube_command = CommandHandler("youtube", self.youtube)

    async def youtube(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not context.args:
            await update.message.reply_text("Por favor, envía un enlace de YouTube después del comando.", reply_to_message_id=update.message.message_id)
            return

        url = context.args[0]
        await update.message.reply_text("Descargando video... esto puede tardar un poco.", reply_to_message_id=update.message.message_id)

        with tempfile.TemporaryDirectory() as tmpdir:
            ydl_opts = {
                'format': 'best[ext=mp4]/best',
                'outtmpl': os.path.join(tmpdir, 'video.%(ext)s'),
                'noplaylist': True,
                'quiet': True,
            }
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                filepath = os.path.join(tmpdir, 'video.mp4')
                # Enviar archivo
                with open(filepath, 'rb') as f:
                    await update.message.reply_video(video=f, reply_to_message_id=update.message.message_id)
            except Exception as e:
                await update.message.reply_text(f"Error al descargar video: {e}", reply_to_message_id=update.message.message_id)

def setup():
    return Youtube()