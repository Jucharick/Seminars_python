# Напишите программу, которая сортирует элементы массива по возрастанию по последней десятичной записи чисел
#
# Входные данные
# 216 234 890 81 73 96
#
#
# Ответ
# 890 81 73 234 96 219
# Программа должна вывести в одной строке элементы массива, отсортированного по возрастанию последней цифры в десятичной записи чисел, раздели их 
# пробелами. Числа, у которых последняя цифра одинаковая, должны быть выведены в том же порядке, в каком они стояли в исходной последовательности.


my_array = [219, 234, 890, 81, 73, 96]
r = sorted(my_array, key = lambda x: x%10) 
print(r)

