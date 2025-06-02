from telegram.ext import ChatMemberHandler, ContextTypes
from telegram import Update

class UserPromote:
    def __init__(self):
        self.promote = ChatMemberHandler(self.on_user_promoted, ChatMemberHandler.CHAT_MEMBER)

    async def on_user_promoted(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        old = update.chat_member.old_chat_member
        new = update.chat_member.new_chat_member

        if old.status != "administrator" and new.status == "administrator":
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"🛡️ {new.user.mention_html()} ha sido *promovido a administrador*.",
                parse_mode="HTML"
            )

def setup():
    return UserPromote()