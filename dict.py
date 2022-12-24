# Считаем сколько раз в строке num_list встречается цифра


my_dict = {}

num_list = '246395609473492461387463856437'

for dig in num_list:
    my_dict[dig] = my_dict.get(dig, 0) + 1

print(my_dict)