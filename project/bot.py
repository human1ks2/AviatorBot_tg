# bot.py
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, CallbackContext
from config import TOKEN

async def start(update: Update, context: CallbackContext):
    # Укажи свой актуальный ngrok URL:
    ngrok_url = "https://945b-194-87-220-42.ngrok-free.app"  # Заменить на свой публичный URL

    # Создаем инлайн кнопку с WebApp
    keyboard = [
        [InlineKeyboardButton("🎮 Играть", web_app=WebAppInfo(url=ngrok_url))]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Отправляем сообщение с кнопкой
    await update.message.reply_text(
        "Привет! Нажми кнопку ниже, чтобы открыть игру 👇",
        reply_markup=reply_markup
    )

def main():
    # Инициализация Application с токеном
    application = Application.builder().token(TOKEN).build()

    # Обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запуск бота
    application.run_polling()

if __name__ == "__main__":
    main()
