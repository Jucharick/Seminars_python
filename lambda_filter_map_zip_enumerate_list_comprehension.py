# lambda, filter, map, zip, enumerate, list comprehension
from random import randint as RI

# list comprehension
list1 = [i for i in range(1, 11)]
print(list1)

# словарь
my_dic = {x: x**2 for x in range(10)}
print(my_dic)


# enumerate
# a = [1, 4, 9, 16, 25, 36, 49, 64]
# for indx, value in enumerate (a):
#     print(indx, value)


# zip
users = ['user1', 'user2', 'user3', 'user4', 'user5']
ids = [4, 5, 9, 14, 7]
data = list(zip(users, ids))
print(data)
print(data[1][0]) # выводим user2 - кортеж с индексом [1] и с элементом кортежа с индексом [0]


# lambda
def sum(a, b):
    return a+b
print(sum(3, 5))


def sum2(a, b): return a+b
print(sum2(3, 5))


def sum3(a, b): return a+b if a >= 5 else 0
print(sum3(7, 6))


def print_smile(name):
    print (f'{name}, Улыбнись!')
on_click = lambda name: print_smile(name)

on_click('Юля')


# map
l = [i for i in range(12)]
l = list(map(lambda x: x+10 if x > 6 else x+0, l))
print(l)


# filter
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
def chek_num(x):
    if x%2 == 0:
        return True

list_1_chet = list(filter(chek_num, list_1))
print(list_1_chet)

list_2_chet = list(filter(lambda x: not x%2, list_1))
print(list_2_chet)