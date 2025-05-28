from telegram import Update
from telegram.ext import MessageHandler, ContextTypes, filters

class Welcome:
    def __init__(self):
        self.welcome_command = MessageHandler(filters.StatusUpdate.NEW_CHAT_MEMBERS, self.send_welcome)

    async def send_welcome(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        for new_user in update.message.new_chat_members:
            nombre = new_user.first_name
            chat = update.effective_chat

            mensaje = (
                f"👋 ¡Bienvenido/a {nombre} al grupo *{chat.title}*!\n"
                "Estamos felices de tenerte aquí 🎉.\n"
                "Por favor, revisa las reglas del grupo y disfruta tu estancia."
            )
            await update.message.reply_text(mensaje, parse_mode="Markdown")
            print("SYS | Sistema Welcome ejecutado.")

def setup():
    return Welcome()