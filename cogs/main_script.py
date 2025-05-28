import aiohttp
import json
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
import os

class MenuScript:
    def __init__(self):
        self.menu_script_command = CommandHandler("sc", self.menu_script)

    async def menu_script(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        repo_owner = "memochiko"
        repo_name = "RoryMercury-TG"

        json_path = os.path.join("info_bot", "script.json")
        try:
            with open(json_path, "r", encoding="utf-8") as f:
                local_info = json.load(f)
        except Exception as e:
            local_info = {
                "nombre": "Desconocido",
                "version": "N/A",
                "descripcion": "No disponible",
                "autor": "N/A",
                "libreria": "N/A"
            }

        api_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(api_url) as response:
                    if response.status != 200:
                        await update.message.reply_text("⚠️ No se pudo obtener la información del repositorio.")
                        return
                    data = await response.json()
        except Exception as e:
            await update.message.reply_text(f"❌ Error al obtener datos del repositorio:\n{e}")
            return

        # Datos combinados
        nombre = local_info.get("nombre", "N/A")
        version = local_info.get("version", "N/A")
        descripcion_local = local_info.get("descripcion", "N/A")
        autor = local_info.get("autor", "N/A")
        libreria = local_info.get("libreria", "N/A")

        descripcion_git = data.get("description", "N/A")
        creador = data.get("owner", {}).get("login", "N/A")
        estrellas = data.get("stargazers_count", 0)
        forks = data.get("forks_count", 0)
        issues = data.get("open_issues_count", 0)
        updated = data.get("updated_at", "N/A")
        repo_url = data.get("html_url", "")

        texto = f"""📦 <b>Información del Bot</b>

🔖 <b>Nombre:</b> {nombre}
📌 <b>Versión:</b> {version}
📄 <b>Descripción:</b> {descripcion_local}
👑 <b>Autor:</b> {autor}
📚 <b>Librería:</b> {libreria}

🌐 <b>GitHub:</b> <a href="{repo_url}">{repo_url}</a>
⭐ <b>Estrellas:</b> {estrellas} | 🍴 <b>Forks:</b> {forks}
🐞 <b>Issues:</b> {issues} | 📆 <b>Últ. actualización:</b> {updated}
👤 <b>Creador:</b> {creador}
"""

        await update.message.reply_text(texto, parse_mode="HTML", disable_web_page_preview=True)

def setup():
    return MenuScript()