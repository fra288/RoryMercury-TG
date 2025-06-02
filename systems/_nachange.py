from telegram.ext import MessageHandler, ContextTypes, filters
from telegram import Update

class GroupNameChange:
    def __init__(self):
        self.name_change = MessageHandler(filters.StatusUpdate.NEW_CHAT_TITLE, self.on_group_name_change)

    async def on_group_name_change(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f"📝 El nombre del grupo fue cambiado a: *{update.message.new_chat_title}*", parse_mode="Markdown")

def setup():
    return GroupNameChange()