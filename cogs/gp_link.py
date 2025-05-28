from telegram import Update, ChatInviteLink
from telegram.ext import CommandHandler, ContextTypes
from telegram.error import BadRequest
import html

class LinkCommand:
    async def link(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        chat = update.effective_chat
        user = update.effective_user

        if chat.type == "private":
            await update.message.reply_text("❌ Este comando solo funciona en grupos.")
            return

        try:
            # Asegúrate de que el bot sea admin con permiso para invitar
            invite_link: ChatInviteLink = await context.bot.create_chat_invite_link(chat.id)
            await update.message.reply_text(
                f"🔗 Aquí tienes el link de invitación del grupo:\n{html.escape(invite_link.invite_link)}"
            )
        except BadRequest as e:
            await update.message.reply_text(
                "❌ No pude generar el link. Asegúrate de que soy administrador con permisos para invitar."
            )

def setup():
    return LinkCommand()