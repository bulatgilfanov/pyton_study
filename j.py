import telebot

bot = telebot.TeleBot('6893343209:AAE0T6ZBHb3Nh_HqxQ6mDOaTzF2OF2qtrIs')

from telebot import types

@bot.message_handler(commands=['help'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🇷🇺 Русский")
    btn2 = types.KeyboardButton('🇬🇧 English')
    markup.add(btn1, btn2)
    bot.send_message(message.from_user.id, "🇷🇺 Выберите язык / 🇬🇧 Choose your language", reply_markup=markup)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Поздороваться")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-фоторедактор!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Поздороваться':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)  # создание новых кнопок
        btn1 = types.KeyboardButton('Как стать автором на Хабре?')
        btn2 = types.KeyboardButton('Правила сайта')
        btn3 = types.KeyboardButton('Советы по оформлению публикации')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '❓ Задайте интересующий вопрос', reply_markup=markup)  # ответ бота
    elif message.text == 'Как стать автором на Хабре?':
        bot.send_message(message.from_user.id, 'а', parse_mode='Markdown')

    elif message.text == 'Правила сайта':
        bot.send_message(message.from_user.id, 'о', parse_mode='Markdown')

    elif message.text == 'Советы по оформлению публикации':
        bot.send_message(message.from_user.id, 'р', parse_mode='Markdown')

bot.polling(none_stop=True, interval=0)  # обязательная для работы бота часть