# Напишите программу на Python для поиска пересечения двух заданных мфссивов с помощью lambda
# [1, 2, 3, 5, 7, 8, 9, 10]
# [1, 2, 4, 8, 9]

num_1 = [1, 2, 3, 5, 7, 8, 9, 10]
num_2 = [1, 2, 4, 8, 9]


res = list(filter(lambda x:  x in num_2, num_1))

print(res)