import random
from telegram.ext import CommandHandler, ContextTypes
from telegram import Update

class PreguntaRandom:
    def __init__(self):
        self.pregunta_command = CommandHandler("pregunta", self.pregunta)

    async def pregunta(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        preguntas = [
            "¿Cuál es la capital de Francia?",
            "¿Cuál es la capital de Francia?",
            "¿Quién pintó la Mona Lisa?",
            "¿Cuál es el planeta más grande del sistema solar?",
            "¿En qué año llegó el hombre a la luna?",
            "¿Cuál es el océano más grande del mundo?",
            "¿Quién escribió 'Cien años de soledad'?",
            "¿Cuántos continentes hay en el mundo?",
            "¿Cuál es el metal más ligero?",
            "¿Cuál es el país más poblado del mundo?",
            "¿Qué gas respiramos los humanos?",
            "¿En qué país se encuentra la Torre de Pisa?",
            "¿Qué instrumento tiene teclas blancas y negras?",
            "¿Cuántos colores hay en el arcoíris?",
            "¿Qué animal es el rey de la selva?",
            "¿Quién descubrió América?",
            "¿Cuál es el río más largo del mundo?",
            "¿Qué número viene después del 99?",
            "¿Qué planeta es conocido como el planeta rojo?",
            "¿Cuál es el idioma más hablado en el mundo?",
            "¿En qué país nació el tango?",
            "¿Cuál es la capital de Japón?",
            "¿Quién escribió 'Romeo y Julieta'?",
            "¿Qué órgano del cuerpo humano bombea sangre?",
            "¿Cuál es el mamífero más grande del planeta?",
            "¿Qué día se celebra Navidad?",
            "¿Qué animal pone huevos y vuela?",
            "¿Cuál es el país más grande del mundo en superficie?",
            "¿Qué invento permite ver objetos lejanos en el cielo?",
            "¿Qué hueso protege el cerebro?",
            "¿Qué bebida se hace con uvas fermentadas?",
            "¿Cuál es el símbolo químico del oro?",
            "¿Qué planeta tiene anillos?",
            "¿Cuál es el deporte más popular del mundo?",
            "¿Qué país tiene forma de bota?",
            "¿Quién fue Albert Einstein?",
            "¿Cuántos minutos tiene una hora?",
            "¿Qué ave es símbolo de sabiduría?",
            "¿En qué continente está Egipto?",
            "¿Cuál es la fórmula del agua?",
            "¿Qué color se obtiene al mezclar rojo y azul?"
        ]
        await update.message.reply_text("📚 " + random.choice(preguntas), reply_to_message_id=update.message.message_id)
        print("CMD | Comando /pregunta ejecutado.")

def setup():
    return PreguntaRandom()