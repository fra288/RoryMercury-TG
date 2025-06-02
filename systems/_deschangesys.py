from telegram.ext import MessageHandler, ContextTypes, filters
from telegram import Update

class GroupDescriptionChange:
    def __init__(self):
        self.description_change = MessageHandler(filters.StatusUpdate.NEW_CHAT_DESCRIPTION, self.on_group_description_change)

    async def on_group_description_change(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text(f"📄 La descripción del grupo fue actualizada:\n\n*{update.message.new_chat_description}*", parse_mode="Markdown")

def setup():
    return GroupDescriptionChange()