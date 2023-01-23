import controller

commands = ['Открыть файл',
            'Сохранить файл',
            'Показать все контакты',
            'Создать контакт',
            'Удалить контакт',
            'Изменить контакт',
            'Найти контак',
            'Выход из программы']

def menu():
    print('Главное меню:')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}. {item}') # \t табуляция 
    request = int(input('Выберите пункт меню: '))
    return request


def show_contacts(phone_list: list):
    if len(phone_list) < 1:
        print('Телефонная книга пуста или не открыта')
    else:
        print()
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:30} {contact[1]:13} {contact[2]}')
    print()
        

def input_err():
    print('Вы ввели некоррекное значение.')

def create_contact():
    name = input('Введите ФИО: ')
    phone = input('Введите номер телефона: ')
    comment = input('Укажите комментарий: ')
    return name, phone, comment

def find_contact():
    find = input('Введите искомый элемент: ')
    return find