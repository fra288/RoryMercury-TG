import random
from telegram.ext import CommandHandler, ContextTypes
from telegram import Update

class EmoQuiz:
    def __init__(self):
        self.emoquiz_command = CommandHandler("emoquiz", self.emoquiz)

    async def emoquiz(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        quizzes = [
            ("🍕🐢🐢🐢🐢", "tortugas ninja"),
            ("🌧️☔🌈", "lluvia"),
            ("🚀🌕", "luna"),
            ("🕷️🕸️🧑", "spiderman"),
            ("🧙‍♂️⚡🧝‍♂️", "harry potter"),
            ("👸❄️⛄", "frozen"),
            ("🐉🔥👦", "entrenar a tu dragón"),
            ("🏴‍☠️💰🏝️", "piratas del caribe"),
            ("👨‍🚀🌌🪐", "interestelar"),
            ("🧛‍♂️🩸🌃", "drácula"),
            ("🧟‍♂️🔫🌆", "apocalipsis zombie"),
            ("🚗💨💥", "rápidos y furiosos"),
            ("🦕🦖🏞️", "jurassic park"),
            ("🐧❄️🎶", "happy feet"),
            ("🦇🦸‍♂️🌃", "batman"),
            ("🦁👑🌍", "el rey león"),
            ("🐘👂🎪", "dumbo"),
            ("👽📞🏠", "ET"),
            ("🐼🥋🐉", "kung fu panda"),
            ("👨‍🔬🧬🧪", "ciencia"),
            ("🕵️‍♂️🔍💼", "sherlock holmes"),
            ("👨‍🍳🔥🍝", "chef"),
            ("👨‍🔬🧪🧫", "laboratorio"),
            ("👧🌪️🌈", "el mago de oz"),
            ("👨‍🎨🎨🖼️", "pintor"),
            ("🪖⚔️🛡️", "guerrero"),
            ("🎤🎶👩‍🎤", "cantante"),
            ("👑🗡️🐉", "rey"),
            ("🧚‍♀️✨🌙", "hada"),
            ("🧞‍♂️🔮🕌", "aladdin"),
            ("👻🏚️🌙", "fantasma"),
            ("🎄🎁🎅", "navidad"),
            ("🎃👻🕯️", "halloween"),
            ("🪁🌬️🌤️", "viento"),
            ("🐱🦁🎪", "circo"),
            ("🧙‍♀️🧹🌌", "bruja"),
            ("🧊🐻❄️", "ártico"),
            ("🌋🌪️🌊", "desastre natural"),
            ("🛸👽🌌", "ovni"),
            ("🏹🦌🌲", "cazador"),
        ]
        pregunta, respuesta = random.choice(quizzes)
        await update.message.reply_text(f"🎬 ¿Qué representa esto?: {pregunta}", reply_to_message_id=update.message.message_id)
        print("CMD | Comando /emoquiz ejecutado.")

        def check(msg):
            return msg.text.lower() == respuesta.lower() and msg.from_user.id == update.message.from_user.id

        try:
            msg = await context.bot.wait_for_message(timeout=15, chat_id=update.effective_chat.id)
            if msg.text.lower() == respuesta:
                await msg.reply_text("🎉 ¡Correcto!", reply_to_message_id=update.message.message_id)
            else:
                await msg.reply_text(f"❌ No era correcto. Era: {respuesta}", reply_to_message_id=update.message.message_id)
        except:
            await update.message.reply_text("⏰ Tiempo agotado.", reply_to_message_id=update.message.message_id)

def setup():
    return EmoQuiz()