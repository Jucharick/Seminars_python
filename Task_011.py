# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#     *Пример:*
#     - Для N = 5: 1, -3, 9, -27, 81

# первый вариант
n = int(input('Введите число: '))
r = 1
for i in range(n):
    print (r, end = '  ')
    r*=-3
print()


# второй вариант
num = int(input('Введите число: '))
my_list = []
for i in range(num):
    my_list.append((-3)**i) # любое число в степени 0 = 1
print(my_list)
