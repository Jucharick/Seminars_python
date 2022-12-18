# Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что ее нет.
# Пример:
# список: ['qwe', 'asd', 'zxc', 'qwe', 'eqwe'], ищем 'qwe' => ответ 3
# список: ['йцу', 'фыв', 'ячс', 'цук', 'йцукен', 'йцу'], ищем 'йцу' => ответ 5
# список: ['123', '234', 123, '567'], ищем '123' => ответ -1
# если второго вхождения нет => выводим -1

my_list = ['qwe', 'asd', 'zxc', 'qwe', 'eqwe']
print(my_list)
search = 'qwe'
print(search)
count = 0
position = 0
for item in my_list:
    if search == item:
        count+=1
    if count == 2:
        break
    position +=1
if count >=2:
    print(f'позиция второго вхождения строки {position}') 
else:
    print('-1') 
print()


# вариант преподавателя
my_list1 = ['qwe', 'asd', 'zxc', 'qwe', 'eqwe']
my_list2 = ['йцу', 'фыв', 'ячс', 'цук', 'йцукен', 'йцу']
my_list3 = ['123', '234', 123, '567']

def check(my_list: list, search: str):
    count = 0
    for i in range(len(my_list)): # используем range потому что работаем с индексами
        if search == my_list[i]:
            count+=1
            if count == 2:
                print(f'позиция второго вхождения строки {i}')
                break
    else:
        print('-1')

check(my_list1, 'qwe')
check(my_list2, 'йцу')
check(my_list3, '123')