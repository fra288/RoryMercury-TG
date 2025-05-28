from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
import asyncio
from .subbot import launch_subbot

class JadiBotManager:
    def __init__(self):
        self.jadibot_command = CommandHandler("jadibot", self.start_subbot)

    async def start_subbot(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        if len(context.args) != 1:
            await update.message.reply_text("❌ Usa: /jadibot <TOKEN_DEL_SUBBOT>", reply_to_message_id=update.message.message_id)
            return

        subbot_token = context.args[0]

        await update.message.reply_text("🔄 Iniciando subbot...", reply_to_message_id=update.message.message_id)
        asyncio.create_task(launch_subbot(subbot_token))
        await update.message.reply_text("✅ Subbot iniciado correctamente.", reply_to_message_id=update.message.message_id)

def setup():
    return JadiBotManager()