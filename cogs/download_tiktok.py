# cogs/tiktok.py
from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
import yt_dlp
import tempfile
import os

class Tiktok:
    def __init__(self):
        self.tiktok_command = CommandHandler("tiktok", self.tiktok)

    async def tiktok(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not context.args:
            await update.message.reply_text("Por favor, envía el enlace del video de TikTok.", reply_to_message_id=update.message.message_id)
            return

        url = context.args[0]
        await update.message.reply_text("Descargando video de TikTok...", reply_to_message_id=update.message.message_id)

        with tempfile.TemporaryDirectory() as tmpdir:
            ydl_opts = {
                'format': 'best',
                'outtmpl': os.path.join(tmpdir, 'video.%(ext)s'),
                'quiet': True,
            }
            try:
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
                filepath = os.path.join(tmpdir, 'video.mp4')
                with open(filepath, 'rb') as f:
                    await update.message.reply_video(video=f, reply_to_message_id=update.message.message_id)
            except Exception as e:
                await update.message.reply_text(f"Error al descargar video: {e}", reply_to_message_id=update.message.message_id)

def setup():
    return Tiktok()