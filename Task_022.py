# Сделать с помощью  filter, lambda
# Напишите программу, удаляющую из текста все слова, содержащие "абв"
# Вывести все пробелы и их индексы из предыдущей строки

str = 'asd вмыл ывсьд фбв абв Абв мтм'
my_list = str.split()
my_list_2 = list(filter(lambda x: 'абв' not in x.lower(), my_list))

print(' '.join(my_list_2)) # ' '.join преобразует строку из списка, соединяя элементы списка пробелом

for i, value in enumerate (str):
    if value == ' ':
        print(i)