import time
import json
import os
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

start_time = time.time()
TG_BOT = "Rory Mercury-TG"
application = ApplicationBuilder().token("TOKEN").build()

def get_uptime() -> str:
    elapsed = int(time.time() - start_time)
    days, remainder = divmod(elapsed, 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"{days}d {hours}h {minutes}m {seconds}s"
    
def load_json_file(path):
    if os.path.exists(path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            return []
    return []

class Menu:
    def __init__(self):
        self.menu_command = CommandHandler("menu", self.menu)

    async def menu(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        print("CMD | Comando /menu ejecutado")
        user = update.effective_user
        username = user.username or user.first_name
        version = "1.0.0"
        
        usuarios_registrados = load_json_file("usuarios.json")
        usuarios_activos = load_json_file("activos.json")
        
        total_reg = len(usuarios_registrados)
        total_act = len(usuarios_activos)
        await update.message.reply_text(f"¡Hola @{username}! Mi nombre es {TG_BOT}\n\nAqui tienes mi lista de comandos\n\n╔━━━━━ *INFO - BOT*\n✧  👤 Tipo: Waifu\n✦  💫 Usuarios Registrados: {total_reg}\n✧  💫 Usuarios Activos: {total_act}\n✦  🛠 Modo: Pública\n✧  ✨ PyTGBot: Multi Device\n✦  🪐 Activada: {get_uptime()}\n✧  🤴 *Creador:* wa.me/56967964633\n✦  🛠 *Version:* {version}\n╚━━━━━━━━━━━━━━\n\n╭┈ SUB-BOTS\n│ ✦ /jadibot\n│ ✦ /delbot (owner)\n│ ✦ /bots\n╰────────────────\n\n╭┈ DOWNLOADERS\n│ ✦ /facebook\n│ ✦ /youtube\n│ ✦ /tiktok\n│ ✦ /tiktokmp3\n│ ✦ /spotify (reparando)\n│ ✦ /npmdl\n│ ✦ /play\n│ ✦ /giclone (mejorando)\n╰────────────────\n\n╭┈ FUN\n│ ✦ /ppt\n│ ✦ /vrddoreto\n│ ✦ /pregunta\n│ ✦ /intenta\n│ ✦ /emoquiz\n│ ✦ /dado\n│ ✦ /colores\n│ ✦ /chiste\n│ ✦ /adivina\n│ ✦ /acertijo\n╰────────────────\n\n╭┈ GRUPOS\n│ ✦ /undefined\n│ ✦ /undefined\n│ ✦ /undefined\n╰────────────────\n\n╭┈ RPG\n│ ✦ /curar\n│ ✦ /dormir\n│ ✦ /mision\n│ ✦ /reg\n│ ✦ /unreg\n╰────────────────\n\n╭┈ TOOLS\n│ ✦ /undefined\n│ ✦ /undefined\n│ ✦ /undefined\n╰────────────────\n\n📌 Nota: Se iran agregando mas comandos a medida del tiempo, tenga paciencia.", reply_to_message_id=update.message.message_id)

def setup():
    return Menu()