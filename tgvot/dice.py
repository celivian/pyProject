# Импортируем необходимые классы.
import datetime
import logging
from telegram.ext import Application, MessageHandler, filters, CommandHandler, ConversationHandler
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
import random

# Запускаем логгирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)
reply_keyboard = [['/dice', '/timer']]
reply_keyboard2 = [
    ['кинуть один шестигранный кубик', 'кинуть 2 шестигранных кубика одновременно', 'кинуть 20-гранный кубик',
     'вернуться назад']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
markup2 = ReplyKeyboardMarkup(reply_keyboard2, one_time_keyboard=False)


async def start(update, context):
    await update.message.reply_text(
        "Я бот-справочник. Какая информация вам нужна?",
        reply_markup=markup
    )


async def close_keyboard(update, context):
    await update.message.reply_text(
        "Ok",
        reply_markup=ReplyKeyboardRemove()
    )


async def echo(update, context):
    # У объекта класса Updater есть поле message,
    # являющееся объектом сообщения.
    # У message есть поле text, содержащее текст полученного сообщения,
    # а также метод reply_text(str),
    # отсылающий ответ пользователю, от которого получено сообщение.
    if update.message.text == 'кинуть один шестигранный кубик':
        await one_six
    await update.message.reply_text('Я получил сообщение ' + update.message.text)


async def dice(update, context):
    await update.message.reply_text('Выбирайте действие', reply_markup=markup2)


async def back(update, context):
    await update.message.reply_text('Выбирайте действие', reply_markup=markup)


async def one_six(update, context):
    await update.message.reply_text(str(random.randint(1, 6)), reply_markup=markup2)


async def two_six(update, context):
    await update.message.reply_text(f'{random.randint(1, 6)}, {random.randint(1, 6)}', reply_markup=markup2)


async def one_twenty(update, context):
    await update.message.reply_text(str(random.randint(1, 20)), reply_markup=markup2)


async def timer(update, context):
    await update.message.reply_text("Телефон: +7(495)776-3030")


def main():
    # Создаём объект Application.
    # Вместо слова "TOKEN" надо разместить полученный от @BotFather токен
    application = Application.builder().token("7031572138:AAHX1APB7hEIyYrbUib-BQotQuZMr-d-3Fo").build()

    # Создаём обработчик сообщений типа filters.TEXT
    # из описанной выше асинхронной функции echo()
    # После регистрации обработчика в приложении
    # эта асинхронная функция будет вызываться при получении сообщения
    # с типом "текст", т. е. текстовых сообщений.
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("dice", dice))
    application.add_handler(CommandHandler("timer", timer))
    application.add_handler(CommandHandler("close", close_keyboard))
    application.add_handler(CommandHandler("кинуть один шестигранный кубик", one_six))
    application.add_handler(CommandHandler("кинуть 2 шестигранных кубика одновременно", two_six))
    application.add_handler(CommandHandler("кинуть 20-гранный кубик", one_twenty))
    application.add_handler(CommandHandler("back", back))

    # Запускаем приложение.
    application.run_polling()


# Напишем соответствующие функции.
# Их сигнатура и поведение аналогичны обработчикам текстовых сообщений.

# Запускаем функцию main() в случае запуска скрипта.
if __name__ == '__main__':
    main()
