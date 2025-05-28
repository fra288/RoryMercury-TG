import json
import os
import importlib
import importlib.util
import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from telegram import BotCommand, Update
from data.commands import get_commands
from cogs.gp_link import setup

# ----------------------------- Manejo de chats usados -----------------------------

CHATS_FILE = "data/chats.json"

def load_chats():
    if not os.path.exists(CHATS_FILE):
        with open(CHATS_FILE, "w") as f:
            json.dump([], f)
    with open(CHATS_FILE, "r") as f:
        return json.load(f)

def save_chat(chat_id: int):
    chats = load_chats()
    if chat_id not in chats:
        chats.append(chat_id)
        with open(CHATS_FILE, "w") as f:
            json.dump(chats, f)

async def registrar_chat(update: Update, _):
    chat_id = update.effective_chat.id
    save_chat(chat_id)

# -----------------------------------------------------------------------------------------

def load_config():
    with open("config.json", "r") as f:
        return json.load(f)

def load_users():
    if not os.path.isfile("usuarios.json"):
        with open("usuarios.json", "w") as f:
            f.write("[]")
    with open("usuarios.json", "r") as f:
        return json.load(f)

def save_users(users):
    with open("usuarios.json", "w") as f:
        json.dump(users, f, indent=4)

def load_jadibots():
    jadibots_path = "jadibots"
    if not os.path.exists(jadibots_path):
        print("🔧 Carpeta 'jadibots' no encontrada. Saltando carga de subbots.")
        return

    for folder in os.listdir(jadibots_path):
        folder_path = os.path.join(jadibots_path, folder)
        subbot_path = os.path.join(folder_path, "subbot.py")
        if os.path.isdir(folder_path) and os.path.isfile(subbot_path):
            try:
                spec = importlib.util.spec_from_file_location(f"jadibots.{folder}.subbot", subbot_path)
                subbot_module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(subbot_module)
                if hasattr(subbot_module, "run_subbot"):
                    asyncio.create_task(subbot_module.run_subbot())
                    print(f"✅ Subbot cargado: {folder}")
                else:
                    print(f"⚠️ El archivo subbot.py en {folder} no tiene 'run_subbot()'")
            except Exception as e:
                print(f"❌ Error al cargar subbot {folder}: {e}")

async def async_main():
    config = load_config()
    link_command = setup()
    application = ApplicationBuilder().token(config["TOKEN"]).build()

    application.add_handler(MessageHandler(filters.ALL, registrar_chat), group=999)
    application.add_handler(CommandHandler("link", link_command.link))

    commands = get_commands()
    await application.bot.set_my_commands(commands)

    for folder in ["cogs", "systems"]:
        folder_path = f"./{folder}"
        for filename in os.listdir(folder_path):
            if filename.endswith(".py") and not filename.startswith("__"):
                module_name = filename[:-3]
                module = importlib.import_module(f"{folder}.{module_name}")
                cog_instance = module.setup()
                for attr_name in dir(cog_instance):
                    if attr_name.endswith("_command"):
                        handler = getattr(cog_instance, attr_name)
                        application.add_handler(handler)

    load_jadibots()

    chats = load_chats()
    for chat_id in chats:
        try:
            await application.bot.send_message(chat_id, "✅ El bot ha sido iniciado y está listo para usarse.")
        except Exception as e:
            print(f"❌ No se pudo enviar mensaje a {chat_id}: {e}")

    print("🤖 Bot principal iniciado...")
    await application.run_polling()

def main():
    try:
        import nest_asyncio
        nest_asyncio.apply()
    except ImportError:
        pass

    loop = asyncio.get_event_loop()
    if loop.is_running():
        loop.create_task(async_main())
    else:
        asyncio.run(async_main())

if __name__ == "__main__":
    main()