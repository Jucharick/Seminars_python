# Задайте два числа. Напишите программу, которая найдет НОК (наименьшее общее кратное) этих двух чисел.

num_1 = int(input('Введите число: '))
num_2 = int(input('Введите число: '))

for i in range(1, num_1*num_2+1):
    if i % num_1 == 0 and i % num_2 == 0:
        print(f'НОК => {i}')
        break # выходим при нахождении наименьшего (идем от 1 до num_1*num_2)