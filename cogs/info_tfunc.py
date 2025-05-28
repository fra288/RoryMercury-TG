from telegram.ext import CommandHandler, ContextTypes
from telegram import Update
import os

class Funciones:
    def __init__(self):
        self.funciones_command = CommandHandler("funciones", self.funciones)

    async def funciones(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        ruta = "cogs"
        comandos = []

        for archivo in os.listdir(ruta):
            if archivo.endswith(".py") and archivo != "__init__.py":
                nombre = archivo.replace(".py", "")
                comandos.append(f"✦ {nombre}")

        total = len(comandos)
        lista = "\n".join(sorted(comandos))

        mensaje = (
            f"╭┈ FUNCIONES\n"
            f"  ✨ Funciones Totales: {total}\n"
            f"  Lista de Funciones:\n\n"
            f"{lista}\n"
            f"╰──────────────"
        )

        await update.message.reply_text(mensaje)
        print("CMD | Comando /funciones ejecutado")
        print(mensaje)

def setup():
    return Funciones()