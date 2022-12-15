# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#     Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

# # первый вариант (неоптимально заводить 5 переменных)
# num_1 = int(input('Введите число 1: '))
# num_2 = int(input('Введите число 2: '))
# num_3 = int(input('Введите число 3: '))
# num_4 = int(input('Введите число 4: '))
# num_5 = int(input('Введите число 5: '))

# print(max(num_1, num_2, num_3, num_4, num_5))

# # второй вариант
# list = input('введите 5 чисел: ').split(", ") # split разбивает строку на подстроки
# max_number = max(list)
# print('Наибольшее число', max_number)

# третий вариант
my_list = []

for i in range(5):
    number = int(input(f'Введите {i+1} число: '))
    my_list.append(number)
print(my_list)

max = my_list[0]
for item in my_list:
    if my_list[item] > max:
        max = my_list[item]

print(f'В данном списке максимальное число {max}')
