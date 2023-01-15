# Дана последовательность чисел. Получить список уникальных элементов
# заданной последовательности.

# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10]


num_list = [1, 2, 3, 5, 1, 5, 3, 10, 13, 2, 3, 123]
my_dict = {}
new_list = []


# 1 вариант
for i in range(len(num_list)):
    my_dict[num_list[i]] = my_dict.get(num_list[i], 0) + 1
print (my_dict)

for key, value in my_dict.items():
    if value == 1:
        new_list.append(key)

print(new_list)


# 2 вариант
for i in num_list:
    if num_list.count(i) == 1:
        print(i)


# 3 вариант list comprehension
new_list_2 = [x for x in num_list if num_list.count(x) == 1]
print(new_list_2)