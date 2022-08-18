# подключение библиотеки telebot
# В google colab добавить: !pip install pyTelegramBotAPI
# для установки необходимо в файл requirements.text добавить строку
# 'PyTelegramBotApi'
from telebot import TeleBot, types
import json

bot = TeleBot(token='5417708512:AAGdoxl4PT6v9jx_9uYP1mx3kVaxUdF-gC8', parse_mode='html') 


# обработчик команды '/start'
@bot.message_handler(commands=['start'])
def start_command_handler(message: types.Message):
    # отправляем ответ на команду '/start'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Мой репозиторий")
    item2 = types.KeyboardButton("Написать мне в личку")

    markup.add(item1, item2)

    bot.send_video(message.chat.id, 'https://c.tenor.com/38Yekx6F7vEAAAAC/predator-arnold.gif', None, 'Text')
    bot.send_message(
        chat_id=message.chat.id, # id чата, в который необходимо направить сообщение
        text='Привет, {0.first_name}! Я умею проверять JSON и форматировать его в красивый текст.\n\nВведи JSON в виде строки или выбери одно из действий ниже'.format(message.from_user, bot.get_me()), reply_markup=markup, # текст сообщения
    )


# обработчик всех остальных сообщений
@bot.message_handler()
def message_handler(message: types.Message):
    if message.text == 'Мой репозиторий':
            bot.send_message(message.chat.id, 'https://github.com/NikTi-it')
    elif message.text == 'Написать мне в личку':
            bot.send_message(message.chat.id, 'https://t.me/nikitit')
    else:
            try:
                payload = json.loads(message.text)
            except json.JSONDecodeError as ex:
                bot.send_message(chat_id=message.chat.id,text=f'При обработке произошла ошибка:\n<code>{str(ex)}</code>')
                return
            text = json.dumps(payload, indent=2, sort_keys=True, ensure_ascii=False)
            bot.send_message(chat_id=message.chat.id,text=f'JSON:\n<code>{text}</code>')


# главная функция программы
def main():
    # запускаем нашего бота
    bot.infinity_polling()


if __name__ == '__main__':
    main()
