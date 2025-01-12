from config import TELEGRAM_BOT_TOKEN
from python_reference import python_help_dict
from bot import PythonHelperBot, NOT_FOUND_MASSAGE

from telegram import Update
from telegram.ext import Application, MessageHandler

bot=PythonHelperBot(python_help_dict)
async def helper(update, context):
    user_message = update.message.text
    answer=bot.get_help(user_message)
    await update.message.reply_text(answer)

def run_bot():
    telegram_bot=Application.builder().token(TELEGRAM_BOT_TOKEN).build()
    telegram_bot.add_handler(MessageHandler(filters=None, callback=helper))
    print('Бот запущен')
    telegram_bot.run_polling(allowed_updates=Update.ALL_TYPES)
    print('Бот остановлен')

if __name__=='__main__':
    run_bot()




