import json
import os
from telegram import Update
from telegram.ext import ContextTypes

USED_CHATS_FILE = "data/chats.json"

async def track_used_chats(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not update.effective_chat:
        return

    chat_id = str(update.effective_chat.id)

    if not os.path.exists(USED_CHATS_FILE):
        with open(USED_CHATS_FILE, "w") as f:
            json.dump([], f)

    with open(USED_CHATS_FILE, "r") as f:
        used_chats = json.load(f)

    if chat_id not in used_chats:
        used_chats.append(chat_id)
        with open(USED_CHATS_FILE, "w") as f:
            json.dump(used_chats, f)