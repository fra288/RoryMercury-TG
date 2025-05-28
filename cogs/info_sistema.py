import platform
import psutil
import os
import socket
import time
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

start_time = time.time()

def get_uptime():
    elapsed = int(time.time() - start_time)
    days, remainder = divmod(elapsed, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{days}d {hours}h {minutes}m {seconds}s"

class Sistema:
    def __init__(self):
        self.sistema_command = CommandHandler("sistema", self.sistema)

    async def sistema(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        try:
            host = socket.gethostname()
            plataforma = platform.system()
            arquitectura = platform.machine()

            mem = psutil.virtual_memory()
            total_ram = mem.total / (1024 ** 3)
            libre_ram = mem.available / (1024 ** 3)
            usada_ram = mem.used / (1024 ** 3)

            disco = psutil.disk_usage('/')
            total_disco = disco.total / (1024 ** 3)
            usado_disco = disco.used / (1024 ** 3)
            libre_disco = disco.free / (1024 ** 3)
            porcentaje_disco = disco.percent

            proceso = psutil.Process(os.getpid())
            memoria = proceso.memory_info()
            rss = memoria.rss / (1024 ** 2)
            heap_total = memoria.vms / (1024 ** 2)
            heap_usado = getattr(memoria, 'shared', 0) / (1024 ** 2)

            mensaje = f"🖥️ *Estado del Sistema:*\n\n╭───[ 💻 Sistema ]\n├ Host: {host}\n├ Plataforma: {plataforma}\n├ Arquitectura: {arquitectura}\n╰ Uptime: {get_uptime()}\n\n╭───[ 🧠 RAM ]\n├ Total: {total_ram:.2f} GB\n├ Usada: {usada_ram:.2f} GB\n╰ Libre: {libre_ram:.2f} GB\n\n╭───[ 📦 Node.js Memory ]\n├ RSS: {rss:.2f} MB\n├ Heap Total: {heap_total:.2f} MB\n╰ Heap Usado: {heap_usado:.2f} MB\n\n╭───[ 💾 Disco ]\n├ Total: {total_disco:.2f} GB\n├ Usado: {usado_disco:.2f} GB\n├ Libre: {libre_disco:.2f} GB\n╰ Uso: {porcentaje_disco}%"
            
            image_system = open("media/sistema.png", "rb")
            
            await update.message.reply_photo(
                photo=image_system,
                caption=mensaje,
                parse_mode="Markdown", 
                reply_to_message_id=update.message.message_id
            )
            print("CMD | Comando / ejecutado.")
            image_system.close()
        except Exception as e:
            await update.message.reply_text(f"❌ Error al obtener información del sistema.\n\n{e}", reply_to_message_id=update.message.message_id)

def setup():
    return Sistema()