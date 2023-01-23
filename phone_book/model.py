# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать все контакты
# 4. Сохранить контакт
# 5. Удалить контакт
# 6. Изменить контакт
# 7. Найти контак 
# 8. Выход из программы

phone_book = []
path = 'C:/Users/Юлия Чарикова/Desktop/GeekBrains/I четверть - блок 2/Знакомство с языком Python/Seminars/phone_book/data.txt'

def get_phone_book():
    global phone_book
    return phone_book

def open_file():
    global path
    global phone_book
    with open(path, 'r', encoding='utf-8') as data: # преобразую в utf-8, иначе ошибка (кириллица)
        file = data.readlines()
    for contact in file:
        phone_book.append(contact.strip().split(';'))
    print('Файл открыт')
    return file

def add_new_contact(new_contact: list):
    global phone_book
    phone_book.append(new_contact)

# def update_contact():

def search_contact(find: str):
    global phone_book
    result = []
    for contact in phone_book:
        for field in contact:
            if find in field:
                result.append(contact)
                break
    return result        

def save_file():
    global path
    global phone_book
    pb_str = []
    for contact in phone_book:
        pb_str.append(';'.join(contact))
    with open(path, 'w', encoding='utf-8') as data: # преобразую в utf-8, иначе ошибка (кириллица)
        data.write('\n'.join(pb_str))

def exit_phone_book():
    exit()