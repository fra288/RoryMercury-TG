from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
import yt_dlp
import os
import asyncio

class TikTokMP3:
    def __init__(self):
        self.tiktokmp3_command = CommandHandler("tiktokmp3", self.tiktokmp3)

    async def tiktokmp3(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if not context.args:
            await update.message.reply_text("Por favor, envía la URL del video de TikTok.\nEjemplo: /tiktokmp3 https://www.tiktok.com/@usuario/video/123456789", reply_to_message_id=update.message.message_id)
            return

        url = context.args[0]
        await update.message.reply_text("Descargando audio...")

        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': 'downloads/%(id)s.%(ext)s',
            'quiet': True,
            'no_warnings': True,
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }

        os.makedirs("downloads", exist_ok=True)

        try:
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                mp3_filename = os.path.splitext(filename)[0] + ".mp3"

            with open(mp3_filename, 'rb') as audio_file:
                await update.message.reply_audio(audio_file, title=info.get('title', 'Audio TikTok'), reply_to_message_id=update.message.message_id)

            os.remove(mp3_filename)

        except Exception as e:
            await update.message.reply_text(f"Error al descargar el audio: {e}", reply_to_message_id=update.message.message_id)

def setup():
    return TikTokMP3()