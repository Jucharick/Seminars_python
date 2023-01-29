# python3 -m venv .lib
# установить библиотеку pip install pytelegrambotapi

import telebot
from telebot import types
user_sweet = 0
bot = telebot.TeleBot('5999387270:AAGCy3Qz8UiI4fQFikMAV1S9Fxwl4C2S_O0')

@bot.message_handler(commands = ['start']) # вызов функции по команде в списке
def start(message):
    bot.send_message(message.chat.id, f'/button') # отправка сообщения (кому отправляем, что отправляем(str))

def sum(message):
    summa = sum(list(map(int, message.text.split())))
    bot.send_message(message.chat.id, str(summa))
    button(message)

@bot.message_handler(commands = ['sweet']) # вызов функции по команде в списке
def sweet(message):
    bot.send_message(message.chat.id, f'Привет! {message.from_user.first_name}. Введи колличество конфет: ') # отправка сообщения (кому отправляем, что отправляем(str))
    bot.register_next_step_handler(message, input_sweet)
    print(user_sweet)

def input_sweet(message):
    global user_sweet
    user_sweet = int(message.text)
    button(message)

@bot.message_handler(commands = ['help']) # вызов функции по команде в списке
def help(message):
    bot.send_message(message.chat.id, '/start\n/sweet') # отправка сообщения (кому отправляем, что отправляем(str))

@bot.message_handler(commands = ['button'])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1= types.KeyboardButton('сумма')
    but2= types.KeyboardButton('конфеты')
    markup.add(but1)
    markup.add(but2)
    bot.send_message(message.chat.id, 'выбери кнопку ниже', reply_markup=markup)

@bot.message_handler(content_types= ['text'])
def controller(message):
    if message.text == 'сумма':
        bot.send_message(message.chat.id, f'Введи два числа через пробел для нахождения их суммы')
        bot.register_next_step_handler(message, sum)
    elif message.text == 'конфеты':
        bot.send_message(message.chat.id, f'Привет! {message.from_user.first_name}. Введи колличество конфет: ') # отправка сообщения (кому отправляем, что отправляем(str))
        bot.register_next_step_handler(message, input_sweet)
        print(user_sweet)

bot.infinity_polling() # бот проверяет не пришли ли какие-то сообщения