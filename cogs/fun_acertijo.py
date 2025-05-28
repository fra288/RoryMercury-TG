import random
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes, ConversationHandler, MessageHandler, filters

ESPERANDO_RESPUESTA = 1

class Acertijo:
    def __init__(self):
        self.acertijo_command = ConversationHandler(
            entry_points=[CommandHandler("acertijo", self.iniciar_acertijo)],
            states={
                ESPERANDO_RESPUESTA: [MessageHandler(filters.TEXT & ~filters.COMMAND, self.recibir_respuesta)]
            },
            fallbacks=[],
            conversation_timeout=15,
        )
        self.pregunta_actual = None
        self.respuesta_actual = None

    async def iniciar_acertijo(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        acertijos = [
            ("¿Qué tiene cabeza, pero no tiene cuerpo?", "una moneda"),
            ("¿Qué sube y baja pero no se mueve?", "una escalera"),
            ("¿Qué tiene agujas pero no pincha?", "un reloj"),
            ("¿Qué palabra empieza con ‘e’ y solo tiene una letra?", "sobre"),
            ("¿Qué cosa se rompe pero no se puede tocar?", "una promesa"),
            ("¿Qué tiene manos pero no puede aplaudir?", "un reloj"),
            ("¿Qué puedes atrapar pero no lanzar?", "un resfriado"),
            ("¿Qué es lo que cuanto más le quitas, más grande es?", "un agujero"),
            ("¿Qué tiene un ojo pero no puede ver?", "una aguja"),
            ("¿Qué tiene patas pero no puede caminar?", "una mesa"),
            ("¿Qué tiene dientes pero no puede morder?", "un peine"),
            ("¿Qué es algo que siempre llega pero nunca llega hoy?", "mañana"),
            ("¿Qué se llena de agua pero nunca se moja?", "el mar"),
            ("¿Qué tiene ciudades pero no casas?", "un mapa"),
            ("¿Qué es algo que mientras más le quitas, más grande se vuelve?", "un agujero"),
            ("¿Qué se puede romper sin tocarlo?", "el silencio"),
            ("¿Qué tiene un corazón que no late?", "una alcachofa"),
            ("¿Qué tiene cuello pero no cabeza?", "una botella"),
            ("¿Qué se mueve sin tener piernas?", "el viento"),
            ("¿Qué tiene orejas pero no puede oír?", "el maíz"),
        ]
        self.pregunta_actual, self.respuesta_actual = random.choice(acertijos)
        await update.message.reply_text(f"🧠 Acertijo: {self.pregunta_actual}\nTienes 15 segundos para responder. ¡Escribe tu respuesta!", reply_to_message_id=update.message.message_id)
        print("CMD | Comando /acertijo ejecutado.")

        return ESPERANDO_RESPUESTA

    async def recibir_respuesta(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        texto = update.message.text.lower()
        correcta = self.respuesta_actual.lower()
        if texto == correcta:
            await update.message.reply_text("✅ ¡Correcto!", reply_to_message_id=update.message.message_id)
        else:
            await update.message.reply_text(f"❌ Incorrecto. La respuesta correcta era: {self.respuesta_actual}", reply_to_message_id=update.message.message_id)
        return ConversationHandler.END

def setup():
    return Acertijo()