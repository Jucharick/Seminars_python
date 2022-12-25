# Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

import datetime
import time

# # def random_int(num):
# #     rand = datetime.datetime.now().microsecond%num
# #     return rand+1



def random_int(num):
    time.sleep(0.01) # добавляем задержку для того, чтобы работало в цикле, но таким образом замедляем нашу программу
    rand = datetime.datetime.now().microsecond/10**6  # datetime.datetime.now().microsecond вернет микросекунды;  делим на миллион, потому что нам надо получить дробь
    return round(((num+1)*rand), 2)

print(random_int(int(input('Введите число: '))))

n = int(input('Введите число: '))
for i in range(n):
    print(random_int(i+1), end = " ")
