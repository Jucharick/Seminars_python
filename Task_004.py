# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#  *Примеры:*
#  - 6,78 -> 7
#  - 5 -> нет
#  - 0,34 -> 3

# первый вариант
num = float(input('Введите дробное число: '))
if num == int(num): # если введенное число (например, 5.0) равно преобразованному в int (5) => значит дробной части нет
    print('дробной части нет')
else:
    print(int(num * 10 % 10))

# второй вариант
num = (input('Введите дробное число: '))
list = num.split('.')
if len(list) > 1: # проверка число ли (длина списка)
    print(list[1][0]) # в строке символы тоже стоят на своих индексах, по split('.') мы делим на две подстроки и обращаемся ко второму числу [1], а в нем выбираем первое число [0]
    # 4.56 => [4, 56] => list[0] - это 4, list[0] - это 56
else:
    print('дробной части нет')



from decimal import Decimal # библиотека позволяет работать с плавающими точками
number = Decimal ('0.56')
print(number*10) # при таком варианте НЕ будет хвоста 5.6000000000000005; ответ 5.60

number_1 = 0.56
print(number_1*10) # 5.6000000000000005