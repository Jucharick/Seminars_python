# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
# *Примеры:*
# - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

# первый вариант
num = int(input('Введите целое число: '))
naumbers = list(range(-1*num, num+1))
print(naumbers)


# второй вариант
num = int(input('Введите целое число: '))
my_list = []
for i in range(-num, num+1):
    my_list.append(i)
    
print(*my_list, sep = ', ') # *  выводит содержимое my_list, без []; sep разделяет через ,
# print(i, and = ', ') # and - что print добавляет в конце (\n по умолчанию)