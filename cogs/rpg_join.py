from telegram.ext import CommandHandler, ContextTypes
from telegram import Update

class Join:
    def __init__(self):
        self.join = CommandHandler("join", self.join)

    async def join(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        print("CMD | Comando /join ejecutado.")
        if not context.args:
            await update.message.reply_text(
                "❌ Uso inválido. Ejemplo: /join https://t.me/+codigoDeInvitacion",
                reply_to_message_id=update.message.message_id
            )
            return

        invite_link = context.args[0]
        if not invite_link.startswith("https://t.me/+"):
            await update.message.reply_text(
                "❌ Link inválido. Asegúrate de que sea un link de invitación válido (https://t.me/+...)",
                reply_to_message_id=update.message.message_id
            )
            return

        try:
            result = await context.bot.join_chat_invite_link(invite_link)
            await update.message.reply_text(
                f"✅ Me uní correctamente a: {result.title}",
                reply_to_message_id=update.message.message_id
            )
        except Exception as e:
            await update.message.reply_text(
                f"❌ No pude unirme al grupo.\nError: {e}",
                reply_to_message_id=update.message.message_id
            )

def setup():
    return Join()