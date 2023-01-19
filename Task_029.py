# Входные данные
# 5 65 8 31 21 219
# Программа должна вывести в одной строке элементы массива отсортированного в порядке убывания сумм цифр
# десятичного числа разделив их пробелами


a = "5 65 8 18 3 31 21 219"
my_array = list(map(int, a.split()))



def sum_num(num):
    sum = 0
    while num > 0:
        sum += num%10
        num = num//10
    return sum


r = sorted(my_array, key = sum_num, reverse=True) 
print(r)