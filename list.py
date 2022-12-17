# список
my_list = [1,2,3,4,456,4,56,67]

# коллекции

# кортеж
my_tuple = (1,5,6,7,8,945) # кортеж, по сути - неизменяемый список

# множество
my_set = {12,45,6,8,7,9,0, 5678, 9} # у множества нет индексации, вывод осуществляется в случайном порядке. Множество тратит меньше места в памяти, чем лист
my_set2 = {3,45,9,7,}

# словарь
my_dict = {(1, 45,67): 'one', 2: 'two', 3: 'three'} # словарь dict  => в данном случае 1 (2, 3) это ключ
my_dict2 = {'+': 888, 2: 'два'}


print(my_list)
print(my_set)
print(my_set.difference(my_set2)) # показывает различия между my_set и my_set2


my_set.pop() # удаляет последний элемент, но так как это множество => вывод случайный и следовательно элемент удаляется случайный
print(my_set)
my_list.pop()
print(my_list) # [1, 2, 3, 4, 456, 4, 56] удаляет последний элемент


my_set.remove(9) # удалить первый совпавший элемент последовательности
print(my_set)


print(my_dict.get(2)) # two
print(my_dict.get((1, 45,67))) # one (кортеж тоже может быть ключом)
print(my_dict.get(9, 'Такого значения нет')) # вывод => такого значения нет
my_dict ['new key'] = 'Мы добавили новый ключ' # добавили новые ключ - значение
print(my_dict)
my_dict ['new key'] = 'Мы обновили этот ключ' # обновили новые ключ - значение
print(my_dict)

my_dict.update(my_dict2) # добавляет новые и переписывает значения с совпадающим ключом
print(my_dict)

keys = set()
for i in my_dict:
    keys.add(i)
for i in my_dict2:
    keys.add(i)
print(keys)



storage = {'Ананас': 3, 'Банан': 2}
delivery = {'Ананас': 7, 'Банан': 5, 'Лайм': 2}

new_dict = {}
keys_1 = set()
for i in keys_1:
    new_dict[i] = storage.get(i, 0) + delivery.get(i, 0)
print(storage)
print(delivery)
print(new_dict) # !!!!!!!!!!!!!!!!

print('storage.items() выведет ключ + значение')
for i in storage.items(): # выведет ключ + значение
    print(i)

print('storage.keys() выведет ключ')
for i in storage.keys(): # выведет ключ (это значение по умолчанию)
    print(i)

print('storage.values() выведет значение')
for i in storage.values(): # выведет значение
    print(i)


people_id = {}
people_id[1] = {'name': 'STONE', 'age': 38, 'comment': 'Молодец'}
people_id[2] = {'name': 'Андрей беляев', 'age': 18, 'comment': 'Еще больший молодец'}
print(people_id)
print(people_id.get(1).get('name'))