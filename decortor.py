# декоратор на вход принимает функцию и возвращает функцию

import telebot
bot = telebot.TeleBot('')


def decorator(func):
    import time
    def wrapper(url):
        print('Проверяем работу нашей программы')
        start = time.time()
        func(url)
        end = time.time()
        print(f'Функция работает за {end - start} секунд')
    return wrapper


@decorator
def hello():
        print('hello')


@decorator
def how_u():
    print('How are you?')


@decorator
def requests_url(url):
    import requests
    response = requests.get(url)
    return response


print(requests_url('https://github.com'))


@bot.message_handler(commands = ['sweet']) # вызов функции по команде в списке
def sweet(message):
        pass