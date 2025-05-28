from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram import Update

application = ApplicationBuilder().token("TOKEN").build()

class Owner:
    def __init__(self):
        self.owner_command = CommandHandler("owner", self.owner)

    async def owner(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        print("CMD | Comando /owner ejecutado")
        owner_txt = "Hola soy Rury Mercury-TG, creado por Memo Chiko.\n\nAqui estan los contactos de mi Owner.\n\n📧 Correo Electronico\nmemochiko.oficial@gmail.com\n✨ GitHub\nhttps://github.com/memochiko\n💬 Numero de WhatsApp\n+56 9 6796 4633\n\nPowered by Nightmoon Club & Memo Chiko"
        
        image_owner = open("media/memochiko.png", "rb")
        
        await update.message.reply_photo(
            photo=image_owner,
            caption=owner_txt, 
            reply_to_message_id=update.message.message_id
        )
        image_owner.close()

def setup():
    return Owner()