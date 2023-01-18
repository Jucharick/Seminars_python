a = [1, 6, 5, 8, 3, 7]
a.sort()
print(a)


b = (3, 5, 6, 54, 3, 2)
new_b = sorted(b) # a.sort() не сортирует кортежи, для их сортировки можно использовать sorted() => возвращает список
print(new_b)

c = [12, 34, 567, 671]
new_c = sorted(c, reverse=True) # сортировка по убыванию
print(new_c)

def sorting(x):
    if x%2==0:
        return True
    else:
        return x # если False => то сортировка будет по возрастанию

r = sorted(c, key = sorting)
print(r)


my_str = ['dfdc', 'ddcd', 'sd', 'ds', 'qdsfsfvfsds'] 
rr = sorted(my_str, key = len) # сортировка по длине строки
print(rr)
rrr = sorted(my_str, key = lambda x: x[0]) # сортировка по первому символу
print(rrr)


my_dic = { 4: 'cdc', 3: 456, 9: 'dvl,vlkdmcljdcm'}
rrrr = sorted(my_dic) # сортировка по ключам
print(rrrr)