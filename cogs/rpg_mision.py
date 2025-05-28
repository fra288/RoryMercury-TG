from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
import random

class Mision:
    def __init__(self):
        self.mision_command = CommandHandler("mision", self.mision)

    async def mision(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        print("CMD | Comando /mision ejecutado.")
        misiones = [
            "Derrota al dragón en la cueva ardiente.",
            "Rescata al aldeano capturado.",
            "Recolecta 10 hierbas curativas del bosque.",
            "Explora las ruinas antiguas en busca de tesoros.",
            "Protege el pueblo de una invasión de goblins.",
            "Encuentra el amuleto perdido en el templo olvidado.",
            "Caza 5 lobos en la montaña nevada.",
            "Investiga los extraños sonidos en el bosque encantado.",
            "Recupera la espada mágica del rey caído.",
            "Ayuda al herrero a conseguir minerales raros.",
            "Entrega un mensaje secreto al castillo vecino.",
            "Destruye el altar oscuro en la caverna subterránea.",
            "Captura a un ladrón que roba en el mercado.",
            "Defiende el puente del ataque de orcos.",
            "Encuentra la fuente de la plaga en el pantano.",
            "Acompaña al comerciante en su ruta peligrosa.",
            "Rescata a la princesa de la torre del mago.",
            "Derrota al jefe goblin en su guarida.",
            "Explora la isla misteriosa al oeste.",
            "Recoge 3 gemas preciosas del volcán activo.",
            "Ayuda a la granjera a salvar sus cultivos.",
            "Destruye las jaulas de bestias en la fortaleza enemiga.",
            "Investiga la desaparición de viajeros en el desierto.",
            "Encuentra el mapa secreto en la biblioteca antigua.",
            "Captura a una bestia salvaje que aterroriza la aldea.",
            "Repara el puente roto para que el comercio pueda continuar.",
            "Busca el libro perdido de hechizos en la torre del mago.",
            "Derrota a la banda de bandidos en el camino real.",
            "Recupera la corona robada del rey.",
            "Protege a los comerciantes durante la caravana.",
            "Explora las catacumbas bajo la ciudad antigua.",
            "Consigue una flor rara para el sanador del pueblo.",
            "Ayuda al pescador a recuperar sus redes robadas.",
            "Derrota al espíritu maligno en el cementerio.",
            "Encuentra la fuente de luz en la cueva oscura.",
            "Reúne materiales para crear una poción poderosa.",
            "Entrega un paquete urgente a la ciudad vecina.",
            "Defiende el campamento contra ataques nocturnos.",
            "Rescata a los prisioneros de la fortaleza enemiga."
        ]
        await update.message.reply_text("🗺️ Nueva misión:\n\n" + random.choice(misiones), reply_to_message_id=update.message.message_id)

def setup():
    return Mision()