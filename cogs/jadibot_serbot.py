import json
import os
import threading
import asyncio
import importlib
from datetime import datetime
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

SUBBOTS_FILE = "jadibots/subbots.json"
application = ApplicationBuilder().token("TOKEN").build()

class JadiBotManager:
    def __init__(self):
        os.makedirs("jadibots", exist_ok=True)
        self.jadibot_command = CommandHandler("jadibot", self.handle_jadibot)

    def load_subbots(self):
        if not os.path.exists(SUBBOTS_FILE):
            return []
        with open(SUBBOTS_FILE, "r") as f:
            return json.load(f)

    def save_subbots(self, data):
        with open(SUBBOTS_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def start_subbot(self, token):
        def run():
            asyncio.run(self.launch_subbot(token))
        threading.Thread(target=run, daemon=True).start()

    async def launch_subbot(self, token):
        try:
            application = ApplicationBuilder().token(token).build()

            # 🧠 Cargar todos los cogs como en main.py
            cogs_path = "./cogs"
            for filename in os.listdir(cogs_path):
                if filename.endswith(".py") and not filename.startswith("__"):
                    module_name = filename[:-3]
                    module = importlib.import_module(f"cogs.{module_name}")
                    cog_instance = module.setup()
                    for attr_name in dir(cog_instance):
                        if attr_name.endswith("_command"):
                            handler = getattr(cog_instance, attr_name)
                            application.add_handler(handler)

            print(f"[SUBBOT] Subbot iniciado con token {token[:10]}...")
            await application.run_polling()
        except Exception as e:
            print(f"[ERROR SUBBOT] No se pudo iniciar subbot: {e}")

    async def handle_jadibot(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        print("CMD | Comando /jadibot ejecutado.")
        if not context.args:
            await update.message.reply_text("❌ Usa: /jadibot <TOKEN>", reply_to_message_id=update.message.message_id)
            return

        token = context.args[0]

        try:
            bot = Bot(token)
            me = await bot.get_me()

            data = self.load_subbots()
            for b in data:
                if b["id"] == me.id:
                    await update.message.reply_text("⚠️ Ese subbot ya está registrado.", reply_to_message_id=update.message.message_id)
                    return

            data.append({
                "id": me.id,
                "username": me.username,
                "nombre": me.first_name,
                "token": token,
                "hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })
            self.save_subbots(data)

            self.start_subbot(token)

            await update.message.reply_text(f"✅ Subbot @{me.username} iniciado con éxito.", reply_to_message_id=update.message.message_id)

        except Exception as e:
            await update.message.reply_text(f"❌ Error al iniciar subbot: {e}", reply_to_message_id=update.message.message_id)

def setup():
    return JadiBotManager()