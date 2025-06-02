from telegram.ext import ChatMemberHandler, ContextTypes
from telegram import Update

class UserDemote:
    def __init__(self):
        self.demote = ChatMemberHandler(self.on_user_demoted, ChatMemberHandler.CHAT_MEMBER)

    async def on_user_demoted(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        old = update.chat_member.old_chat_member
        new = update.chat_member.new_chat_member

        if old.status == "administrator" and new.status not in ["administrator", "creator"]:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=f"⚠️ {new.user.mention_html()} ha sido *removido como administrador*.",
                parse_mode="HTML"
            )

def setup():
    return UserDemote()