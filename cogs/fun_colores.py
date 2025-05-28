import random
from telegram.ext import CommandHandler, ContextTypes
from telegram import Update

class Colores:
    def __init__(self):
        self.colores_command = CommandHandler("colores", self.colores)

    async def colores(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        colores = ["rojo", "azul", "verde", "amarillo", "naranja", "morado", "rosado", "marrón", "negro", "blanco", "gris", "cian", "magenta", "lima", "índigo", "violeta", "beige", "dorado", "plateado", "granate", "azul marino", "verde azulado", "oliva", "coral", "turquesa", "salmón", "canela", "azul cielo", "lavanda", "melocotón", "vino", "fucsia", "verde lima", "verde esmeralda", "azul celeste", "amarillo limón", "ocre", "azul petróleo", "carbón", "ámbar", "menta", "terracota", "púrpura", "chocolate", "pizarra", "cobre", "azafrán"]
        elegido = random.choice(colores)
        await update.message.reply_text("🎨 Estoy pensando en un color... ¿Cuál crees que es? (Escribe tu respuesta)", reply_to_message_id=update.message.message_id)
        print("CMD | Comando /colores ejecutado.")

        def check(msg):
            return msg.text.lower() == elegido.lower() and msg.from_user.id == update.message.from_user.id

        try:
            msg = await context.bot.wait_for_message(timeout=15, filters=None, chat_id=update.effective_chat.id)
            if msg.text.lower() == elegido:
                await msg.reply_text("🎉 ¡Correcto! Ese era el color.", reply_to_message_id=update.message.message_id)
            else:
                await msg.reply_text(f"❌ No era correcto. El color era {elegido}.", reply_to_message_id=update.message.message_id)
        except:
            await update.message.reply_text("⏰ Se acabó el tiempo. Era " + elegido, reply_to_message_id=update.message.message_id)

def setup():
    return Colores()