from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.message.from_user.first_name
    await update.message.reply_text(f'Hello, {user_first_name}!')
    
if __name__ == '__main__':
    # Make sure to replace your token with a valid one
    application = ApplicationBuilder().token('7079751398:AAHzb-4mKMqzIqduRKhXkWSfTydj5UIT5Aw').build()
    application.add_handler(CommandHandler('start', start))
    application.run_polling()


# измененный файл аязом
