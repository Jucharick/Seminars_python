my_string = '\tПитон самый лучший в мире язык\n'

new_string1 = my_string.split() # по умолчанию делит по символу 'пробел'; не могут идти за другим

print(my_string)
print(new_string1)

new_string2 = my_string.replace('и', '$').replace(' ', '') # реплейсы могут идти один за другим потому что возвращается строка
print(new_string2)

new_string3 = my_string.strip() # убирает табуляцию и пробелы в начале и в конце строки
print(new_string3)

if my_string.lower().startswith('\tпит'):
    print('Да, все верно')

if my_string.strip().upper().startswith('\tПИТ'):
    print(my_string.upper())


# lower()  перевод в нижний регистр
# upper()  перевод в верхний регистр
# startswith('\tпит') начинается с 


my_list = ['21', '23', '45', 'fgghm', '45fs', 'gdg',]
add = ' '

print(add.join(my_list))

# join()  склеивает через add список и превращает в строку (работает только со строками)


my_dict = {1: '456', 32: 'fjbntb', 3: 4, 'sdfdbbg': '545756', 'Список': [234, 457, 7]}
print(my_dict[1]) # в [] пишем ключ
print(my_dict.get(2, 'Нет такого ключа'))
print(my_dict.get(32, 'Нет такого ключа'))
print(my_dict.get(2, 0)) # вернет 0 => потому что ключа 2 нет (можно использовать в домашней работе для подсчета num)

my_dict['New_key'] = 'value' # добавляем новый элемент в словарь my_dict в конец
print(my_dict)

my_dict[3] = my_dict.get(3) + 1 # под ключем 3 int
print(my_dict)
