from telegram.ext import MessageHandler, ContextTypes, filters
from telegram import Update

class GroupPhotoChange:
    def __init__(self):
        self.photo_change = MessageHandler(filters.StatusUpdate.NEW_CHAT_PHOTO, self.on_group_photo_change)

    async def on_group_photo_change(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text("🖼️ La foto del grupo fue actualizada.")

def setup():
    return GroupPhotoChange()