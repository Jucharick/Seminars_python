# Напишите программу, которая при вводе количества строк выведет соответсвующее количество строк с символом * следующим образом:
# => 5
# *****
# ****
# ***
# **
# *

number = int(input('Введите количество строк: '))
for number in range(number, 0, -1):
    print('*' * number)