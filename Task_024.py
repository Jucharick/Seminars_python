# Имеется список id сотрудников из 10 элементов, каждый id - случайное число от 1 до 100
# Имеется список имен сотрудников из 10 элементов.
# Сопоставьте каждому имени сотрудника его id и выведите получившийся список.
# Выведите имена сотрудников, получивших нечетное id. Решите с помощью zip, filter и lambda.
import random

id = [random.randint(1, 101) for i in range(10)]
names = ['ivanov', 'petrov', 'sidorov', 'kuznecov', 'potapov', 'laptin', 'skvor', 'jukov', 'si', 'li', ]

lst = list(zip(id, names))
print(lst)

list_odd = [elem[1] for elem in lst if elem[0] % 2 !=0]
print(list_odd)