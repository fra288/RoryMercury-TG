from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update
import json
import os

application = ApplicationBuilder().token("TOKEN").build()

class Registro:
    def __init__(self, load_users_func, save_users_func):
        self.load_users = load_users_func
        self.save_users = save_users_func

        self.reg_command = CommandHandler("reg", self.reg)
        self.unreg_command = CommandHandler("unreg", self.unreg)  # <-- nuevo comando

    async def reg(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        print("CMD | Comando /reg ejecutado.")
        users = self.load_users()
        user_id = update.effective_user.id

        if len(context.args) == 0:
            await update.message.reply_text("❌ Debes usar el comando así: /reg nombre.edad", reply_to_message_id=update.message.message_id)
            return

        arg = context.args[0]
        if "." not in arg:
            await update.message.reply_text("❌ Formato incorrecto. Usa: /reg nombre.edad (ej: /reg Memo-Chiko.25)", reply_to_message_id=update.message.message_id)
            return

        nombre, edad_str = arg.split(".", 1)
        nombre = nombre.strip()
        edad_str = edad_str.strip()

        if not nombre or not edad_str.isdigit():
            await update.message.reply_text("❌ Nombre o edad inválidos. Usa: /reg nombre.edad (ej: /reg Memo-Chiko.25)", reply_to_message_id=update.message.message_id)
            return

        edad = int(edad_str)

        for u in users:
            if u["id"] == user_id:
                await update.message.reply_text(f"⚠️ Ya estás registrado como {u['nombre']}, edad {u['edad']}.", reply_to_message_id=update.message.message_id)
                return

        users.append({
            "id": user_id,
            "nombre": nombre,
            "edad": edad
        })
        self.save_users(users)
        await update.message.reply_text(f"✅ Registro exitoso. Nombre: {nombre}, Edad: {edad}")

    async def unreg(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        print("CMD | Comando /unreg ejecutado.")
        users = self.load_users()
        user_id = update.effective_user.id

        # Buscar al usuario en la lista
        for u in users:
            if u["id"] == user_id:
                users.remove(u)
                self.save_users(users)
                await update.message.reply_text("✅ Has sido dado de baja correctamente.")
                return

        # Si no estaba registrado
        await update.message.reply_text("⚠️ No estabas registrado.")

def load_users():
    if not os.path.isfile("usuarios.json"):
        with open("usuarios.json", "w") as f:
            f.write("[]")
    with open("usuarios.json", "r") as f:
        return json.load(f)

def save_users(users):
    with open("usuarios.json", "w") as f:
        json.dump(users, f, indent=4)

def setup():
    return Registro(load_users, save_users)