from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
import html

OWNER_ID = 6768174513

class Report:
    def __init__(self):
        self.report_command = CommandHandler("report", self.report)

    async def report(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        mensaje = " ".join(context.args)

        if not mensaje:
            await update.message.reply_text("✍️ Escribe tu reporte. Ejemplo:\n/report El comando /menu está fallando")
            return

        texto = (
            f"📩 <b>Nuevo Reporte</b>\n"
            f"👤 Usuario: {user.first_name} (@{user.username or 'sin username'})\n"
            f"🆔 ID: <code>{user.id}</code>\n"
            f"📢 Mensaje:\n{html.escape(mensaje)}"
        )

        try:
            await context.bot.send_message(chat_id=OWNER_ID, text=texto, parse_mode="HTML")
            await update.message.reply_text("✅ Tu reporte ha sido enviado correctamente al owner. ¡Gracias!")
        except Exception as e:
            await update.message.reply_text("⚠️ No pude enviar tu reporte. Intenta más tarde.")
            print(f"Error al enviar reporte: {e}")

def setup():
    return Report()