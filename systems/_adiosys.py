from telegram import Update
from telegram.ext import MessageHandler, ContextTypes, filters

class Farewell:
    def __init__(self):
        self.farewell_command = MessageHandler(filters.StatusUpdate.LEFT_CHAT_MEMBER, self.send_farewell)

    async def send_farewell(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.message.left_chat_member
        chat = update.effective_chat

        mensaje = (
            f"👋 {user.first_name} ha salido del grupo *{chat.title}*.\n"
            "¡Buena suerte en tu camino!"
        )
        await update.message.reply_text(mensaje, parse_mode="Markdown")
        print("SYS | Sistema Adios ejecutado.")

def setup():
    return Farewell()